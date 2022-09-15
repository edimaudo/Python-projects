import streamlit as st
import pandas as pd
import base64
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pickle as pkl
import shap
import streamlit.components.v1 as components
import os, os.path



######################
# Load data
######################
path = os.path.dirname(__file__)
DATA_URL = path + "/loan.csv"

######################
# Load model
######################
model=pkl.load(open("model.p","rb"))

######################
# Title
######################
st.set_page_config(
    page_title="Loan Prediction App",
    page_icon="loan.png"
)
st.set_option('deprecation.showPyplotGlobalUse', False)
######################
# Main Page
######################
st.title("Loan Default Prediction")
st.subheader("Are you sure your loan applicant is surely going to pay the loan back?💸 "
                 "This machine learning app will help you to make a prediction to help you with your decision!")

col1, col2 = st.columns([1, 1])

with col1:
    st.image("loan.png")

with col2:
    st.write("""To borrow money, credit analysis is performed. Credit analysis involves the measure to investigate
the probability of the applicant to pay back the loan on time and predict its default/ failure to pay back.

These challenges get more complicated as the count of applications increases that are reviewed by loan officers.
Human approval requires extensive hour effort to review each application, however, the company will always seek
cost optimization and improve human productivity. This sometimes causes human error and bias, as it’s not practical
to digest a large number of applicants considering all the factors involved.""")

st.subheader("To predict default/ failure to pay back status, you need to follow the steps below:")
st.markdown("""
1. Enter/choose the parameters that best descibe your applicant on the left side bar;
2. Press the "Predict" button and wait for the result.

""")
st.subheader("Prediction results: ")
######################
# Sidebar 
######################
st.sidebar.title("Loan Applicant Information")
st.sidebar.image("ab.png", width=100)
st.sidebar.write("Please choose parameters that descibe the applicant")

# Input features
loan_amnt =st.sidebar.slider("Select the loan amount: ",min_value=1000, max_value=40000,step=500)
term = st.sidebar.radio("Select Loan term: ", ('36 months', '60 months'))
int_rate = st.sidebar.slider("Select the interest rate: ",min_value=0.05, max_value=1.00,step=0.05)
installment = st.sidebar.slider("Select the installment amount: ",min_value=10, max_value=400,step=50)
grade =st.sidebar.selectbox('Select grade: ', ("A","B","C","D","E","F","G"))
home_ownership = st.sidebar.selectbox("Select home ownership status: ",('OWN', 'MORTGAGE','RENT', 'OTHER', 'NONE'))
annual_inc =st.sidebar.slider("Select annual income: ", min_value=10000, max_value=200000,step=1000)
verification_status = st.sidebar.selectbox("Select verification status: ",('Verified', 'Source Verified', 'Not Verified'))

def preprocess(loan_amnt, term, int_rate, installment, grade, home_ownership, annual_inc, verification_status):
    # Pre-processing user input

    user_input_dict={'loan_amnt':[loan_amnt], 'term':[term],'int_rate':[int_rate],'installment':[installment],
    'grade':[grade],'home_ownership':[home_ownership],'annual_inc':[annual_inc],'verificiation_status':[verification_status]}
    user_input=pd.DataFrame(data=user_input_dict)

    cleaner_type = {"term": {"36 months": 1.0, "60 months": 2.0},
    "grade": {"A": 1.0, "B": 2.0, "C": 3.0, "D": 4.0, "E": 5.0,"F":6.0,"G":7.0},
    "home_ownership": {'NONE':1.0,'OTHER':2.0,'RENT':3.0,'MORTGAGE':4.0,'OWN':5},
    "verification_status": {'Not Verified':1.0,'Source Verified':2.0,'Verified':3.0}
    }
    

    user_input = user_input.replace(cleaner_type)

    return user_input

#user_input=preprocess
user_input=preprocess(loan_amnt, term, int_rate, installment, grade, home_ownership, annual_inc, verification_status)
btn_predict = st.sidebar.button("Predict")

######################
# Model
######################
if btn_predict:
    pred = model.predict_proba(user_input)[:, 1]
    if pred[0] < 0.78:
        st.error('Warning! The applicant has a high risk to not pay the loan back!')
    else:
        st.success('It is green! The aplicant has a high probability to pay the loan back!')
    
    #prepare test set for shap explainability
    loans = st.cache(pd.read_csv)("loan.csv")
    X = loans.drop(columns=['loan_amt','term','int_rate','installment','grade','home_ownership','annual_inc',
    'verification_status'])
    y = loans[['loan_status']]
    y_ravel = y.values.ravel()

    X_train, X_test, y_train, y_test = train_test_split(X, y_ravel, test_size=0.25, random_state=42, stratify=y)

    st.subheader('Result Interpretability - Applicant Level')
    shap.initjs()
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(user_input)
    fig = shap.plots.bar(shap_values[0])
    st.pyplot(fig)

    st.subheader('Model Interpretability - Overall')
    shap_values_ttl = explainer(X_test)
    fig_ttl = shap.plots.beeswarm(shap_values_ttl)
    st.pyplot(fig_ttl)
    st.write(""" In this chart blue and red mean the feature value, e.g. annual income blue is a smaller value e.g. 40K USD,
    and red is a higher value e.g. 100K USD. The width of the bars represents the number of observations on a certain feature value,
    for example with the annual_inc feature we can see that most of the applicants are within the lower-income or blue area. And on axis x negative SHAP
    values represent applicants that are likely to churn and the positive values on the right side represent applicants that are likely to pay the loan back.
    What we are learning from this chart is that features such as annual_inc and sub_grade are the most impactful features driving the outcome prediction.
    The higher the salary is, or the lower the subgrade is, the more likely the applicant to pay the loan back and vice versa, which makes total sense in our case.
    """)