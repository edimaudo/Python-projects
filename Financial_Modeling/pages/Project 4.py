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

