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
    page_title = "Project 1 - Machines Manufacturing Captal Budgeting Model",
    layout = 'wide'
)

st.title('Financial Modeling using Python')

st.header("Project 1 - Machines Manufacturing Captal Budgeting Model")

st.subheader("The Problem")
with st.expander(" "):
    st.write("""
    You work for a new startup that is trying to manufacture phones. You are tasked with building a model which will
    help determine how many machines to invest in and how much to spend on marketing. Each machine produces
    noutput phones per year. Each phone sells for $pphone and costs $cphone in variable costs to produce. After nlif e
    years, the machine can no longer produce output, but may be scrapped for $pscrap. The machine will not be
    replaced, so you may end up with zero total output before your model time period ends. Equity investment is
    limited, so in each year you can spend cmachine to either buy a machine or buy advertisements. In the first year you
    must buy a machine. Any other machine purchases must be made one after another (advertising can only begin
    after machine buying is done). Demand for your phones starts at d1. Each time you advertise, demand increases
    by gd%. The prevailing market interest rate is r.
    """)

    st.subheader("Notes")
    st.write("""
    • You may limit your model to 20 years and a maximum of 5 machines if it is helpful.
    • For simplicity, assume that cmachine is paid in every year, even after all machines have shut down.
    • Ensure that you can change the inputs and the outputs change as expected.
    • For simplicity, assume that fractional phones can be sold, you do not need to round the quantity transacted.
    """)

    st.subheader("The Model")
    st.write("""
    Inputs
    • noutput: Number of phones per machine per year
    • nmachines: Number of machines purchased
    • nlif e: Number of years for which the machine produces phones
    • pphone: Price per phone
    • pscrap: Scrap value of machine
    • cmachine: Price per machine or advertising year
    • cphone: Variable cost per phone
    • d1: Quantity of phones demanded in the first year
    • gd: Percentage growth in demand for each advertisement
    • r: Interest rate earned on investments

    Outputs
    • Cash flows in each year, up to 20 years
    • PV of cash flows, years 1 - 20
    """)

    st.subheader("Bonus Problem")
    st.write("""
    It is unrealistic to assume that price and demand are unrelated. To extend the model, we can introduce a relationship
    between price and demand, given by the following equation:
    d1 = dc − Epphone (1)
    • E: Price elasticity of demand
    • dc: Demand constant
    For elasticities and constants [(E = 500, dc = 900000), (E = 200, dc = 500000), (E = 100, dc = 300000)] (3 total
    cases), and taking the other model inputs in the Check your Work section, determine the optimal price for each
    elasticity, that is the price which maximizes the NPV.
    Notes
    • d1 is no longer an input, but an output.
    • This bonus requires optimization, which we have not yet covered in class.
    • In Excel, you can use Solver.
    • In Python, the scipy package provides optimization tools. You will probably want to use:
    - scipy.optimize.minimize_scalar
    - You will need to write a function which accepts price and returns NPV, with other model inputs fixed.
    * Depending on how you set this up, functools.partial may be helpful for this.
    - It will actually need to return negative NPV, as the optimizer only minimizes, but we want maximum
    NPV.
    - No answers to check your work are given for this bonus. The Check your Work section only applies to
    without the bonus.

    """)

st.subheader("Solution")
with st.expander(" "):
    # Inputs
    st.markdown("**Inputs**")
    phone_choice = st.slider('# of phones per machine per year', min_value=10000, max_value=10000000, value=100000, step=500)
    price_scrap_choice = st.slider('Scrap Value of machine', min_value=10000, max_value=1000000, value=50000, step=500)
    phone_price_choice = st.slider('Price Per Phone', min_value=100, max_value=5000, value=2000, step=50)
    cost_machine_adv_choice = st.slider('Price per machine or advertising year', min_value=10, max_value=1000, value=250, step=5)
    phone_variable_cost_choice = st.slider('Variable cost per phone', min_value=10000, max_value=5000000, value=1000000, step=5000)
    year_machine_choice = st.slider('# of years for which the machine produces phones', min_value=1, max_value=20, value=10, step=1)
    machine_purchase_choice = st.slider('# of machines purchased', min_value=1, max_value=100, value=5, step=1)
    phone_demand_choice = st.slider('Quantity of phones demanded in the first year', min_value=1000, max_value=1000000, value=100000, step=100)
    percent_growth_choice = st.slider('Percentage growth in demand for each advertisement', min_value=0.01, max_value=1.0, value=0.2, step=0.01)
    interest_choice = st.slider('Interest rate earned on investments', min_value=0.01, max_value=1.0, value=0.05, step=0.01)
    max_year_choice = st.slider('Max Year', min_value=1, max_value=50, value=20, step=1)
    elasticity_choice = st.slider('Elasticity', min_value=1, max_value=500, value=100, step=10)
    demand_choice = st.slider('Demand constant', min_value=100000, max_value=5000000, value=300000, step=1000)
    clicked = st.button("Run Model")
    if clicked:
        st.markdown("**Cash Flow**")
        cashflow = []

        st.markdown("**NPV**")
        npv_output = np.npv(interest_choice,[-100, 19, 49, 58, 200]) # change to cashflow
        npv_output = "{:.2f}".format(npv_output)
        st.write(npv_output)

    
 
 