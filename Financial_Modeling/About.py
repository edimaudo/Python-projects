# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import warnings
import numpy as np
from datetime import datetime
import random
warnings.simplefilter(action='ignore', category=FutureWarning)
import math 
import re, string


st.set_page_config(
    page_title = "Financial Modeling Using Python",
    layout = 'wide'
)

st.title('Financial Modeling using Python')

st.header("About")
st.write("""
This application leverages Nick DeRobertis’ Financial Modeling [course](https://nickderobertis.github.io/fin-model-course/index.html).  The application will have different pages that focus on solving the projects associated with the [course](https://nickderobertis.github.io/fin-model-course/index.html).  The application will be built using streamlit.
""")