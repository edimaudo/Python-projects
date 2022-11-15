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


st.title('Financial Modeling using Python')

st.header("Project 1")

st.subheader("The Problem")
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