#================
# Telco. Customer Insights
#================

# Load libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os, os.path
import pandas as pd
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn import model_selection
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, OneHotEncoder
from sklearn.metrics import roc_curve, auc, recall_score, precision_score, f1_score, confusion_matrix, cohen_kappa_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import TimeSeriesSplit, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression

st.title('Telco. Customer Insights')

st.write("High level analysis of telco data")

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    data.dropna(inplace=True)
    data.drop('customerID', axis=1, inplace=True)
    return data

# Load data
DATA_URL = "customer_churn.csv"
df = load_data()

#====================
# Raw data
#====================
st.subheader("Raw Data")
with st.expander("Open to see more",expanded=False):
    st.dataframe(df)

#====================
# Data visualization
#====================
st.subheader("Visualization")
with st.expander("Open to see more",expanded=False):
    # Payment Method
    st.write("Payment Methods")
    df_payment_method = df[['PaymentMethod','TotalCharges']]
    df_payment_method_agg = df_payment_method.groupby('PaymentMethod').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_payment_method_agg.columns = ['Payment Methods','Total Charges']
    df_payment_method_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_payment_method_agg, x="Payment Methods", y="Total Charges")
    st.plotly_chart(output)

    #Contract
    st.write("Contracts")
    df_info = df[['Contract','TotalCharges']]
    df_agg = df_info.groupby('Contract').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_agg.columns = ['Contract','Total Charges']
    df_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_agg, x="Contract", y="Total Charges")
    st.plotly_chart(output)

    # Internet Service
    st.write("Internet Service")
    df_info = df[['InternetService','TotalCharges']]
    df_agg = df_info.groupby('InternetService').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_agg.columns = ['Internet Service','Total Charges']
    df_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_agg, x="Internet Service", y="Total Charges")
    st.plotly_chart(output)

    # Phone Service
    st.write("Phone Services")
    df_info = df[['PhoneService','TotalCharges']]
    df_agg = df_info.groupby('PhoneService').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_agg.columns = ['Phone Service','Total Charges']
    df_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_agg, x="Phone Service", y="Total Charges")
    st.plotly_chart(output)

    # Paperless
    st.write("Paperless Billing")
    df_info = df[['PaperlessBilling','TotalCharges']]
    df_agg = df_info.groupby('PaperlessBilling').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_agg.columns = ['Paperless Billing','Total Charges']
    df_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_agg, x="Paperless Billing", y="Total Charges")
    st.plotly_chart(output)

    # Gender
    st.write("Gender")
    df_info = df[['gender','TotalCharges']]
    df_agg = df_info.groupby('gender').agg(Total_Charges = ('TotalCharges', 'sum')).reset_index()
    df_agg.columns = ['Gender','Total Charges']
    df_agg.sort_values("Total Charges", ascending=True)
    output = px.bar(df_agg, x="Gender", y="Total Charges")
    st.plotly_chart(output)


#====================
# Churn prediction using ML
#====================

# ML Models
st.subheader("Churn Prediction")
with st.expander("Open to see more",expanded=False):
    clicked = st.button("Run ML Model")
    if clicked:
        # Drop first column
        df.drop('customerID', axis=1, inplace=True)
    

    # rescale all variables except the target variable
    # df_scale = df.loc[:, df.columns!='disease']
    # scaler = preprocessing.MinMaxScaler()
    # df_scale = scaler.fit_transform(df_scale)
    # df_scale = pd.DataFrame(df_scale)
    # df_scale.reset_index(drop=True, inplace=True)
    # # combine rescaled value
    # df['disease'].reset_index(drop=True, inplace=True)
    # df_1 = pd.concat([df_scale,df['disease']], axis=1)
    # df_1 = df.columns.values.tolist()
    # df.shape
    # #Let's now create our training and test data.
    # train,test = train_test_split(df,test_size=0.2,random_state=42)
    # print(train.shape, test.shape)
    # # Models
    # import warnings
    # warnings.simplefilter(action='ignore', category=FutureWarning)
    # model1=LogisticRegression(random_state=22,C=0.000000001,solver='liblinear',max_iter=200)
    # model2=GaussianNB()
    # model3=RandomForestClassifier(n_estimators=200,random_state=22)
    # model4=GradientBoostingClassifier(n_estimators=200)
    # model5=KNeighborsClassifier()
    # model6=DecisionTreeClassifier()
    # model7=LinearDiscriminantAnalysis()
    # model8=BaggingClassifier()
    # Ensembled_model=VotingClassifier(estimators=[('lr', model1), ('gn', model2), ('rf', model3),
    #                                              ('gb',model4),('kn',model5),('dt',model6),('lda',model7), ('bc',model8)], voting='hard')
    #                                              features=train.iloc[:,0:1094]
    # target = train['disease']
    # Name=[]
    # Accuracy=[]
    # f1=[]

    # # Accuracy
    # for model, label in zip([model1, model2, model3, model4,model5,model6,model7,model8,Ensembled_model], 
    #                         ['Logistic Regression','Naive Bayes','Random Forest', 'Gradient Boosting','KNN','Decision Tree','LDA', 'Bagging Classifier', 'Ensemble']):
    #     scores = cross_val_score(model, features, target, cv=5, scoring='accuracy')
    #     Accuracy.append(scores.mean())
    #     Name.append(model.__class__.__name__)
    #     print("Accuracy: %f for model %s" % (scores.mean(),label))

    # # F1 score - Metrics of Scoring
    # for model, label in zip([model1, model2, model3, model4,model5,model6,model7,model8,Ensembled_model], 
    #                         ['Logistic Regression','Naive Bayes','Random Forest', 'Gradient Boosting','KNN','Decision Tree','LDA', 'Bagging Classifier', 'Ensemble']):
    #     scores = cross_val_score(model, features, target, cv=5, scoring='f1_weighted')
    #     f1.append(scores.mean())
    #     Name.append(model.__class__.__name__)
    #     print("F1: %f for model %s" % (scores.mean(),label))

    # # Cohen’s kappa - Metrics of Scoring
    # warnings.simplefilter(action='ignore')
    # cohen = []
    # for model, label in zip([model1, model2, model3, model4,model5,model6,model7,model8,Ensembled_model], 
    #                         ['Logistic Regression','Naive Bayes','Random Forest', 'Gradient Boosting','KNN','Decision Tree','LDA', 'Bagging Classifier', 'Ensemble']):
    #   model.fit(X_train, y_train)
    #   y_pred = model.predict(X_test)
    #   cohen = cohen_kappa_score(Y_test, y_pred)
    #   Name.append(model.__class__.__name__)
    #   print("Cohen Kappa Score: %f for model %s" % (cohen,label))

    # # Prediction
    # X_test = test.drop('disease', axis=1)
    # Y_test = test[['disease']]

    # # Fairness Information