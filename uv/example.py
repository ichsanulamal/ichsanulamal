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
        
        # IDX website often blocks scrapers, so this is a simplified approach
        # In a real implementation, consider using Indonesia's financial data APIs
        
        # For demo purposes, using some major Indonesian stocks
        # These are some of the largest stocks on IDX by market cap
        self.idx_tickers = [
            'BBCA.JK',  # Bank Central Asia
            'BBRI.JK',  # Bank Rakyat Indonesia
            'BMRI.JK',  # Bank Mandiri
            'TLKM.JK',  # Telkom Indonesia
            'ASII.JK',  # Astra International
            'UNVR.JK',  # Unilever Indonesia
            'HMSP.JK',  # HM Sampoerna
            'ICBP.JK',  # Indofood CBP
            'INDF.JK',  # Indofood Sukses Makmur
            'ANTM.JK',  # Aneka Tambang
        ]
        
        print(f"Found {len(self.idx_tickers)} Indonesian stocks for analysis.")
        return self.idx_tickers
    
    def fetch_financial_data(self, lookback_years=5):
        """Fetch financial data for Indonesia stocks"""
        print("Fetching financial data...")
        
        for ticker in self.idx_tickers:
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
                
                print(f"Successfully fetched data for {ticker}")
                time.sleep(1)  # To avoid hitting API limits
                
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
        
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
        """Visualize the results of analysis"""
        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
        
        # Plot Buffett Score
        ax1.barh(metrics_df['Ticker'], metrics_df['Buffett Score'], color='green')
        ax1.set_title('Value Investing (Buffett) Score for Indonesian Stocks')
        ax1.set_xlabel('Score (0-100)')
        ax1.set_ylabel('Stock')
        ax1.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Highlight top 3 stocks
        top_3 = metrics_df.head(3)
        for i, ticker in enumerate(top_3['Ticker']):
            ax1.get_children()[i].set_color('darkgreen')
        
        # Plot P/E vs ROE
        scatter = ax2.scatter(
            metrics_df['P/E'], 
            metrics_df['ROE (%)'],
            s=metrics_df['Market Cap (B IDR)'] / 50,  # Size based on market cap
            alpha=0.7,
            c=metrics_df['Buffett Score'],  # Color based on Buffett score
            cmap='viridis'
        )
        
        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax2)
        cbar.set_label('Buffett Score')
        
        # Add labels for each point
        for i, txt in enumerate(metrics_df['Ticker']):
            ax2.annotate(txt, (metrics_df['P/E'].iloc[i], metrics_df['ROE (%)'].iloc[i]),
                        fontsize=8)
        
        ax2.set_title('P/E Ratio vs Return on Equity (ROE)')
        ax2.set_xlabel('P/E Ratio')
        ax2.set_ylabel('ROE (%)')
        ax2.grid(True, alpha=0.3)
        ax2.set_axisbelow(True)
        
        # Add a horizontal line at ROE = 15% (Buffett's typical threshold)
        ax2.axhline(y=15, color='r', linestyle='--', alpha=0.5)
        # Add a vertical line at P/E = 15 (Buffett's typical threshold)
        ax2.axvline(x=15, color='r', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        plt.show()
        
        return fig

    def save_results(self, metrics_df, filename='indonesia_value_stocks.csv'):
        """Save the analysis results to a CSV file"""
        metrics_df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")

def main():
    print("Indonesian Value Investing Analysis")
    print("===================================")
    
    # Create investor instance
    investor = IndonesianValueInvestor()
    
    # Get list of IDX tickers
    investor.get_idx_tickers()
    
    # Add custom tickers if needed
    custom_tickers = input("Enter any additional Indonesian stocks to analyze (comma-separated, leave blank to skip): ")
    if custom_tickers.strip():
        additional_tickers = [ticker.strip() + ".JK" for ticker in custom_tickers.split(',')]
        investor.idx_tickers.extend(additional_tickers)
    
    # Fetch financial data
    investor.fetch_financial_data()
    
    # Calculate metrics
    metrics_df = investor.calculate_metrics()
    
    # Display top value stocks
    print("\nTop Indonesian Value Stocks:")
    print("==========================")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(metrics_df.head(5).to_string(index=False))
    
    # Visualize results
    fig = investor.visualize_results(metrics_df)
    
    # Save results
    investor.save_results(metrics_df)
    
    print("\nAnalysis complete! Review the visualizations and CSV output for detailed information.")

if __name__ == "__main__":
    main()