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
    page_title = "Project 4 - Full DCF Valuation",
    layout = 'wide'
)

st.title('Financial Modeling using Python')

st.header("Project 4 - Full DCF Valuation")

st.subheader("The Problem")
with st.expander(" "):
    st.write("""
    The purpose of this exercise is to complete a full discounted cash flow valuation of a stock from end to end, complete
    with all of the additional analyses you learned throughout the course. You can pick any publicly traded stock for
    your valuation. You must find the data on your own and research the company’s operations. Ultimately the main
    output is your valuation of the stock, but you must also provide a written justification of why you believe this value
    to be correct. You must discuss and show how variable this estimate is, as well as what could have large effects on
    the valuation. You should also consider several realistic scenarios based on states of the economy, and how these
    scenarios affect the valuation.
    Some of the components of your project should include:

    • WACC estimation

    • FCF estimation and forecasting (must forecast financial statements, not only FCFs directly, though that can
    be an extra check)

    • Terminal value estimation using both perpetuity growth and various exit multiples

    • Monte carlo simulation

    • Sensitivity analysis

    • Scenario analysis

    • Visualization
        """)



# --- Logic for Loading and Cleaning Data ---
def load_and_process_data():
    # 1. Load Prices for Beta calculation
    wmt_prices = pd.read_csv("WMT Prices.xlsx - WMT.csv")
    sp_prices = pd.read_csv("SP500 Prices.xlsx - GSPC.csv")
    
    # Calculate Daily Returns
    wmt_prices['Returns'] = wmt_prices['Adj Close'].pct_change()
    sp_prices['Returns'] = sp_prices['Adj Close'].pct_change()
    
    # Merge and calculate Beta
    merged = pd.merge(wmt_prices[['Date', 'Returns']], sp_prices[['Date', 'Returns']], on='Date').dropna()
    beta = np.cov(merged['Returns_x'], merged['Returns_y'])[0, 1] / np.var(merged['Returns_y'])
    
    # 2. Load Debt Details (Skip 12 header rows as seen in inspection)
    debt_df = pd.read_csv("WMT Debt Details.xls - Capital Structure Details.csv", skiprows=12)
    
    def parse_coupon(val):
        if pd.isna(val) or val == 'NA': return 0.0274 # Use baseline pre-tax cost if missing
        val = str(val).replace('%', '')
        if '-' in val: # Handle ranges (midpoint)
            low, high = map(float, val.split('-'))
            return (low + high) / 2 / 100
        return float(val) / 100

    def excel_date_to_dt(serial):
        try: return pd.to_datetime('1899-12-30') + pd.to_timedelta(float(serial), 'D')
        except: return datetime(2025, 12, 31) # Fallback

    debt_df['Clean_Coupon'] = debt_df['Coupon/Base Rate'].apply(parse_coupon)
    debt_df['Clean_Maturity'] = debt_df['Maturity'].apply(excel_date_to_dt)
    
    return beta, debt_df, wmt_prices['Adj Close'].iloc[-1]

# --- Financial Logic & Simulation ---
def run_simulation(baseline_beta, debt_df, current_price, n_sims=10000):
    # Fixed Parameters from PDF
    shares_out = 2.85e9
    rf_annual = 0.005 
    rd_pretax = 0.0274
    settlement_date = datetime(2021, 6, 9)
    
    # Calculate Equity Value
    equity_mv = current_price * shares_out
    
    # Value Debt
    total_debt_mv = 0
    for _, row in debt_df.iterrows():
        years = (row['Clean_Maturity'] - settlement_date).days / 365.25
        if years <= 0: total_debt_mv += row['Principal Due (USD)']
        else:
            # PV of bond
            pv = npf.pv(rd_pretax, years, -row['Clean_Coupon']*row['Principal Due (USD)'], -row['Principal Due (USD)'])
            total_debt_mv += pv

    # Distributions for Monte Carlo
    sim_betas = np.random.normal(baseline_beta, 0.2, n_sims)
    sim_rm = np.random.normal(0.08, 0.03, n_sims)
    sim_tax = np.random.normal(0.21, 0.05, n_sims)
    
    # WACC Calculation
    wacc_results = []
    for i in range(n_sims):
        # CAPM using daily adjustment
        re_daily = (rf_annual/252) + sim_betas[i] * ((sim_rm[i]/252) - (rf_annual/252))
        re_annual = re_daily * 252
        
        # WACC Formula
        v = equity_mv + total_debt_mv
        wacc = (equity_mv/v * re_annual) + (total_debt_mv/v * rd_pretax * (1 - sim_tax[i]))
        wacc_results.append(wacc * 100)
        
    return wacc_results, total_debt_mv

# --- Streamlit UI Integration ---
if st.sidebar.button("Execute Model"):
    beta, debt_data, last_price = load_and_process_data()
    results, mv_debt = run_simulation(beta, debt_data, last_price)
    
    st.success("Simulation Complete!")
    col1, col2 = st.columns(2)
    col1.metric("Calculated Beta", f"{beta:.2f}")
    col2.metric("Market Value Debt", f"${mv_debt/1e9:.2f}B")
    
    fig = px.histogram(results, title="WACC Probability Distribution", labels={'value': 'WACC %'})
    st.plotly_chart(fig)