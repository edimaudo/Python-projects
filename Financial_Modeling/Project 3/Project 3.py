# Libraries
import streamlit as st
import pandas as pd
import matplotlib as mp
import plotly.express as px
import os, os.path
import warnings
import numpy as np
import numpy_financial as npf
from datetime import datetime
import random
warnings.simplefilter(action='ignore', category=FutureWarning)
import math 

st.set_page_config(
    page_title = "Project 3 - Monte Carlo Cost of Capital",
    layout = 'wide'
)

st.title('Financial Modeling using Python')

st.header("Project 3 - Monte Carlo Cost of Capital")

st.subheader("The Problem")
with st.expander(" "):
    st.write("""
        You are an analyst at an investment fund. The fund is considering an investment in Walmart. As part of the
    decision-making process, your team is building a DCF model to value the stock. Another analyst is working on
    getting the free cash flows. Your job is to determine the cost of capital for Walmart.  Determine the WACC for Walmart. Ensure that you estimate the market value of debt by valuing the individual
    debt instruments. Once you have a baseline estimate, you want to figure out the variability of that estimate.
    Given the standard deviations in the Monte Carlo Inputs section, and assuming these variables all follow normal
    distributions, visualize the probability distribution of the WACC via a histogram and a probability table. Which
    of the variables has the greatest contribution to the WACC? Use at least 10,000 simulations.
        """)

    st.subheader("Notes")
    st.write("""
    • Be careful that the returns are daily. You will need to divide the risk free rate by 252 to get a daily rate.
    After you get an estimate from CAPM, you will need to multiply it by 252.
    • You can feel free to modify any of the input files to make them easier to load. But keep in mind that if you
    did this on the job, and you needed to keep updating the model, you would have to do this every time. If
    you cleaned it up with code then it would be automated. At the end I will show my model which automates
    the cleanup process.
    • If there is not a specific day associated with a debt maturity, only a year, assume it is December 31st.
    • If there is a range of coupons given, you can assume the midpoint of the range is the coupon.
    • If there is not enough information to calculate a bond price, or the bond already expired, just use the principal
    as the market price of the bond.
        """)


# --- HELPER FUNCTIONS FOR CLEANUP ---
def clean_coupon(coupon_val):
    """Handles midpoint for ranges like '3% - 4%' or strings like '3.50%'"""
    if isinstance(coupon_val, str) and '-' in coupon_val:
        parts = [float(x.strip().replace('%', '')) for x in coupon_val.split('-')]
        return sum(parts) / len(parts) / 100
    try:
        return float(str(coupon_val).replace('%', '')) / 100
    except:
        return 0.05 # Default fallback

def clean_date(date_val):
    """Appends Dec 31 if only year is provided"""
    str_date = str(date_val).strip()
    if len(str_date) == 4: # Just a year
        return pd.to_datetime(f"{str_date}-12-31")
    return pd.to_datetime(str_date)

# --- MAIN APP ---
st.title('Project 3: WMT Monte Carlo Cost of Capital')

if st.sidebar.button("Run Full Analysis"):
    try:
        # 1. LOAD DATA
        # Note: Filenames match the PDF requirements
        wmt_prices = pd.read_excel("WMT Prices.xlsx")
        sp_prices = pd.read_excel("SP500 Prices.xlsx")
        debt_df = pd.read_excel("WMT Debt Details.xls")
        inc_stmt = pd.read_excel("WMT Income Statement.xlsx")
        bal_sheet = pd.read_excel("WMT Balance Sheet.xlsx")

        # 2. CALCULATE BETA (CAPM)
        wmt_ret = wmt_prices['Adj Close'].pct_change().dropna()
        sp_ret = sp_prices['Adj Close'].pct_change().dropna()
        
        # Beta = Cov(WMT, SP) / Var(SP)
        matrix = np.cov(wmt_ret, sp_ret)
        beta_calc = matrix[0,1] / matrix[1,1]
        
        # 3. VALUATION OF DEBT (Individually)
        # Using baseline pre-tax cost of debt 2.74% for valuation
        r_d_baseline = 0.0274 
        today = datetime(2021, 6, 9) # Settlement date for the project
        
        total_mv_debt = 0
        for _, row in debt_df.iterrows():
            principal = row['Principal']
            coupon = clean_coupon(row['Coupon'])
            maturity = clean_date(row['Maturity'])
            
            years_to_maturity = (maturity - today).days / 365.25
            if years_to_maturity <= 0:
                total_mv_debt += principal # Already expired/due
            else:
                # Price = PV of Coupons + PV of Principal
                bond_pv = npf.pv(r_d_baseline, years_to_maturity, -coupon*principal, -principal)
                total_mv_debt += bond_pv

        # 4. EQUITY VALUE
        price_wmt = wmt_prices['Adj Close'].iloc[-1]
        shares = 2850000000 # Based on PDF data
        market_cap = price_wmt * shares

        # 5. MONTE CARLO SIMULATION (10,000 Runs)
        n_sims = 10000
        # Inputs defined in PDF: Beta (std 0.2), Mkt Ret (std 3%), Tax (std 5%)
        sim_betas = np.random.normal(beta_calc, 0.2, n_sims)
        sim_mkt_returns = np.random.normal(0.08, 0.03, n_sims)
        sim_taxes = np.random.normal(0.21, 0.05, n_sims)
        
        rf_daily = 0.005 / 252
        
        results = []
        for i in range(n_sims):
            # Cost of Equity
            re_daily = rf_daily + sim_betas[i] * ((sim_mkt_returns[i]/252) - rf_daily)
            re_annual = re_daily * 252
            
            # WACC
            total_val = market_cap + total_mv_debt
            w_e = market_cap / total_val
            w_d = total_mv_debt / total_val
            
            wacc = (w_e * re_annual) + (w_d * r_d_baseline * (1 - sim_taxes[i]))
            results.append(wacc)

        # 6. OUTPUTS
        st.header("Baseline Metrics")
        c1, c2, c3 = st.columns(3)
        c1.metric("Calculated Beta", round(beta_calc, 2))
        c2.metric("MV Debt (Billion)", f"${total_mv_debt/1e9:.2f}B")
        c3.metric("Baseline WACC", f"{np.mean(results)*100:.2f}%")

        # Histogram
        fig = px.histogram(results, nbins=50, title="Distribution of WACC Outcomes")
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error loading files: {e}. Ensure all Excel files are in the directory.")
