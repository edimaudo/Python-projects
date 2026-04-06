# Libraries
import numpy_financial as npf
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
    page_title = "Project 2 - Probabilistic Loan Pricing",
    layout = 'wide'
)

st.title('Financial Modeling using Python')

st.header("Project 2 - Probabilistic Loan Pricing")

st.subheader("The Problem")
with st.expander(" "):
    st.write("""
    You work for a bank who is considering loaning funds to a small manufacturing business. The business needs price-machine to buy machinery. 
    The business would like to borrow the funds for n-life, and at that time it will repay price machine in full. 
    Interest is paid annually at a rate of rinterest (in the final period, both price-machine and r-interest at the rate of rinterest will be paid). 
    As this is a small business, there is significant default risk, but that default risk decreases over time as the business matures. 
    The probability of default in the first year is p1-default, and then each year thereafter it is:
    pt-default = pt−1 (default) Decaydefault 
    Finally, the default probability is different in the final year, as it is the repayment year. The business has to
    pay a lot more in this period so there is a greater likelihood it can’t come up with the funds. In the final year, (at
    year n-life), the default probability is pn-default.
    When the business defaults, then the default covenants of the loan trigger bankruptcy for the borrower, and
    the borrower must pay as much as it can on the loan in the bankruptcy process. The bankruptcy process takes two
    years, and then once it is resolved, the lender will collect rrecovery% of pricemachine. For the year of default and
    the year after, the lender will not collect any cash flows, and then two years after default, the lender will collect
    rrecoverypricemachine. Note that this means the number of years of cash flows may be up to two years greater than
    the life of the loan.
    You are the commercial loan analyst trying to decide if this loan makes sense for the bank. You want to give the
    lending officer all the information she would need to negotiate a rate for this loan.
    Given the inputs, what is the expected IRR of the loan for a variety of interest rates on the loan? The lending
    officer would like you to evaluate rates in 5% increments from 30% to 40%.
    The lending officer is also worried that she may have estimated p1 default incorrectly. She is hoping for the answers
    to the above questions considering that pdefault 1 may vary. Evaluate the above questions for p
    default 1 = 0.1, 0.3 in addition to the base case of 0.2. Finally, the lending officer is unsure for how long she should extend
    """)

    st.subheader("Notes")
    st.write("""
    You may assume a maximum loan life of 20 years in your model, which would make up to 22 years of cash
    flows.
    • Probably the easiest approach to building this model will use internal randomness. Though it certainly is
    possible to build this model using only expected values, I think that is generally more difficult.
    • With the internal randomness approach, make sure you set the number of iterations to 1,000 per set of inputs
    to get a good estimate.
    • While you are testing things out, set it lower, such as 10 or 100, to have it run quicker, but beware that the
    lower your number of iterations, the less consistent the results will be.
    • Also beware that with 1,000 iterations as required for the final submission, it may take over an hour to run
    the model, so plan for that time.
    • You may choose to either submit a pure Python model, pure Excel model, or a combination of the two. If
    you use both, then the Python model should be what I ultimately run and extract results from. The Python
    model would be running the Excel model many times and extracting the results.
    • Upon reading the prior note, you may think to implement in pure Excel because of greater familiarity, but I
    think you will find meeting the objective of running the model repeatedly with three changing inputs quite
    difficult. You need to run your model 27,000 times in total with three inputs changing together.
    • Your answers may differ slightly from those in the Selected Solutions section. This is the nature of a random
    model. They should be very close with 1,000 iterations, though.
        """)

    st.subheader("The Model")
    st.write("""
    Inputs
    1. pricemachine: 1000000
    2. nlif e: 5
    3. pdefault1: 0.2
    4. Decaydefault: 0.9
    5. pdefaultn: 0.4
    6. rrecovery: 0.4
    """)

    st.subheader("Bonus Problem")
    st.write("""
    Especially good visualization of the original problem will earn part of the bonus.
    Further, produce the same outputs as the main problem, but instead of evaluating p
    default1 = 0.1, 0.3, consider pdefault1
    as being normally distributed with mean 0.2 and standard deviation 0.05.
    Also examine a single selected input case with different numbers of iterations, producing visualizations and
    summary statistics of the results with different numbers of iterations, to show how precise the expected IRR
    estimates are.
    """)

st.subheader("Model Simulation")

# 1. Input Sidebars/Columns
col1, col2 = st.columns(2)
with col1:
    price_machine = st.number_input("Machine Price", value=1000000)
    n_life = st.selectbox("Loan Life (Years)", [5, 10, 20], index=0)
    r_interest = st.slider("Interest Rate", 0.0, 1.0, 0.30, 0.05)
with col2:
    p1_default = st.selectbox("Initial Default Prob (p1)", [0.1, 0.2, 0.3], index=1)
    decay = st.number_input("Default Decay", value=0.9)
    pn_default = st.number_input("Final Year Default Prob (pn)", value=0.4)
    r_recovery = st.number_input("Recovery Rate", value=0.4)

iterations = st.number_input("Iterations (1000 recommended)", value=100, step=100)

if st.button("Run Simulation"):
    all_irrs = []
    
    for i in range(int(iterations)):
        # Cash flows start with the loan outflow
        cfs = [-price_machine]
        current_p = p1_default
        defaulted = False
        
        for year in range(1, n_life + 1):
            # Determine probability for THIS year
            prob = pn_default if year == n_life else current_p
            
            if np.random.rand() < prob:
                # DEFAULT logic: 2 years of $0, then recovery
                cfs.extend([0, 0])
                cfs.append(price_machine * r_recovery)
                defaulted = True
                break
            else:
                # NO DEFAULT: Pay interest (+ principal if final year)
                payment = price_machine * r_interest
                if year == n_life:
                    payment += price_machine
                cfs.append(payment)
                current_p *= decay # Decay for next year
        
        all_irrs.append(npf.irr(cfs))
    
    expected_irr = np.mean(all_irrs)
    
    # 2. Validation Output
    st.metric("Expected IRR", f"{expected_irr:.2%}")
    
    # Show distribution to validate randomness
    df_irrs = pd.DataFrame(all_irrs, columns=["IRR"])
    st.line_chart(df_irrs)