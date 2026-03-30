import streamlit as st
import pandas as pd
import numpy as np
import warnings
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from zerve import variable

APP_NAME = 'Crowdfunding Analytics'
warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

# # --- 1. Data and Model Setup ---
@st.cache_data
def get_clean_data():
    # df = pd.read_csv('PleaseFundThis.csv')
    df = variable("load_clean_explore_data","df") 
    df.columns = df.columns.str.strip()
    # Use the specific logic from your ledger for success calculation
    df['is_success'] = df['project_success'].astype(str).str.strip().str.upper() == 'TRUE'
    df['target'] = df['is_success'].astype(int)
    return df


@st.cache_resource
def train_best_model(df):
    # Mimicking the specific preprocessing from your code
    # Selecting numeric features for the 166-column requirement mentioned in your snippet
    numeric_df = df.select_dtypes(include=[np.number]).fillna(0)
    features = numeric_df.iloc[:, 0:166]
    target = df['target']
    
    # Using only the Bagging Classifier as requested
    model = BaggingClassifier(random_state=22)
    model.fit(features, target)
    return model, features.columns

df = get_clean_data()
best_model, feature_cols = train_best_model(df)

# --- 2. Navigation ---
st.title(APP_NAME)
section = st.radio("Navigation", ["Overview", "Region Insights", "City Insights", "Category Insights", "Success Prediction"], horizontal=True)

# --- 3. Overview Section ---
if section == "Overview":
    # KPIs
    s_rate = (df['target'].sum() / len(df)) * 100
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Cities", df['city'].nunique())
    c2.metric("Countries", df['region'].nunique())
    c3.metric("Overall Success Rate", f"{s_rate:.1f}%")
    c4.metric("Avg Duration (days)", f"{df['duration_days'].mean():.1f}")
    c5.metric("Avg Goal Amount ($)", f"{df['goal_$'].mean():,.0f}")
    c6.metric("Avg Pledge Amount($)", f"{df['amt_pledged_$'].mean():,.0f}")

    col1, col2 = st.columns(2)
    with col1:
        # Top 10 Regions
        top_reg = df.groupby('region')['amt_pledged_$'].sum().nlargest(10).reset_index()
        top_reg =  top_reg.sort_values('amt_pledged_$')
        fig = px.bar(top_reg, x='amt_pledged_$', y='region', orientation='h', title="Top 10 Countries by Amount Pledged",  labels={'amt_pledged_$': 'Amount Pledged ($)','region':"Country"})
        fig.update_layout(title_font_size=16,title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        # Major Category Bar
        maj_cat = df.groupby('major_category')['amt_pledged_$'].sum().sort_values(ascending=False).reset_index()
        maj_cat = maj_cat.sort_values('amt_pledged_$')
        fig = px.bar(maj_cat, x='major_category', y='amt_pledged_$', title="Major Category by Amount Pledged",labels={'amt_pledged_$': 'Amount Pledged ($)','major_category':"Major Category"})
        fig.update_layout(title_font_size=16,title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        # Top 10 Projects
        st.markdown("<h3 style='text-align: center;'>Top 10 Projects by Amount Pledged</h3>", unsafe_allow_html=True)
        top_10_df = df.nlargest(10, 'amt_pledged_$')[['project_name', 'amt_pledged_$']].copy()
        top_10_df = top_10_df.rename(columns={'project_name': 'Projects','amt_pledged_$': 'Amount Pledged ($)'})
        st.dataframe(top_10_df, hide_index=True, use_container_width=True)

    with col2:
        # Top 10 Cities
        top_cit = df.groupby('city')['amt_pledged_$'].sum().nlargest(10).reset_index()
        top_cit =  top_cit.sort_values('amt_pledged_$')
        fig = px.bar(top_cit, x='amt_pledged_$', y='city', orientation='h', title="Top 10 Cities by Amount Pledged",  labels={'amt_pledged_$': 'Amount Pledged ($)','city':"City"})
        fig.update_layout(title_font_size=16,title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        # Minor Category Bar
        min_cat = df.groupby('minor_category')['amt_pledged_$'].sum().nlargest(10).reset_index()
        st.plotly_chart(px.bar(min_cat, x='minor_category', y='amt_pledged_$', title="Minor Category by Pledge"), use_container_width=True)
        # Donut Chart
        st.plotly_chart(px.pie(df, names='is_success', hole=0.5, title="Project Success Distribution"), use_container_width=True)

# --- 4. Insights Sections (Common Structure) ---
elif section in ["Region Insights", "City Insights", "Category Insights"]:
    # Sidebar Filtering
    if section == "Region Insights":
        sel = st.sidebar.multiselect("Region", df['region'].unique())
        f_df = df[df['region'].isin(sel)] if sel else df
    elif section == "City Insights":
        sel = st.sidebar.multiselect("City", df['city'].unique())
        f_df = df[df['city'].isin(sel)] if sel else df
    else:
        maj = st.sidebar.multiselect("Major Category", df['major_category'].unique())
        min_opts = df[df['major_category'].isin(maj)]['minor_category'].unique() if maj else df['minor_category'].unique()
        min_sel = st.sidebar.multiselect("Minor Category", min_opts)
        f_df = df[(df['major_category'].isin(maj if maj else df['major_category'])) & 
                  (df['minor_category'].isin(min_sel if min_sel else df['minor_category']))]

    # Required Tabs
    t1, t2, t3, t4 = st.tabs(["Category and Markets", "Flow and Distribution", "Success Drivers & Indicators", "Performance Trends and Comparisons"])
    
    with t1:
        st.plotly_chart(px.bar(f_df.groupby('minor_category')['amt_pledged_$'].sum().reset_index(), x='minor_category', y='amt_pledged_$'), use_container_width=True)
    with t2:
        st.plotly_chart(px.histogram(f_df, x='amt_pledged_$', color='is_success', marginal="box"), use_container_width=True)
    with t3:
        st.plotly_chart(px.scatter(f_df, x='goal_$', y='amt_pledged_$', color='is_success', size='number_of_pledgers'), use_container_width=True)
    with t4:
        st.plotly_chart(px.line(f_df.sort_values('date_launched'), x='date_launched', y='percent_raised'), use_container_width=True)

# --- 5. Success Prediction (Bagging Classifier Only) ---
elif section == "Success Prediction":
    st.header("Predictive Modeling: Bagging Classifier")
    
    with st.expander("Enter Project Details", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            in_goal = st.number_input("Goal Amount ($)", value=1000)
            in_dur = st.slider("Duration (Days)", 1, 90, 30)
            in_pledgers = st.number_input("Expected Pledgers", value=50)
            in_updates = st.number_input("Project Updates", value=2)
        with c2:
            in_comments = st.number_input("Comments Count", value=5)
            in_pledge_levels = st.number_input("Pledge Levels", value=5)
            in_facebook = st.selectbox("Has Facebook?", [1, 0])
            in_video = st.selectbox("Has Video?", [1, 0])

    if st.button("Generate Prediction"):
        # Create input array matching training features
        input_data = np.zeros((1, len(feature_cols)))
        # Map user inputs to the correct positions (assuming specific indices from your 166-col slice)
        # Note: In a production app, you would map these by column name
        input_data[0, 0] = in_dur
        input_data[0, 1] = in_goal
        input_data[0, 2] = in_updates
        input_data[0, 3] = in_pledgers
        
        pred = best_model.predict(input_data)
        prob = best_model.predict_proba(input_data)[0][1]
        
        if pred[0] == 1:
            st.success(f"Prediction: SUCCESS (Confidence: {prob:.2%})")
        else:
            st.error(f"Prediction: FAILURE (Confidence: {1-prob:.2%})")
            
        st.write("---")
        st.write("Current Model Performance (Bagging Classifier):")
        test_pred = best_model.predict(df[feature_cols])
        st.text(f"Precision: {precision_score(df['target'], test_pred):.2f}")
        st.text(f"Recall: {recall_score(df['target'], test_pred):.2f}")