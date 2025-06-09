## Contracts, prices, and no-arbitrage
Consider the following contract
- Pay price $p$ at time $t = 0$
- Receive $c_k$ at time $t = k, k = 1,... ,T$
Note that the cash flow c could be negative!
  
The no-arbitrage condition bounds the price $p$ for this contract
- Weak No-Arbitrage: $c_k \geq 0$ for all $k \geq 1 \to p \geq 0$
- Strong No-Arbitrage: $c_k \geq 0$ for all $k \geq 1$ and $c_l > 0$
    
    for some $l \to p > 0$
    
Essentially eliminate the possibility of a free-lunch
  
The rationale for the **weak** no-arbitrage condition: Suppose $p < 0$:
- Since $c_k \geq 0$ for all $k \geq 1$, the buyer receives $-p > 0$ at time $0$, and then does not lose money thereafter. Free lunch!
- The seller can increase the price as long as $p \leq 0$, and still have buyers available.
- Buyers will be willing to pay a higher price in order to compete.
## Assumptions underlying no-arbitrage
The rationale for the **strong** no-arbitrage condition
- Suppose $p \leq 0$.
- Recall that for some $c_l > 0$ for some $l \geq 1$. Therefore, free lunch as long as $p \leq 0$.
- We can only guarantee that $p > 0$ but not the precise value!
Implicit assumptions underlying the no-arbitrage condition
- Markets are liquid: a sufficient number of buyers and sellers
- The price information is available to all buyers and sellers
- Competition in supply and demand will correct any deviations from no-arbitrage prices
  
## Pricing a simple bond
What is the price of a contract $p$ that pays A dollars in 1 year?
Suppose one is able to borrow and lend unlimited amounts at an interest rate of $r$ per year.
  
Construct the following **portfolio:**
- **Buy** the contract at price $p$
- **Borrow $\frac{A}{1 + r}$** at interest rate $r$
Cash flows associated with this portfolio:
- Price of portfolio:
$$z = p - \frac{A}{1+r}$$
- Cashflow in 1 year:
$$A - A = 0$$
Weak No-arbitrage: $c_1 \geq 0$ implices price $z \geq 0$, i.e., $p \geq \frac{A}{1 + r}$
  
Next, construct the following **portfolio:**
- **Sell** the contract at price $p$
- **Lend $\frac{A}{1 + r}$** at interest rate $r$
Cash flows associated with this portfolio:
- Price of portfolio:
$$z = p - \frac{A}{1+r}$$
- Cashflow in 1 year:
$$- A + A = 0$$
Weak No-arbitrage: $c_1 \geq 0$ implices price $z \geq 0$, i.e., $p \leq \frac{A}{1 + r}$
Two results together imply $p = \frac{A}{1+r}$. Surprise?
The result relied on the ability to borrow and lend at rate r.
- What if borrowing and lending rates are different?
- What if borrowing and lending markets are elastic?