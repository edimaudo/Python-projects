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



