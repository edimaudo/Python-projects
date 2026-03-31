import streamlit as st
import pandas as pd
import numpy as np
import warnings
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.preprocessing import MinMaxScaler
from zerve import variable

APP_NAME = 'Crowdfunding Analytics'
warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

@st.cache_data
def get_clean_data():
    df = variable("load_clean_explore_data","df")  # df = pd.read_csv('PleaseFundThis.csv')
    df.columns = df.columns.str.strip()
    df['is_success'] = df['project_success'].astype(str).str.strip().str.upper() == 'TRUE'
    df['target'] = df['is_success'].astype(int)
    return df


@st.cache_data
def get_processed_data(df):
    df['date_launched'] = pd.to_datetime(df['date_launched'], dayfirst=True)
    df['week_name'] = df['date_launched'].dt.day_name()
    df['year'] = df['date_launched'].dt.year
    df['month'] = df['date_launched'].dt.month
    

    df['project_success'] = df['project_success'].replace({False: 0, True: 1, "FALSE": 0, "TRUE": 1})
    df['project_has_video'] = df['project_has_video'].replace({False: 0, True: 1, "FALSE": 0, "TRUE": 1})
    df['project_has_facebook_page'] = df['project_has_facebook_page'].replace({"No": 0, "Yes": 1})
    df['project_has_pledge_rewards'] = df['project_has_pledge_rewards'].replace({"No": 0, "Yes": 1})
    

    cat_cols = ['major_category', 'region', 'week_name']
    df_cat = pd.get_dummies(df[cat_cols])
    
    cts_cols = ['duration_days', 'goal_$', 
                #'amt_pledged_$'
                #, 'project_update_count', 
                #'number_of_pledgers', 
                #'comments_count', 
                'project_has_video', 
                'project_has_facebook_page', 'project_has_pledge_rewards', 'year', 'month']
    
    scaler = MinMaxScaler()
    df_cts = pd.DataFrame(scaler.fit_transform(df[cts_cols]), columns=cts_cols)
    
    X = pd.concat([df_cts, df_cat], axis=1)
    y = df['project_success'].astype(int)
    
    return X, y, scaler, cat_cols, df[cat_cols]

@st.cache_resource
def train_model(X, y):
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(X, y)
    return model


df = get_clean_data()
model_df = get_clean_data()
X, y, scaler, cat_names, original_cats = get_processed_data(model_df)
best_model = train_model(X, y)


st.title(APP_NAME)
section = st.radio("", ["Overview", "Region Insights", "City Insights", "Category Insights", "Success Prediction"], horizontal=True)

# --- Overview Section ---
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
        st.markdown("<h3 style='text-align: center; font-size: 16px;'>Top 10 Projects by Amount Pledged</h3>", unsafe_allow_html=True)
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
        min_cat = min_cat.sort_values('amt_pledged_$')
        fig = px.bar(min_cat, x='minor_category', y='amt_pledged_$', title="Minor Category by Amount Pledged",labels={'amt_pledged_$': 'Amount Pledged ($)','minor_category':"Minor Category"})
        fig.update_layout(title_font_size=16,title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        # Donut Chart
        df['success_label'] = df['is_success'].map({
            True: 'Success', 
            False: 'Failed',
            'TRUE': 'Success', 
            'FALSE': 'Failed'
        })
        fig_donut = px.pie(df, names='success_label',  hole=0.5, title="Project Outcome Distribution")
        fig_donut.update_layout(title_font_size=16,title_x=0.5,legend_title_text='Project Outcome')
        fig_donut.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_donut, use_container_width=True)

# --- Insights Sections---
# Sidebar Filtering
elif section in ["Region Insights", "City Insights", "Category Insights"]:
    if section == "Region Insights":
        region_options = sorted(df['region'].unique())
        sel = st.sidebar.multiselect("Region", region_options)
        f_df = df[df['region'].isin(sel)] if sel else df
    elif section == "City Insights":        
        city_options = sorted(df['city'].unique())
        sel = st.sidebar.multiselect("City", city_options)
        f_df = df[df['city'].isin(sel)] if sel else df
    else:
        major_options = sorted(df['major_category'].unique())
        maj = st.sidebar.multiselect("Major Category", major_options)
        if maj:
            min_opts = sorted(df[df['major_category'].isin(maj)]['minor_category'].unique())
        else:
            min_opts = sorted(df['minor_category'].unique())
            
        min_sel = st.sidebar.multiselect("Minor Category", min_opts)
        f_df = df.copy()
        if maj:
            f_df = f_df[f_df['major_category'].isin(maj)]
        if min_sel:
            f_df = f_df[f_df['minor_category'].isin(min_sel)]

    f_df = f_df.copy()
    f_df['Outcome'] = f_df['is_success'].map({True: 'Success', False: 'Failure'})
    color_map = {'Success': '#00CC96', 'Failure': '#EF553B'}

    t1, t2, t3, t4 = st.tabs(["Category and Markets", "Flow and Distribution", "Success Drivers & Indicators", "Performance Trends and Comparisons"])
    
    with t1:
        fig = px.bar(f_df.groupby('minor_category')['amt_pledged_$'].sum().reset_index(), 
                     x='minor_category', y='amt_pledged_$',
                     labels={'amt_pledged_$': 'Amount Pledged ($)','minor_category':"Minor Category"})
        #fig.update_layout(title_font_size=16, title_x=0.5,title='')
        st.plotly_chart(fig, use_container_width=True)

    with t2:
        fig_hist = px.histogram(
            f_df, 
            x='amt_pledged_$', 
            color='Outcome', 
            marginal="box",
            title='',
            color_discrete_map=color_map,
            labels={'amt_pledged_$': 'Amount Pledged ($)', 'Outcome': 'Project Outcome'},
            template='plotly_white'
        )
        #fig_hist.update_layout(title_font_size=16)
        st.plotly_chart(fig_hist, use_container_width=True)

    with t3:
        fig_scatter = px.scatter(
            f_df, 
            x='goal_$', 
            y='amt_pledged_$', 
            color='Outcome', 
            size='number_of_pledgers',
             title='',
            color_discrete_map=color_map,
            labels={
                'goal_$': 'Goal Amount ($)', 
                'amt_pledged_$': 'Amount Pledged ($)', 
                'Outcome': 'Project Outcome',
                'number_of_pledgers': 'Total Pledgers'
            },
            template='plotly_white'
        )
        #fig_scatter.update_layout(title_font_size=16, title_x=0.5)
        st.plotly_chart(fig_scatter, use_container_width=True)

    with t4:
        f_df['date_launched'] = pd.to_datetime(f_df['date_launched'], errors='coerce')
        f_df['Month'] = f_df['date_launched'].dt.month_name()
        f_df['success_numeric'] = f_df['is_success'].astype(int)
        
        seasonal_df = f_df.groupby('Month')['success_numeric'].mean().reset_index()
        seasonal_df['Success_Rate_Pct'] = seasonal_df['success_numeric'] * 100
        
        month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        
        fig_monthly_bar = px.bar(
            seasonal_df, 
            x='Month', 
            y='Success_Rate_Pct',
            #title='Seasonal Success: Which Months Win?',
            category_orders={'Month': month_order},
            color='Success_Rate_Pct',
            color_continuous_scale='Viridis',
            text_auto='.1f',
            template='plotly_white',
            labels={'Success_Rate_Pct': 'Success Rate (%)'}
        )

        fig_monthly_bar.update_layout(
            #title_x=0.5, 
            showlegend=False, 
            #title_font_size=16,
            xaxis_title="Month of Launch"
        )
        st.plotly_chart(fig_monthly_bar, use_container_width=True)

# --- Success Prediction  ---
elif section == "Success Prediction":
    st.header("Project Success Prediction")
    with st.expander("Enter Project Details", expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            in_goal = st.number_input("Goal Amount ($)", value=1000)
            #in_pledged = st.number_input("Expected Pledges ($)", value=500)
            #in_pledgers = st.number_input("Number of Pledgers", value=50)
            in_dur = st.slider("Project Duration (Days)", 1, 90, 30)
            in_pledge_rewards = st.selectbox("Pledge Rewards?", ["Yes", "No"])
        with c2:
            #in_updates = st.number_input("# of Project Updates", value=2)
            #in_comments = st.number_input("# of Comments", value=5)
            in_video = st.selectbox("Has Project Video?", ["Yes", "No"])
            in_facebook = st.selectbox("Has Facebook Page?", ["Yes", "No"])
            region_options = sorted(original_cats['region'].unique())
            in_reg = st.selectbox("Region", region_options)
        with c3:
            month_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] # Month mapping
            in_month_name = st.selectbox("Launch Month", month_options)
            in_month = month_options.index(in_month_name) + 1
            day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            in_day = st.selectbox("Launch Day of Week", day_options)
            major_options = sorted(original_cats['major_category'].unique())
            in_cat = st.selectbox("Category", major_options) #original_cats['major_category'].unique()


    if st.button("Generate Prediction"):
        input_row = pd.DataFrame(0, index=[0], columns=X.columns)
        cts_data = pd.DataFrame([{
            'duration_days': in_dur,
            'goal_$': in_goal,
            #'amt_pledged_$': in_pledged,
            #'project_update_count': in_updates,
            #'number_of_pledgers': in_pledgers,
            #'comments_count': in_comments,
            'project_has_video': 1 if in_video == "Yes" else 0,
            'project_has_facebook_page': 1 if in_facebook == "Yes" else 0,
            'project_has_pledge_rewards': 1 if in_pledge_rewards == "Yes" else 0,
            'year': 2012,
            'month': in_month
        }])
        
        scaled_cts = scaler.transform(cts_data)
        
        for i, col in enumerate(cts_data.columns):
            input_row[col] = scaled_cts[0][i]
        if f"major_category_{in_cat}" in input_row.columns:
            input_row[f"major_category_{in_cat}"] = 1
        if f"region_{in_reg}" in input_row.columns:
            input_row[f"region_{in_reg}"] = 1
        if f"week_name_{in_day}" in input_row.columns:
            input_row[f"week_name_{in_day}"] = 1

        pred = best_model.predict(input_row)
        prob = best_model.predict_proba(input_row)[0][1]
        
        if pred[0] == 1:
            st.success(f"Prediction: **SUCCESS** (Confidence: {prob:.2%})")
        else:
            st.error(f"Prediction: **FAILURE** (Confidence: {1-prob:.2%})")