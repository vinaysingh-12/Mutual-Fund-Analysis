import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as plt_sns

# 1. Setup Environment
os.makedirs('visualizations', exist_ok=True)
db_path = 'bluestock_mf.db'

# Set visualization style
plt.style.use('seaborn-v0_8-whitegrid')
plt_sns.set_palette("muted")

def create_visualizations():
    print("Connecting to database...")
    conn = sqlite3.connect(db_path)

    # --- Chart 1: Top 5 Funds by AUM ---
    print("Generating: Top 5 Funds by AUM...")
    query1 = """
    SELECT scheme_name, aum_crore 
    FROM fact_performance 
    ORDER BY aum_crore DESC 
    LIMIT 5;
    """
    df1 = pd.read_sql(query1, conn)
    
    if not df1.empty:
        plt.figure(figsize=(10, 6))
        plt_sns.barplot(data=df1, x='aum_crore', y='scheme_name', palette='viridis')
        plt.title('Top 5 Mutual Funds by AUM (in Crores)', fontsize=14, pad=15)
        plt.xlabel('AUM (Crores)')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig('visualizations/01_top_5_funds_by_aum.png', dpi=300)
        plt.close()

    # --- Chart 2: Average NAV Trend for a Fund ---
    print("Generating: Average NAV Trend...")
    query2 = """
    SELECT strftime('%Y-%m', date) as month, AVG(nav) as avg_nav
    FROM fact_nav
    WHERE amfi_code = 119551
    GROUP BY month
    ORDER BY month;
    """
    df2 = pd.read_sql(query2, conn)
    
    if not df2.empty:
        plt.figure(figsize=(12, 5))
        plt.plot(df2['month'], df2['avg_nav'], marker='o', linestyle='-', color='#2c3e50', linewidth=2)
        plt.title('Monthly Average NAV Trend (SBI Bluechip Fund)', fontsize=14, pad=15)
        plt.xlabel('Month')
        plt.ylabel('Average NAV (INR)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('visualizations/02_nav_trend_sbi_bluechip.png', dpi=300)
        plt.close()

    # --- Chart 3: Transaction Volume by State ---
    print("Generating: Transaction Volume by State...")
    query3 = """
    SELECT state, SUM(amount_inr) / 100000 as total_amount_lakh
    FROM fact_transactions
    GROUP BY state
    ORDER BY total_amount_lakh DESC
    LIMIT 10;
    """
    df3 = pd.read_sql(query3, conn)
    
    if not df3.empty:
        plt.figure(figsize=(10, 6))
        plt_sns.barplot(data=df3, x='total_amount_lakh', y='state', palette='magma')
        plt.title('Top 10 States by Transaction Volume (in Lakhs)', fontsize=14, pad=15)
        plt.xlabel('Total Transaction Amount (Lakh INR)')
        plt.ylabel('State')
        plt.tight_layout()
        plt.savefig('visualizations/03_transactions_by_state.png', dpi=300)
        plt.close()

    # --- Chart 4: Payment Mode Preferences ---
    print("Generating: Payment Mode Preferences...")
    query4 = """
    SELECT payment_mode, COUNT(*) as usage_count
    FROM fact_transactions
    GROUP BY payment_mode
    ORDER BY usage_count DESC;
    """
    df4 = pd.read_sql(query4, conn)
    
    if not df4.empty:
        plt.figure(figsize=(8, 8))
        plt.pie(df4['usage_count'], labels=df4['payment_mode'], autopct='%1.1f%%', startangle=140, colors=plt_sns.color_palette('pastel'))
        plt.title('Preferred Payment Modes for Transactions', fontsize=14, pad=15)
        plt.tight_layout()
        plt.savefig('visualizations/04_payment_mode_preferences.png', dpi=300)
        plt.close()

    conn.close()
    print("\nSuccess! All charts have been saved to the 'visualizations/' folder.")

if __name__ == "__main__":
    create_visualizations()