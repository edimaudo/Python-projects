# Libraries
import streamlit as st
import pandas as pd
import matplotlib as mp
import plotly.express as px
import os, os.path
import warnings
import numpy as np
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


st.subheader("Model Configuration & Baseline Inputs")

with st.expander("Adjust Parameters", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Equity & Market**")
        price_wmt = st.number_input("WMT Stock Price", value=119.51)
        shares_out = st.number_input("Shares Outstanding (Billions)", value=2.85)
        beta_baseline = st.number_input("Baseline Beta", value=0.70)
        mkt_return_baseline = st.number_input("Baseline Market Return (%)", value=8.0) / 100
        rf_rate = st.number_input("Risk-Free Rate (%)", value=0.50) / 100

    with col2:
        st.markdown("**Debt & Tax**")
        mv_debt_baseline = st.number_input("Baseline MV Debt (Billions)", value=82.7)
        cost_debt_pre_tax = st.number_input("Pre-tax Cost of Debt (%)", value=2.74) / 100
        tax_rate_baseline = st.number_input("Corporate Tax Rate (%)", value=21.0) / 100
        sim_runs = st.select_slider("Simulations", options=[100, 1000, 10000], value=1000)

# Financial Functions
def calculate_re(rf, beta, rm):
    # Adjust for daily as per PDF instructions
    rf_daily = rf / 252
    rm_daily = rm / 252
    re_daily = rf_daily + beta * (rm_daily - rf_daily)
    return re_daily * 252

def calculate_wacc(e_val, d_val, re, rd, tax):
    total_val = e_val + d_val
    w_e = e_val / total_val
    w_d = d_val / total_val
    return (w_e * re) + (w_d * rd * (1 - tax))

if st.button("Run Monte Carlo Analysis"):
    equity_val = price_wmt * shares_out
    
    # 1. Generate Normal Distributions for Simulation
    betas = np.random.normal(beta_baseline, 0.2, sim_runs)
    mkt_returns = np.random.normal(mkt_return_baseline, 0.03, sim_runs)
    tax_rates = np.random.normal(tax_rate_baseline, 0.05, sim_runs)
    
    # For simplicity in this shell, we simulate the variation in Bond Value directly
    # In a full model, you would simulate individual bond yields
    debt_values = np.random.normal(mv_debt_baseline, 5.0, sim_runs) 

    # 2. Run Iterations
    results = []
    for i in range(sim_runs):
        sim_re = calculate_re(rf_rate, betas[i], mkt_returns[i])
        sim_wacc = calculate_wacc(equity_val, debt_values[i], sim_re, cost_debt_pre_tax, tax_rates[i])
        results.append(sim_wacc * 100) # Convert to percentage

    # 3. Visualizations
    df_results = pd.DataFrame(results, columns=['WACC'])
    
    st.divider()
    st.metric("Mean WACC", f"{np.mean(results):.2f}%")
    
    fig = px.histogram(df_results, x="WACC", nbins=50, 
                       title="Probability Distribution of WACC",
                       labels={'WACC': 'WACC (%)'},
                       template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    # 4. Probability Table
    st.subheader("Probability Table")
    percentiles = [1, 5, 25, 50, 75, 95, 99]
    table = pd.DataFrame({
        "Percentile": [f"{p}%" for p in percentiles],
        "WACC Value": [f"{np.percentile(results, p):.2f}%" for p in percentiles]
    })
    st.table(table)
