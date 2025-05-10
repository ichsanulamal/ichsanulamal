import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class IndonesianValueInvestor:
    """
    A class to analyze Indonesian stocks based on Buffett's value investing principles
    """
    
    def __init__(self):
        # IDX tickers list
        self.idx_tickers = []
        # Dictionary to store stock data
        self.stock_data = {}
        
    def get_idx_tickers(self):
        """Scrape to get list of stocks from Indonesia Stock Exchange"""
        print("Fetching list of Indonesian stocks...")
        
        try:
            # Try to scrape the list of all IDX stocks from Yahoo Finance
            url = "https://finance.yahoo.com/screener/predefined/ms_indonesia/"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the table with stock listings
            table = soup.find('table', {'class': 'W(100%)'})
            
            if table:
                # Extract stock symbols from the table
                self.idx_tickers = []
                rows = table.find('tbody').find_all('tr')
                
                for row in rows:
                    try:
                        # First column contains the ticker symbol
                        ticker_cell = row.find_all('td')[0]
                        ticker = ticker_cell.find('a').text.strip()
                        
                        # Make sure it's an Indonesian stock (should end with .JK)
                        if not ticker.endswith('.JK'):
                            ticker = f"{ticker}.JK"
                            
                        self.idx_tickers.append(ticker)
                    except:
                        continue
            
            # If the scraping didn't work or found no tickers, fall back to an extended list
            if not self.idx_tickers:
                print("Scraping failed, using extended predefined list...")
                self.use_extended_list()
                
        except Exception as e:
            print(f"Error fetching stocks from Yahoo Finance: {e}")
            print("Using extended predefined list instead...")
            self.use_extended_list()
            
        print(f"Found {len(self.idx_tickers)} Indonesian stocks for analysis.")
        return self.idx_tickers
        
    def use_extended_list(self):
        """Use an extended predefined list of Indonesian stocks"""
        # Extended list of Indonesian stocks (over 100 major stocks on IDX)
        self.idx_tickers = [
            # Banks
            'BBCA.JK',  # Bank Central Asia
            'BBRI.JK',  # Bank Rakyat Indonesia
            'BBNI.JK',  # Bank Negara Indonesia
            'BMRI.JK',  # Bank Mandiri
            'BNGA.JK',  # CIMB Niaga
            'BNLI.JK',  # Bank Permata
            'BTPS.JK',  # Bank BTPN Syariah
            'BTPN.JK',  # Bank BTPN
            'MEGA.JK',  # Bank Mega
            'BJTM.JK',  # Bank Jatim
            'BJBR.JK',  # Bank BJB
            'BRIS.JK',  # Bank BRI Syariah
            'BABP.JK',  # Bank MNC Internasional
            'BNBA.JK',  # Bank Bumi Arta
            'BACA.JK',  # Bank Capital Indonesia
            
            # Telecommunications
            'TLKM.JK',  # Telkom Indonesia
            'EXCL.JK',  # XL Axiata
            'ISAT.JK',  # Indosat Ooredoo
            'FREN.JK',  # Smartfren Telecom
            
            # Consumer Goods
            'UNVR.JK',  # Unilever Indonesia
            'ICBP.JK',  # Indofood CBP
            'INDF.JK',  # Indofood Sukses Makmur
            'HMSP.JK',  # HM Sampoerna
            'GGRM.JK',  # Gudang Garam
            'KLBF.JK',  # Kalbe Farma
            'MYOR.JK',  # Mayora Indah
            'ULTJ.JK',  # Ultra Jaya Milk
            'CINT.JK',  # Chitose Internasional
            'DLTA.JK',  # Delta Djakarta
            'MLBI.JK',  # Multi Bintang Indonesia
            'CLEO.JK',  # Sariguna Primatirta
            'KINO.JK',  # Kino Indonesia
            'GOOD.JK',  # Garudafood Putra Putri Jaya
            'ADES.JK',  # Akasha Wira International
            
            # Automotive & Components
            'ASII.JK',  # Astra International
            'AUTO.JK',  # Astra Otoparts
            'GDYR.JK',  # Goodyear Indonesia
            'GJTL.JK',  # Gajah Tunggal
            'IMAS.JK',  # Indomobil Sukses International
            'SMSM.JK',  # Selamat Sempurna
            
            # Property & Construction
            'SMRA.JK',  # Summarecon Agung
            'LPKR.JK',  # Lippo Karawaci
            'BSDE.JK',  # Bumi Serpong Damai
            'PWON.JK',  # Pakuwon Jati
            'CTRA.JK',  # Ciputra Development
            'DMAS.JK',  # Puradelta Lestari
            'PTPP.JK',  # PP (Persero)
            'WIKA.JK',  # Wijaya Karya
            'WSKT.JK',  # Waskita Karya
            'ADHI.JK',  # Adhi Karya
            'TOTL.JK',  # Total Bangun Persada
            'WEGE.JK',  # Wijaya Karya Bangunan Gedung
            
            # Mining
            'ANTM.JK',  # Aneka Tambang
            'PTBA.JK',  # Bukit Asam
            'INCO.JK',  # Vale Indonesia
            'TINS.JK',  # Timah
            'MDKA.JK',  # Merdeka Copper Gold
            'BUMI.JK',  # Bumi Resources
            'HRUM.JK',  # Harum Energy
            'ADRO.JK',  # Adaro Energy
            'ITMG.JK',  # Indo Tambangraya Megah
            
            # Oil & Gas
            'MEDC.JK',  # Medco Energi
            'ESSA.JK',  # Surya Esa Perkasa
            'ELSA.JK',  # Elnusa
            
            # Plantations
            'AALI.JK',  # Astra Agro Lestari
            'LSIP.JK',  # PP London Sumatra Indonesia
            'SIMP.JK',  # Salim Ivomas Pratama
            'SSMS.JK',  # Sawit Sumbermas Sarana
            'SGRO.JK',  # Sampoerna Agro
            
            # Cement
            'SMGR.JK',  # Semen Indonesia
            'INTP.JK',  # Indocement Tunggal Prakarsa
            'SMBR.JK',  # Semen Baturaja
            
            # Steel & Metal
            'KRAS.JK',  # Krakatau Steel
            'ISSP.JK',  # Steel Pipe Industry of Indonesia
            'NIKL.JK',  # Pelat Timah Nusantara
            
            # Technology
            'BUKA.JK',  # Bukalapak
            'GOTO.JK',  # GoTo (Gojek Tokopedia)
            'EMTK.JK',  # Elang Mahkota Teknologi
            'MLPT.JK',  # Multipolar Technology
            'MTDL.JK',  # Metrodata Electronics
            
            # Retail
            'MAPI.JK',  # Mitra Adiperkasa
            'MPPA.JK',  # Matahari Putra Prima
            'ERAA.JK',  # Erajaya Swasembada
            'ACES.JK',  # Ace Hardware Indonesia
            'AMRT.JK',  # Sumber Alfaria Trijaya
            'RANC.JK',  # Supra Boga Lestari
            'MIDI.JK',  # Midi Utama Indonesia
            'LPPF.JK',  # Matahari Department Store
            
            # Transportation & Logistics
            'JSMR.JK',  # Jasa Marga
            'GIAA.JK',  # Garuda Indonesia
            'BIRD.JK',  # Blue Bird
            'PGAS.JK',  # Perusahaan Gas Negara
            'AKRA.JK',  # AKR Corporindo
            'POWR.JK',  # Cikarang Listrindo
            'PPRE.JK',  # PP Presisi
            
            # Healthcare
            'KAEF.JK',  # Kimia Farma
            'MIKA.JK',  # Mitra Keluarga Karyasehat
            'HEAL.JK',  # Medikaloka Hermina
            'PRDA.JK',  # Prodia Widyahusada
            'SAME.JK',  # Sarana Meditama Metropolitan
            
            # Media & Entertainment
            'SCMA.JK',  # Surya Citra Media
            'MNCN.JK',  # Media Nusantara Citra
            'MSIN.JK',  # MNC Studios International
            
            # Others
            'INKP.JK',  # Indah Kiat Pulp & Paper
            'TKIM.JK',  # Pabrik Kertas Tjiwi Kimia
            'FASW.JK',  # Fajar Surya Wisesa
            'JPFA.JK',  # Japfa Comfeed Indonesia
            'CPIN.JK',  # Charoen Pokphand Indonesia
            'MAIN.JK',  # Malindo Feedmill
            'HRTA.JK',  # Hartadinata Abadi
            'MOLI.JK',  # Madusari Murni Indah
        ]
    
    def fetch_financial_data(self, lookback_years=5, batch_size=20):
        """Fetch financial data for Indonesia stocks with batching and progress tracking"""
        print("Fetching financial data...")
        
        total_tickers = len(self.idx_tickers)
        processed = 0
        successful = 0
        failed = 0
        
        # Process in batches to avoid overwhelming the API
        for i in range(0, total_tickers, batch_size):
            batch = self.idx_tickers[i:i+batch_size]
            
            for ticker in batch:
                try:
                    # Use yfinance to get stock data
                    stock = yf.Ticker(ticker)
                    
                    # Get financial statements
                    income_stmt = stock.income_stmt
                    balance_sheet = stock.balance_sheet
                    cash_flow = stock.cashflow
                    
                    # Get stock price history
                    hist = stock.history(period=f"{lookback_years}y")
                    
                    # Store in dictionary
                    self.stock_data[ticker] = {
                        'income_stmt': income_stmt,
                        'balance_sheet': balance_sheet,
                        'cash_flow': cash_flow,
                        'price_history': hist,
                        'info': stock.info
                    }
                    
                    successful += 1
                    print(f"Successfully fetched data for {ticker}")
                    
                except Exception as e:
                    failed += 1
                    print(f"Error fetching data for {ticker}: {e}")
                
                processed += 1
                # Show progress
                progress = (processed / total_tickers) * 100
                print(f"Progress: {processed}/{total_tickers} stocks processed ({progress:.1f}%) - Success: {successful}, Failed: {failed}")
                
                # Brief pause to avoid API rate limits
                time.sleep(0.5)
            
            # Longer pause between batches
            print(f"Completed batch {i//batch_size + 1}/{(total_tickers+batch_size-1)//batch_size}. Pausing briefly...")
            time.sleep(3)
        
        print(f"\nData fetching complete. Successfully retrieved data for {successful} out of {total_tickers} stocks.")
        return self.stock_data
    
    def calculate_metrics(self):
        """Calculate value investing metrics for the stocks"""
        print("Calculating value investing metrics...")
        
        metrics_df = pd.DataFrame(columns=[
            'Ticker', 'Company', 'Price', 'Market Cap (B IDR)', 
            'P/E', 'P/B', 'ROE (%)', 'Debt/Equity', 
            'Dividend Yield (%)', '5Y Revenue Growth (%)', 
            'Net Margin (%)', 'Free Cash Flow (B IDR)',
            'Buffett Score'
        ])
        
        for ticker, data in self.stock_data.items():
            try:
                info = data['info']
                
                # Extract metrics or use placeholder if not available
                company_name = info.get('longName', ticker)
                price = info.get('currentPrice', np.nan)
                market_cap = info.get('marketCap', np.nan) / 1e9  # Convert to billions
                pe_ratio = info.get('trailingPE', np.nan)
                pb_ratio = info.get('priceToBook', np.nan)
                roe = info.get('returnOnEquity', np.nan) * 100 if info.get('returnOnEquity') else np.nan
                debt_equity = info.get('debtToEquity', np.nan) / 100 if info.get('debtToEquity') else np.nan
                dividend_yield = info.get('dividendYield', np.nan) * 100 if info.get('dividendYield') else np.nan
                
                # Calculate 5-year revenue growth
                income_stmt = data['income_stmt']
                if not income_stmt.empty and 'Total Revenue' in income_stmt.index:
                    recent_revenue = income_stmt.loc['Total Revenue'][0]
                    if len(income_stmt.columns) >= 5:
                        old_revenue = income_stmt.loc['Total Revenue'][4]
                        revenue_growth = ((recent_revenue / old_revenue) ** (1/5) - 1) * 100
                    else:
                        revenue_growth = np.nan
                else:
                    revenue_growth = np.nan
                
                # Calculate net margin
                if not income_stmt.empty and 'Net Income' in income_stmt.index and 'Total Revenue' in income_stmt.index:
                    net_income = income_stmt.loc['Net Income'][0]
                    revenue = income_stmt.loc['Total Revenue'][0]
                    if revenue != 0:
                        net_margin = (net_income / revenue) * 100
                    else:
                        net_margin = np.nan
                else:
                    net_margin = np.nan
                
                # Calculate free cash flow
                cash_flow = data['cash_flow']
                if not cash_flow.empty and 'Free Cash Flow' in cash_flow.index:
                    fcf = cash_flow.loc['Free Cash Flow'][0] / 1e9  # Convert to billions
                else:
                    fcf = np.nan
                
                # Calculate Buffett Score (0-100)
                # This is a simplified version based on value investing principles
                buffett_score = 0
                
                # Low P/E ratio (below 15 is good)
                if not np.isnan(pe_ratio):
                    if pe_ratio < 10:
                        buffett_score += 15
                    elif pe_ratio < 15:
                        buffett_score += 10
                    elif pe_ratio < 20:
                        buffett_score += 5
                
                # Low P/B ratio (below 1.5 is good)
                if not np.isnan(pb_ratio):
                    if pb_ratio < 1:
                        buffett_score += 15
                    elif pb_ratio < 1.5:
                        buffett_score += 10
                    elif pb_ratio < 2:
                        buffett_score += 5
                
                # High ROE (above 15% is good)
                if not np.isnan(roe):
                    if roe > 20:
                        buffett_score += 15
                    elif roe > 15:
                        buffett_score += 10
                    elif roe > 10:
                        buffett_score += 5
                
                # Low Debt/Equity (below 0.5 is good)
                if not np.isnan(debt_equity):
                    if debt_equity < 0.3:
                        buffett_score += 15
                    elif debt_equity < 0.5:
                        buffett_score += 10
                    elif debt_equity < 0.7:
                        buffett_score += 5
                
                # Dividend Yield (above 2% is good)
                if not np.isnan(dividend_yield):
                    if dividend_yield > 4:
                        buffett_score += 10
                    elif dividend_yield > 2:
                        buffett_score += 5
                
                # Revenue Growth (above 10% annually is good)
                if not np.isnan(revenue_growth):
                    if revenue_growth > 15:
                        buffett_score += 15
                    elif revenue_growth > 10:
                        buffett_score += 10
                    elif revenue_growth > 5:
                        buffett_score += 5
                
                # Net Margin (above 10% is good)
                if not np.isnan(net_margin):
                    if net_margin > 20:
                        buffett_score += 15
                    elif net_margin > 15:
                        buffett_score += 10
                    elif net_margin > 10:
                        buffett_score += 5
                
                # Append to DataFrame
                metrics_df = pd.concat([metrics_df, pd.DataFrame([{
                    'Ticker': ticker,
                    'Company': company_name,
                    'Price': price,
                    'Market Cap (B IDR)': market_cap,
                    'P/E': pe_ratio,
                    'P/B': pb_ratio,
                    'ROE (%)': roe,
                    'Debt/Equity': debt_equity,
                    'Dividend Yield (%)': dividend_yield,
                    '5Y Revenue Growth (%)': revenue_growth,
                    'Net Margin (%)': net_margin,
                    'Free Cash Flow (B IDR)': fcf,
                    'Buffett Score': buffett_score
                }])], ignore_index=True)
                
            except Exception as e:
                print(f"Error calculating metrics for {ticker}: {e}")
        
        # Sort by Buffett Score
        metrics_df = metrics_df.sort_values('Buffett Score', ascending=False)
        
        return metrics_df
    
    def visualize_results(self, metrics_df):
        """Visualize the results of analysis with improved visualizations for large datasets"""
        # Create a figure with multiple subplots for comprehensive analysis
        fig = plt.figure(figsize=(18, 20))
        
        # 1. Top 20 stocks by Buffett Score
        ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)
        top_20 = metrics_df.head(20)
        bars = ax1.barh(top_20['Ticker'], top_20['Buffett Score'], color='lightgreen')
        ax1.set_title('Top 20 Indonesian Stocks by Value Investing (Buffett) Score', fontsize=14)
        ax1.set_xlabel('Score (0-100)', fontsize=12)
        ax1.set_ylabel('Stock', fontsize=12)
        ax1.grid(axis='x', linestyle='--', alpha=0.7)
        ax1.invert_yaxis()  # Display highest score at top
        
        # Add company names as annotations
        for i, bar in enumerate(bars):
            company_name = top_20['Company'].iloc[i]
            shortened_name = company_name[:20] + '...' if len(company_name) > 20 else company_name
            score = top_20['Buffett Score'].iloc[i]
            ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                    f"{shortened_name} ({score:.0f})", 
                    va='center', fontsize=8)
            
        # Highlight top 5 stocks
        for i in range(min(5, len(bars))):
            bars[i].set_color('darkgreen')
        
        # 2. P/E vs ROE scatter plot (only for stocks with valid data)
        ax2 = plt.subplot2grid((3, 2), (1, 0))
        valid_data = metrics_df.dropna(subset=['P/E', 'ROE (%)'])
        
        # Limit P/E to reasonable range for better visualization
        pe_filter = valid_data['P/E'] < 50  # Filter out extreme P/E values
        valid_data = valid_data[pe_filter]
        
        scatter = ax2.scatter(
            valid_data['P/E'], 
            valid_data['ROE (%)'],
            s=valid_data['Market Cap (B IDR)'].clip(upper=1000) / 20,  # Size based on market cap (capped)
            alpha=0.7,
            c=valid_data['Buffett Score'],  # Color based on Buffett score
            cmap='viridis'
        )
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax2)
        cbar.set_label('Buffett Score')
        
        # Add labels for top 10 stocks by Buffett score
        top_10_tickers = valid_data.nlargest(10, 'Buffett Score')
        for i, row in top_10_tickers.iterrows():
            ax2.annotate(row['Ticker'], 
                        (row['P/E'], row['ROE (%)']),
                        fontsize=8, fontweight='bold')
        
        ax2.set_title('P/E Ratio vs Return on Equity (ROE)')
        ax2.set_xlabel('P/E Ratio')
        ax2.set_ylabel('ROE (%)')
        ax2.grid(True, alpha=0.3)
        ax2.set_axisbelow(True)
        
        # Add threshold lines
        ax2.axhline(y=15, color='r', linestyle='--', alpha=0.5, label='ROE = 15%')
        ax2.axvline(x=15, color='r', linestyle='--', alpha=0.5, label='P/E = 15')
        ax2.legend(loc='upper right')
        
        # 3. Dividend Yield vs Debt/Equity
        ax3 = plt.subplot2grid((3, 2), (1, 1))
        valid_div_data = metrics_df.dropna(subset=['Dividend Yield (%)', 'Debt/Equity'])
        
        # Filter out extreme values for better visualization
        div_filter = (valid_div_data['Dividend Yield (%)'] < 15) & (valid_div_data['Debt/Equity'] < 3)
        valid_div_data = valid_div_data[div_filter]
        
        scatter2 = ax3.scatter(
            valid_div_data['Debt/Equity'],
            valid_div_data['Dividend Yield (%)'],
            s=valid_div_data['Market Cap (B IDR)'].clip(upper=1000) / 20,
            alpha=0.7,
            c=valid_div_data['Buffett Score'],
            cmap='viridis'
        )
        
        # Add labels for top dividend payers
        top_div_payers = valid_div_data.nlargest(10, 'Dividend Yield (%)')
        for i, row in top_div_payers.iterrows():
            ax3.annotate(row['Ticker'], 
                        (row['Debt/Equity'], row['Dividend Yield (%)']),
                        fontsize=8, fontweight='bold')
        
        ax3.set_title('Dividend Yield vs Debt/Equity Ratio')
        ax3.set_xlabel('Debt/Equity Ratio')
        ax3.set_ylabel('Dividend Yield (%)')
        ax3.grid(True, alpha=0.3)
        ax3.set_axisbelow(True)
        
        # Add threshold lines
        ax3.axhline(y=3, color='g', linestyle='--', alpha=0.5, label='Yield = 3%')
        ax3.axvline(x=0.5, color='r', linestyle='--', alpha=0.5, label='D/E = 0.5')
        ax3.legend(loc='upper right')
        
        # 4. Sector breakdown of top 50 stocks
        ax4 = plt.subplot2grid((3, 2), (2, 0))
        
        # Extract sector information if available
        top_50 = metrics_df.head(50)
        sectors = []
        for i, row in top_50.iterrows():
            # Try to extract sector from company name or use industry grouping based on ticker
            company = row['Company']
            ticker = row['Ticker']
            
            if 'Bank' in company:
                sectors.append('Banking')
            elif any(x in ticker for x in ['BBCA', 'BBRI', 'BMRI', 'BBNI', 'BNGA', 'BTPN']):
                sectors.append('Banking')
            elif any(x in ticker for x in ['TLKM', 'EXCL', 'ISAT']):
                sectors.append('Telecommunications')
            elif any(x in ticker for x in ['UNVR', 'ICBP', 'INDF', 'MYOR', 'KLBF']):
                sectors.append('Consumer Goods')
            elif any(x in ticker for x in ['HMSP', 'GGRM']):
                sectors.append('Tobacco')
            elif any(x in ticker for x in ['ASII', 'AUTO', 'SMSM']):
                sectors.append('Automotive')
            elif any(x in ticker for x in ['SMRA', 'LPKR', 'BSDE', 'PWON', 'CTRA']):
                sectors.append('Property')
            elif any(x in ticker for x in ['PTPP', 'WIKA', 'WSKT', 'ADHI']):
                sectors.append('Construction')
            elif any(x in ticker for x in ['ANTM', 'PTBA', 'INCO', 'MDKA', 'ADRO']):
                sectors.append('Mining')
            elif any(x in ticker for x in ['MEDC', 'ESSA', 'ELSA', 'PGAS']):
                sectors.append('Energy')
            elif any(x in ticker for x in ['AALI', 'LSIP', 'SIMP', 'SGRO']):
                sectors.append('Plantation')
            elif any(x in ticker for x in ['SMGR', 'INTP']):
                sectors.append('Cement')
            elif any(x in ticker for x in ['BUKA', 'GOTO', 'EMTK', 'MTDL']):
                sectors.append('Technology')
            elif any(x in ticker for x in ['MAPI', 'MPPA', 'ERAA', 'ACES', 'AMRT']):
                sectors.append('Retail')
            elif any(x in ticker for x in ['KAEF', 'MIKA', 'HEAL']):
                sectors.append('Healthcare')
            elif any(x in ticker for x in ['SCMA', 'MNCN']):
                sectors.append('Media')
            else:
                sectors.append('Others')
        
        # Create sector summary
        sector_summary = pd.Series(sectors).value_counts()
        ax4.pie(sector_summary, labels=sector_summary.index, autopct='%1.1f%%', 
               shadow=False, startangle=90, textprops={'fontsize': 8})
        ax4.axis('equal')
        ax4.set_title('Sector Distribution of Top 50 Value Stocks')
        
        # 5. Distribution of Buffett Scores
        ax5 = plt.subplot2grid((3, 2), (2, 1))
        ax5.hist(metrics_df['Buffett Score'].dropna(), bins=20, color='skyblue', edgecolor='black')
        ax5.set_title('Distribution of Buffett Scores')
        ax5.set_xlabel('Buffett Score')
        ax5.set_ylabel('Number of Stocks')
        ax5.grid(True, alpha=0.3)
        
        # Add key statistics as text
        stats_text = (
            f"Total Stocks Analyzed: {len(metrics_df)}\n"
            f"Avg. Buffett Score: {metrics_df['Buffett Score'].mean():.1f}\n"
            f"Median P/E: {metrics_df['P/E'].median():.1f}\n"
            f"Median P/B: {metrics_df['P/B'].median():.1f}\n"
            f"Median ROE: {metrics_df['ROE (%)'].median():.1f}%\n"
            f"Median Dividend Yield: {metrics_df['Dividend Yield (%)'].median():.1f}%"
        )
        ax5.text(0.95, 0.95, stats_text, transform=ax5.transAxes, 
                fontsize=10, va='top', ha='right', 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        plt.show()
        
        return fig

    def save_results(self, metrics_df, filename='indonesia_value_stocks.csv'):
        """Save the analysis results to a CSV file"""
        metrics_df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")


if __name__ == "__main__":
    main()