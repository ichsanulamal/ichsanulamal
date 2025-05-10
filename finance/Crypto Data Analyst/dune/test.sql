-- 1

-- What is the number of pairs being created containing tokens USDC and/or WETH?

-- select count(pair)
-- from uniswap_v2_ethereum.Factory_evt_PairCreated
-- -- USDC: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 | WETH: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
-- where token0 in (0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48, 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2)
--     and token1 in (0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48, 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2)

select 
    p.evt_block_time as time
    , p.pair as pair_address
    , p.token0
    , t0.symbol as t0_symbol
    , p.token1
    , t1.symbol as t1_symbol
    , t0.blockchain as b0 , t1.blockchain as b1
from uniswap_v2_ethereum.Factory_evt_PairCreated p

left join tokens.erc20 t0 
    on t0.contract_address = p.token0
left join tokens.erc20 t1
    on t1.contract_address = p.token1

-- USDC: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 | WETH: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
where token0 in (0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48, 0x03aa6298f1370642642415edc0db8b957783e8d6)
    and token1 in (0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48, 0x03aa6298f1370642642415edc0db8b957783e8d6)
    -- and t0.blockchain = 'ethereum' and t1.blockchain = 'ethereum'


-- 2

-- 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc
with 
    frequency as (
        SELECT 
            date_trunc('week', evt_block_time) time
            , count(*) as num_swaps
        FROM uniswap_v2_ethereum.Pair_evt_Swap
        WHERE contract_address = 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc
        GROUP BY 1
    ),
    
    volume as (
        with 
            base as (
                SELECT 
                    date_trunc('minute', s.evt_block_time) time
                    , case when cast(amount0Out as double) = 0 then p.token1 else p.token0 end as token_bought_address
                    , case when cast(amount0Out as double) = 0 then cast(amount1Out as double) else cast(amount0Out as double) end as token_bought_amount_raw
                FROM uniswap_v2_ethereum.Pair_evt_Swap s
                LEFT JOIN uniswap_v2_ethereum.Factory_evt_PairCreated p ON p.pair = s.contract_address
                WHERE s.contract_address = 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc
            )
        
        SELECT 
            date_trunc('week', b.time) time
            , sum(token_bought_amount_raw / pow(10,COALESCE(t.decimals,18)) * p.price) as total_usd_amount
        FROM base b
        LEFT JOIN tokens.erc20 t ON t.contract_address = b.token_bought_address
        LEFT JOIN prices.usd p ON p.minute = b.time AND p.blockchain = 'ethereum' AND p.contract_address = b.token_bought_address
        GROUP BY 1
    )
    
    , dex_trades as (
        SELECT
            date_trunc('week',block_date) week
            , count(*) as num_swaps_dx
            , sum(amount_usd) total_usd_amount_dx
        FROM dex.trades
        WHERE blockchain = 'ethereum'
        AND project_contract_address = 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc
        GROUP BY 1
    )
    
SELECT 
    v.time
    , f.num_swaps
    , v.total_usd_amount
    , dx.total_usd_amount_dx
    , dx.num_swaps_dx
FROM volume v
LEFT JOIN frequency f ON f.time = v.time
LEFT JOIN dex_trades dx ON dx.week = v.time