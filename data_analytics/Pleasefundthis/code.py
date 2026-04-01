import pandas as pd
import numpy as np
import os, os.path
import matplotlib.pyplot as plt
import random
from math import sqrt

import warnings
warnings.filterwarnings("ignore")

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, OneHotEncoder  
from sklearn import model_selection
from sklearn.metrics import mean_squared_error
from sklearn.metrics import roc_curve, auc, recall_score, precision_score, f1_score, confusion_matrix, recall_score,accuracy_score, classification_report, average_precision_score

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import TimeSeriesSplit, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import MultinomialNB

## Load data
# ## Load data
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
#check data
print(df.head())
print(" ")
#summary
print(df.describe())
# Get column Names
print(" ")
print(df.columns.tolist())
# Remove unames columns
df = df.drop(['Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29'], axis=1) #drop unnamed columns
print(" ")
# Check data types
print(df.dtypes)
print(" ")
# # Remove rows with missing values
# df = df.dropna()
print(" ")
# Display basic statistics
print(df.info())
# Check for missing values
print(df.isnull().sum())
print(" ")
# Display missing values as percentage
print((df.isnull().sum() / len(df) * 100).round(2))
# # Date update
# df['date_launched'] = pd.to_datetime(df['date_launched'], dayfirst=True)
# # Use the correct method to get the day name
# df['week_name'] = df['date_launched'].dt.day_name()
# df['year'] = df['date_launched'].dt.year
# df['month_name'] = df['date_launched'].dt.month_name()


# Category and Markets section

##=====================
## Category and Markets
##=====================

####################
## Category Treemap
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
if df['amt_pledged_$'].dtype == 'object':
    df['amt_pledged_$'] = pd.to_numeric(df['amt_pledged_$'].str.replace(r'[$,]', '', regex=True), errors='coerce')

fig_treemap = px.treemap(
    df, 
    path=[px.Constant("All Projects"), 'major_category', 'minor_category'], 
    values='amt_pledged_$',
    color='amt_pledged_$',
    color_continuous_scale='Viridis',
    title='Funding Hierarchy: Major to Minor Category Breakdown',
    labels={'amt_pledged_$': 'Total Amount Pledged $'}
)

fig_treemap.update_traces(
    hovertemplate='<b>%{label}</b><br>Total Amount Pledged $: %{value:,.2f}<extra></extra>'
)

fig_treemap.update_layout(
    template='plotly_white', 
    margin=dict(l=10, r=10, t=40, b=10),
    title_font_size=20, 
    title_x=0.5, 
    height=500
)

fig_treemap.show()

####################
## Major Category Ranking
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
major_ranked = df.groupby('major_category')['amt_pledged_$'].sum().reset_index()
major_ranked = major_ranked.sort_values('amt_pledged_$', ascending=False)

fig_major = px.bar(
    major_ranked,
    x='amt_pledged_$',
    y='major_category',
    orientation='h',
    title='Pledge Amount by Major Category',
    labels={'amt_pledged_$': 'Pledged Amount ($)', 'major_category': 'Major Category'},
    color='amt_pledged_$',
    color_continuous_scale='viridis',
    text_auto='.2s' # Displays formatted values on bars
)

fig_major.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False, template='plotly_white', margin=dict(l=10, r=10, t=40, b=10),
        title_font_size=20, title_x=0.5, height=400)
fig_major.show()

####################
## Minor Category Ranking
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
minor_ranked = df.groupby('minor_category')['amt_pledged_$'].sum().reset_index()
minor_ranked = minor_ranked.sort_values('amt_pledged_$', ascending=False)

fig_minor = px.bar(
    minor_ranked,
    x='amt_pledged_$',
    y='minor_category',
    orientation='h',
    title='Pledge Amount by Minor Category',
    labels={'amt_pledged_$': 'Pledged Amount ($)', 'minor_category': 'Minor Category'},
    color='amt_pledged_$',
    color_continuous_scale='viridis',
    text_auto='.2s'
)

fig_minor.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False,template='plotly_white', margin=dict(l=10, r=10, t=40, b=10),
        title_font_size=20, title_x=0.5, height=400)
fig_minor.show()

####################
## Pledgers by Category 
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
if df['number_of_pledgers'].dtype == 'object':
    df['number_of_pledgers'] = pd.to_numeric(df['number_of_pledgers'].str.replace(',', ''), errors='coerce')

fig_treemap_pledge_count = px.treemap(
    df,
    path=[px.Constant("All Projects"), 'major_category', 'minor_category'], 
    values='number_of_pledgers',
    color='number_of_pledgers',
    color_continuous_scale='Viridis',
    title='Pledgers by Category'
)

fig_treemap_pledge_count.update_traces(
    textinfo="label+value",
    hovertemplate='<b>%{label}</b><br>Total Pledgers: %{value:,.0f}<extra></extra>'
)

fig_treemap_pledge_count.update_layout(
    margin=dict(t=80, l=10, r=10, b=10),
    title_x=0.5,
    title_font_size=20,
    coloraxis_colorbar=dict(title="Pledgers")
)

fig_treemap_pledge_count.show()

####################
## Goal $ distribution by major category 
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
df['goal_$'] = pd.to_numeric(df['goal_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')

# (Log Scale)
df['log_goal'] = np.log10(df['goal_$'].replace(0, 1))
categories = sorted(df['major_category'].unique())
colors = px.colors.sequential.Viridis

fig_ridge = go.Figure()

for i, cat in enumerate(categories):
    df_cat = df[df['major_category'] == cat]
    
    color_idx = i % len(colors)
    
    fig_ridge.add_trace(go.Violin(
        x=df_cat['log_goal'],
        line_color='black',       # Darker lines for contrast on white background
        line_width=1,
        fillcolor=colors[color_idx], 
        name=cat,
        orientation='h',
        side='positive', 
        width=4,                 # Increased width to ensure nice overlapping
        points=False
    ))


fig_ridge.update_layout(
    title='The "Mountain Range" of Goal Distributions',
    title_x=0.5,
    xaxis_title="Funding Goal Amount ($)",
    yaxis_title="Major Category",
    template='plotly_white',   
    showlegend=False,
    height=800,
    violingap=0, 
    violingroupgap=0
)


fig_ridge.update_xaxes(
    tickvals=[1, 2, 3, 4, 5, 6],
    ticktext=['$10', '$100', '$1k', '$10k', '$100k', '$1M'],
    gridcolor='lightgrey',     
    zerolinecolor='grey'
)

fig_ridge.show()

####################
## Goal $ Histogram 
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
df_filtered = df[(df['goal_$'] > 0) & (df['goal_$'] <= 100000)].copy()

fig_anchors = px.histogram(
    df_filtered, 
    x="goal_$", 
    nbins=500, # High bin count is CRITICAL to see the narrow spikes
    title='Funding Goal Target Amount Distribution',
    labels={'goal_$': 'Funding Goal ($)'},
    template='plotly_white',
    color_discrete_sequence=['#636EFA']
)


fig_anchors.update_layout(
    title_x=0.5,
    xaxis_title="Funding Goal Amount ($)",
    yaxis_title="Number of Projects",
    bargap=0.1,
    xaxis=dict(
        tickvals=[0, 1000, 5000, 10000, 20000, 25000, 50000, 75000, 100000],
        tickformat='$,.0f',
        range=[0, 100000]
    )
)


fig_anchors.add_annotation(x=10000, yref='paper', y=0.9, text="The $10k Peak", showarrow=True, arrowhead=1)
fig_anchors.add_annotation(x=5000, yref='paper', y=0.7, text="$5k Peak", showarrow=True, arrowhead=1)

fig_anchors.show()

####################
## Word cloud 
####################
from collections import Counter
import re
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
successful_titles = df[df['project_success'] == True]['project_name'].astype(str).str.lower()
# Define common "Stopwords" to filter out (the, and, for, etc.)
stopwords = {'the', 'and', 'for', 'your', 'with', 'from', 'this', 'that', 'project', 'new', 'help', 'make'}

all_words = []
for title in successful_titles:
    # Remove special characters and split into words
    words = re.findall(r'\w+', title)
    all_words.extend([w for w in words if w not in stopwords and len(w) > 2])
word_counts = Counter(all_words).most_common(25)
df_words = pd.DataFrame(word_counts, columns=['Keyword', 'Frequency'])
fig_keywords = px.bar(
    df_words, 
    x='Frequency', 
    y='Keyword', 
    orientation='h',
    title='Keywords of Success: Top Terms in Funded Project Titles',
    color='Frequency',
    color_continuous_scale='Viridis',
    template='plotly_white'
)

fig_keywords.update_layout(
    yaxis={'categoryorder':'total ascending'}, 
    title_x=0.5,
    xaxis_title="Keyword Count",
    height=700
)



fig_keywords.show()

####################
## City Success
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
df['city'] = df['city'].astype(str).str.strip().str.title()
df['is_success'] = pd.to_numeric(df['project_success'], errors='coerce').fillna(0).astype(bool)
if df['is_success'].sum() == 0:
    df['is_success'] = df['project_success'].astype(str).str.strip().str.upper() == 'TRUE'

# Calculate metrics
city_stats = df.groupby('city')['is_success'].agg(['sum', 'count']).reset_index()
city_stats.columns = ['City', 'Successes', 'Total_Outcomes']
city_stats['Success Rate'] = (city_stats['Successes'] / city_stats['Total_Outcomes']) * 100
top_cities = city_stats[city_stats['Total_Outcomes'] >= 10].sort_values('Success Rate', ascending=False)

fig_geo = px.bar(
    top_cities.head(20), 
    x='Success Rate',      # Move numeric value to x
    y='City',              # Move category to y
    color='Success Rate',
    orientation='h',       # Explicitly set horizontal orientation
    text_auto='.1f',
    title='<b>Cities by Success Rate</b>',
    labels={'Success Rate': 'Success Rate (%)', 'City': 'Location'},
    color_continuous_scale='viridis',
    template='plotly_white'
)

fig_geo.update_layout(
    title_x=0.5,
    yaxis={'categoryorder':'total ascending'} # Keeps the highest rate at the top
)

fig_geo.show()

####################
## Creator personas
####################
df = pd.read_csv('PleaseFundThis.csv')
# # Clean column names immediately 
df.columns = df.columns.str.strip()
# Clean Numeric Data
df['avg_amt$_per_pledger'] = pd.to_numeric(df['avg_amt$_per_pledger'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
df['number_of_pledgers'] = pd.to_numeric(df['number_of_pledgers'], errors='coerce')

df = df.dropna(subset=['avg_amt$_per_pledger', 'number_of_pledgers'])

# Thresholds (Medians)
x_mid = df['number_of_pledgers'].median()
y_mid = df['avg_amt$_per_pledger'].median()

# Numeric Quadrant Assignment
def assign_num(row):
    if row['avg_amt$_per_pledger'] >= y_mid and row['number_of_pledgers'] >= x_mid: return 1
    if row['avg_amt$_per_pledger'] >= y_mid and row['number_of_pledgers'] < x_mid:  return 2
    if row['avg_amt$_per_pledger'] < y_mid and row['number_of_pledgers'] >= x_mid:  return 3
    return 4

df['Quad_Num'] = df.apply(assign_num, axis=1)

fig_menu = px.scatter(
    df,
    x='number_of_pledgers',
    y='avg_amt$_per_pledger',
    color='Quad_Num',
    log_x=True, log_y=True,
    hover_data=['project_name'],
    title='<b>Creator Persona</b> Value vs. Volume',
    labels={'number_of_pledgers': 'Backer Volume', 'avg_amt$_per_pledger': 'Avg Pledge ($)'},
    template='plotly_white',
    color_continuous_scale=[(0, '#00CC96'), (0.33, '#636EFA'), (0.66, '#AB63FA'), (1, '#EF553B')]
)

fig_menu.add_vline(x=x_mid, line_width=3, line_color="RoyalBlue", opacity=1)
fig_menu.add_hline(y=y_mid, line_width=3, line_color="RoyalBlue", opacity=1)

fig_menu.update_layout(
    annotations=[
        dict(x=0.95, y=0.95, xref="paper", yref="paper", text="<b>STARS</b><br>High Value / High Volume", showarrow=False, font=dict(color="#00CC96", size=14)),
        dict(x=0.05, y=0.95, xref="paper", yref="paper", text="<b>BOUTIQUES</b><br>High Value / Low Volume", showarrow=False, font=dict(color="#636EFA", size=14)),
        dict(x=0.95, y=0.05, xref="paper", yref="paper", text="<b>PLOWHORSES</b><br>Low Value / High Volume", showarrow=False, font=dict(color="#AB63FA", size=14)),
        dict(x=0.05, y=0.05, xref="paper", yref="paper", text="<b>STRUGGLES</b><br>Low Value / Low Volume", showarrow=False, font=dict(color="#EF553B", size=14))
    ]
)

fig_menu.update_layout(coloraxis_showscale=False, title_x=0.5, height=700)
fig_menu.show()
"""
By using Average Pledge (Price) and Number of Pledgers (Popularity), you are showing the group exactly where the "profitability" lies.
Plowhorses (Bottom Right) are popular but cheap. They need to raise their "menu prices" (add higher reward tiers).
Boutiques (Top Left) are expensive but niche. They need better "marketing" (more backers) to become Stars.
"""

# Performance and Trends Section
##=====================
# Performance Trends and Comparisons
##=====================

####################
## Trend over time Month
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['date_launched'] = pd.to_datetime(df['date_launched'], errors='coerce')
df['Month'] = df['date_launched'].dt.month_name()
df['success_numeric'] = df['project_success'].astype(int)

seasonal_df = df.groupby('Month')['success_numeric'].mean().reset_index()
seasonal_df['Success_Rate_Pct'] = seasonal_df['success_numeric'] * 100

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

fig_monthly_bar = px.bar(
    seasonal_df, 
    x='Month', 
    y='Success_Rate_Pct',
    title='Seasonal Success: Which Months Win?',
    category_orders={'Month': month_order},
    color='Success_Rate_Pct',  # Colors bars by performance
    text_auto='.1f',           # Shows the % on top of the bars
    template='plotly_white',
    labels={'Success_Rate_Pct': 'Success Rate (%)'}
)

fig_monthly_bar.update_layout(title_x=0.5, showlegend=False,title_font_size=20,template='plotly_white')
fig_monthly_bar.show()

####################
## Launch window day of week
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['Day_of_Week'] = df['date_launched'].dt.day_name()
day_df = df.groupby('Day_of_Week')['success_numeric'].mean().reset_index()
day_df['Success_Rate_Pct'] = day_df['success_numeric'] * 100
week_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fig_daily = px.bar(
    day_df, 
    x='Day_of_Week', 
    y='Success_Rate_Pct',
    title='Success Rate by Day of Week',
    category_orders={'Day_of_Week': week_order},
    color='Success_Rate_Pct',
    text_auto='.1f',
    template='plotly_white',
    labels={'Success_Rate_Pct': 'Success Rate (%)', 'Day_of_Week': 'Day of Launch'}
)
fig_daily.update_layout(
    title_font_size=20,
    title_x=0.5,
    showlegend=False,
    yaxis_range=[0, max(day_df['Success_Rate_Pct']) + 10]
)

fig_daily.show()

####################
## Comparison between goal $ and amount pledged
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean currency columns
for col in ['goal_$', 'amt_pledged_$']:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')

# We use MEDIAN to find the 'typical' experience for each category
df_cat = df.groupby('major_category').agg({
    'goal_$': 'median',
    'amt_pledged_$': 'median'
}).reset_index()

# Sort by Pledged amount for a cleaner "ladder" visual
df_cat = df_cat.sort_values('amt_pledged_$')

fig_cat_dumbbell = go.Figure()

for i, row in df_cat.iterrows():
    fig_cat_dumbbell.add_trace(go.Scatter(
        x=[row['goal_$'], row['amt_pledged_$']],
        y=[row['major_category'], row['major_category']],
        mode='lines',
        line=dict(color='lightgrey', width=4),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add the "Median Goal" dots (Red)
fig_cat_dumbbell.add_trace(go.Scatter(
    x=df_cat['goal_$'],
    y=df_cat['major_category'],
    mode='markers',
    name='Median Goal',
    marker=dict(color='#EF553B', size=14),
    hovertemplate="Typical Goal: $%{x:,.0f}<extra></extra>"
))

# Add the "Median Pledged" dots (Green)
fig_cat_dumbbell.add_trace(go.Scatter(
    x=df_cat['amt_pledged_$'],
    y=df_cat['major_category'],
    mode='markers',
    name='Median Pledged',
    marker=dict(color='#00CC96', size=14),
    hovertemplate="Typical Pledged: $%{x:,.0f}<extra></extra>"
))

fig_cat_dumbbell.update_layout(
    title='"Funding Gap" by Category',
    xaxis_title='Amount ($)', # - Log Scale'
    yaxis_title=None,
    title_x=0.5,
    template='plotly_white',
      title_font_size=20,
    xaxis_type='log',
    height=700,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Set the log-scale ticks
fig_cat_dumbbell.update_xaxes(
    tickvals=[100, 1000, 10000, 100000],
    ticktext=['$100', '$1k', '$10k', '$100k']
)

fig_cat_dumbbell.show()

####################
## analyze top 20 projects to compare overfunding
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Calculate the 'overfunding' amount and select Top 20 for readability
df['overfunding_gap'] = df['amt_pledged_$'] - df['goal_$']
top_20 = df.sort_values(by='overfunding_gap', ascending=False).head(20).copy()

# 2. Build the Figure
fig_dumbbell = go.Figure()

# Loop through each project to draw the "bar" part of the dumbbell
for i, row in top_20.iterrows():
    fig_dumbbell.add_shape(
        type='line',
        x0=row['goal_$'], y0=row['project_name'],
        x1=row['amt_pledged_$'], y1=row['project_name'],
        line=dict(color='lightgrey', width=3)
    )

# 3. Add the "Goal" dots (Red)
fig_dumbbell.add_trace(go.Scatter(
    x=top_20['goal_$'],
    y=top_20['project_name'],
    mode='markers',
    name='Goal',
    marker=dict(color='#EF553B', size=12, symbol='circle'),
    hovertemplate="<b>%{y}</b><br>Goal: $%{x:,.0f}<extra></extra>"
))

# 4. Add the "Pledged" dots (Green)
fig_dumbbell.add_trace(go.Scatter(
    x=top_20['amt_pledged_$'],
    y=top_20['project_name'],
    mode='markers',
    name='Pledged Amount',
    marker=dict(color='#00CC96', size=12, symbol='circle'),
    hovertemplate="<b>%{y}</b><br>Pledged: $%{x:,.0f}<extra></extra>"
))


fig_dumbbell.update_layout(
    title='Magnitude of Overfunding: Top 20 Most Successful Projects',
    title_x=0.5,
    xaxis_title='Funding Amount ($)', ## log scale
    yaxis_title=None,
    template='plotly_white',
    xaxis_type='log', # Log scale allows us to see different orders of magnitude
    height=800,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Optional: Add clear log-scale ticks
fig_dumbbell.update_xaxes(
    tickvals=[10, 100, 1000, 10000, 100000, 1000000],
    ticktext=['$10', '$100', '$1k', '$10k', '$100k', '$1M']
)

fig_dumbbell.show()


# Flow and Distribution Section

##=====================
## Flow and Distribution
##=====================

####################
## Sankey chart major category 
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
top_minors = df['minor_category'].value_counts().nlargest(30).index
df_filtered = df[df['minor_category'].isin(top_minors)].copy()
# Map outcomes to strings
df_filtered['outcome'] = df_filtered['project_success'].map({True: 'Successful', False: 'Failed'})
# Create Node List and Mapping
majors = sorted(df_filtered['major_category'].unique().tolist())
minors = sorted(df_filtered['minor_category'].unique().tolist())
outcomes = ['Successful', 'Failed']
label_list = majors + minors + outcomes
label_map = {label: i for i, label in enumerate(label_list)}

source_list = []
target_list = []
value_list = []
link_colors = []

# --- Layer 1: Major -> Minor ---
flow1 = df_filtered.groupby(['major_category', 'minor_category']).size().reset_index(name='count')
for _, row in flow1.iterrows():
    source_list.append(label_map[row['major_category']])
    target_list.append(label_map[row['minor_category']])
    value_list.append(row['count'])
    link_colors.append("rgba(200, 200, 200, 0.3)") # Neutral grey for the middle

# --- Layer 2: Minor -> Outcome ---
flow2 = df_filtered.groupby(['minor_category', 'outcome']).size().reset_index(name='count')
for _, row in flow2.iterrows():
    source_list.append(label_map[row['minor_category']])
    target_list.append(label_map[row['outcome']])
    value_list.append(row['count'])
    # Color the final path: Green for Success, Red for Failure
    if row['outcome'] == 'Successful':
        link_colors.append("rgba(0, 204, 150, 0.5)")
    else:
        link_colors.append("rgba(239, 85, 59, 0.5)")

fig_sankey = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 30,         # Increased padding makes nodes easier to click/hover
      thickness = 15,
      line = dict(color = "white", width = 2),
      label = label_list,
      color = "#333333" # Dark nodes for a professional "light mode" look
    ),
    link = dict(
      source = source_list,
      target = target_list,
      value = value_list,
      color = link_colors
    )
)])

fig_sankey.update_layout(
    title_text="<b>Project Flow: From Category to Success</b>",
    title_x=0.5,
    font=dict(size=12, color="black"),
    height=700,
    margin=dict(l=20, r=20, t=60, b=20), # Tight margins to maximize use of space
    template='plotly_white'
)

fig_sankey.show()

####################
## Parallel Categories Diagram
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df_plot = df.copy()

# Ensure success is an integer (1 for True, 0 for False) for the color scale
df_plot['Outcome_Int'] = df_plot['project_success'].astype(str).str.strip().str.upper() == 'TRUE'
df_plot['Outcome_Int'] = df_plot['Outcome_Int'].astype(int)

# Rename the columns to match your 'dimensions' list exactly
df_plot = df_plot.rename(columns={
    'project_has_video': 'Video?',
    'project_has_facebook_page': 'FB Page?',
    'project_success': 'Outcome'
})

# 2. Build the Parallel Categories Chart
fig_parallel = px.parallel_categories(
    df_plot, 
    dimensions=['Video?', 'FB Page?', 'Outcome'],
    color='Outcome_Int', # Numeric column for the color scale
    color_continuous_scale=['#EF553B', '#00CC96'], # Red (0) to Green (1)
    title='Multi-Factor Success Paths: Video & Facebook Influence',
    labels={
        'Video?': 'Video Presence', 
        'FB Page?': 'Facebook Presence', 
        'Outcome': 'Project Outcome'
    },
    template='plotly_white'
)

fig_parallel.update_layout(
    title_x=0.5,
    margin=dict(l=100, r=100, t=100, b=100),
    coloraxis_showscale=False, # Hides the 0-1 bar on the right
    height=600
)

fig_parallel.show()

####################
## Whales vs the crowd
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
def get_quadrant(row):
    avg_pledge = row['amt_pledged_$'] / max(1, row['number_of_pledgers'])
    high_backers = row['number_of_pledgers'] > 500
    high_value = avg_pledge > 100
    
    if high_backers and high_value:
        return "The Unicorns (High Volume & High Value)"
    if high_backers and not high_value:
        return "The Crowd (Mass Appeal, Low Cost)"
    if not high_backers and high_value:
        return "The Whales (Boutique, High Cost)"
    return "The Baseline (Small Scale)"

df['Project_Type'] = df.apply(get_quadrant, axis=1)
df['Outcome'] = df['project_success'].map({True: 'Successful', False: 'Failed'})

# This shows the "Success Rate" for each of the 4 buckets
quadrant_stats = df.groupby('Project_Type')['project_success'].mean().reset_index()
quadrant_stats['Success_Rate_%'] = quadrant_stats['project_success'] * 100

fig_quadrant = px.bar(
    quadrant_stats.sort_values('Success_Rate_%', ascending=False),
    x='Success_Rate_%',
    y='Project_Type',
    orientation='h',
    title='Which Strategy Actually Works? (Success Rate by Project Type)',
    color='Success_Rate_%',
    color_continuous_scale='RdYlGn',
    labels={'Success_Rate_%': 'Probability of Success (%)', 'Project_Type': ''},
    template='plotly_white',
    text_auto='.1f'
)

fig_quadrant.update_layout(showlegend=False, height=400,    title_x=0.5,)
fig_quadrant.show()

####################
# Density pledge rewards (low)
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean Currency
df['lowest_pledge_reward_$'] = pd.to_numeric(df['lowest_pledge_reward_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
# We filter to $200 for a readable linear scale
df_low = df[df['lowest_pledge_reward_$'] <= 10000]
success_df = df_low[df_low['project_success'] == True]
failed_df = df_low[df_low['project_success'] == False]

fig_low = go.Figure()

fig_low.add_trace(go.Violin(
    y=success_df['lowest_pledge_reward_$'],
    name='Successful Projects',
    line_color='#00CC96',
    box_visible=True,
    meanline_visible=True
))

fig_low.add_trace(go.Violin(
    y=failed_df['lowest_pledge_reward_$'],
    name='Unsuccessful Projects',
    line_color='#EF553B',
    box_visible=True,
    meanline_visible=True
))

fig_low.update_layout(
    title={'text': 'Entry Level Pledge Rewards Density', 'x': 0.5},
    yaxis_title="Pledge Amount ($)",
    template='plotly_white'
)

fig_low.show()

####################
# Density pledge rewards (high)
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['highest_pledge_reward_$'] = pd.to_numeric(df['highest_pledge_reward_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
# Separate by Project Result (Your provided logic)
df_high = df[df['highest_pledge_reward_$'] <= 10000]
success_df_h = df_high[df_high['project_success'] == True]
failed_df_h = df_high[df_high['project_success'] == False]

fig_high = go.Figure()

fig_high.add_trace(go.Violin(
    y=success_df_h['highest_pledge_reward_$'],
    name='Successful Projects',
    line_color='#00CC96',
    box_visible=True,
    meanline_visible=True
))

fig_high.add_trace(go.Violin(
    y=failed_df_h['highest_pledge_reward_$'],
    name='Unsuccessful Projects',
    line_color='#EF553B',
    box_visible=True,
    meanline_visible=True
))

fig_high.update_layout(
    title={'text': 'High-Tier Pledge Rewards Density', 'x': 0.5},
    yaxis_title="Pledge Amount ($)",
    template='plotly_white'
)

fig_high.show()

# Success Drivers and Indicators section
##=====================
# Success Drivers and Indicators
##=====================

####################
## Correlation heatmap
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
currency_cols = ['lowest_pledge_reward_$', 'highest_pledge_reward_$', 'amt_pledged_$', 'goal_$']
for col in currency_cols:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')

# Convert Success and Video to 0 and 1
df['project_success'] = df['project_success'].astype(int)
df['project_has_video'] = df['project_has_video'].astype(int)

# Select Numeric Metrics for the Heatmap
metrics = [
    'amt_pledged_$', 'percent_raised', 'project_success',
    'project_update_count', 'number_of_pledgers', 'comments_count',
    'facebook_friends_count', 'lowest_pledge_reward_$', 'highest_pledge_reward_$',
    'duration_days', 'project_has_video'
]

# Create the Correlation Matrix
corr_matrix = df[metrics].corr()

fig_heatmap = px.imshow(
    corr_matrix,
    text_auto=".2f", # Shows the correlation number in the box
    aspect="auto",
    color_continuous_scale='RdBu_r', # Red for negative, Blue for positive
    zmin=-1, zmax=1,                 # Standard correlation range
    title='What Drives Funding? (Correlation Heatmap)',
    labels={'color': 'Correlation Strength'},
    template='plotly_white'
)

fig_heatmap.update_layout(
    title={'text': 'The Drivers of Success: Correlation Heatmap', 'x': 0.5},
    height=800,
    xaxis_tickangle=-45
)

fig_heatmap.show()

####################
## ROI of Communication
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['project_update_count'] = pd.to_numeric(df['project_update_count'], errors='coerce')
df['percent_raised'] = pd.to_numeric(df['percent_raised'], errors='coerce')

df_filtered = df[df['percent_raised'] <= 1000].copy()

success_df = df_filtered[df_filtered['project_success'] == True]
failed_df = df_filtered[df_filtered['project_success'] == False]

fig_roi = go.Figure()

fig_roi.add_trace(go.Scatter(
    x=success_df['project_update_count'],
    y=success_df['percent_raised'],
    mode='markers',
    name='Successful Projects',
    marker=dict(color='#00CC96', opacity=0.5),
    hovertemplate="Updates: %{x}<br>Raised: %{y}%<extra></extra>"
))

# Add Unsuccessful Projects (Dots + Trendline)
fig_roi.add_trace(go.Scatter(
    x=failed_df['project_update_count'],
    y=failed_df['percent_raised'],
    mode='markers',
    name='Unsuccessful Projects',
    marker=dict(color='#EF553B', opacity=0.5),
    hovertemplate="Updates: %{x}<br>Raised: %{y}%<extra></extra>"
))

fig_roi.update_layout(
    title={'text': 'The ROI of Communication: Updates vs. Funding Percentage', 'x': 0.5},
    xaxis_title="Number of Project Updates",
    yaxis_title="Percent of Goal Raised (%)",
    template='plotly_white',
    legend_title="Project Result",
    height=600
)

fig_roi.show()

####################
## Funding lift looking at social media (fb pages) and funding videos
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean Currency
df['amt_pledged_$'] = pd.to_numeric(df['amt_pledged_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')

df_view = df[df['amt_pledged_$'] <= 10000].copy()
df_view['video_label'] = df_view['project_has_video'].apply(lambda x: 'With Video' if x is True else 'No Video')
success_df = df_view[df_view['project_success'] == True]
failed_df = df_view[df_view['project_success'] == False]

fig_video = go.Figure()

fig_video.add_trace(go.Box(
    x=success_df['video_label'],
    y=success_df['amt_pledged_$'],
    name='Successful',
    marker_color='#00CC96',
    boxpoints=None
))

fig_video.add_trace(go.Box(
    x=failed_df['video_label'],
    y=failed_df['amt_pledged_$'],
    name='Unsuccessful',
    marker_color='#EF553B',
    boxpoints=None
))

fig_video.update_layout(
    title={'text': 'Funding Lift: Impact of Video Assets', 'x': 0.5},
    yaxis_title="Total Amount Pledged ($)",
    xaxis_title="Video Presence",
    boxmode='group',
    template='plotly_white'
)

fig_video.show()

####################
### Social media Availability
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df_view['fb_label'] = df_view['project_has_facebook_page'].apply(lambda x: 'Has Facebook' if x is True else 'No Facebook')
success_df_fb = df_view[df_view['project_success'] == True]
failed_df_fb = df_view[df_view['project_success'] == False]

fig_fb = go.Figure()

fig_fb.add_trace(go.Box(
    x=success_df_fb['fb_label'],
    y=success_df_fb['amt_pledged_$'],
    name='Successful',
    marker_color='#00CC96',
    boxpoints=None
))

fig_fb.add_trace(go.Box(
    x=failed_df_fb['fb_label'],
    y=failed_df_fb['amt_pledged_$'],
    name='Unsuccessful',
    marker_color='#EF553B',
    boxpoints=None
))

fig_fb.update_layout(
    title={'text': 'Social Lift: Impact of Facebook Pages', 'x': 0.5},
    yaxis_title="Total Amount Pledged ($)",
    xaxis_title="Facebook Page Presence",
    boxmode='group',
    template='plotly_white'
)

fig_fb.show()

####################
## Social media impact facebook friends count
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['facebook_friends_count'] = pd.to_numeric(df['facebook_friends_count'], errors='coerce')

df_view = df[df['facebook_friends_count'] <= 10000].copy()

success_df = df_view[df_view['project_success'] == True]
failed_df = df_view[df_view['project_success'] == False]

fig_strip = go.Figure()

# Successful Projects
fig_strip.add_trace(go.Box(
    y=success_df['facebook_friends_count'],
    name='Reached Goal',
    marker=dict(color='#00CC96', size=5, opacity=0.4),
    boxpoints='all', jitter=0.5, pointpos=0,
    fillcolor='rgba(0,0,0,0)', line_color='rgba(0,0,0,0)',
    hovertext="Successful Project"
))

# Unsuccessful Projects
fig_strip.add_trace(go.Box(
    y=failed_df['facebook_friends_count'],
    name='Did Not Reach Goal',
    marker=dict(color='#EF553B', size=5, opacity=0.4),
    boxpoints='all', jitter=0.5, pointpos=0,
    fillcolor='rgba(0,0,0,0)', line_color='rgba(0,0,0,0)',
    hovertext="Unsuccessful Project"
))

fig_strip.update_layout(
    title={
        'text': "<b>Crowdsourcing Power:</b> How Personal Networks Impact Success",
        'y': 0.95, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'
    },
    yaxis_title="Total Facebook Friends",
    xaxis_title="Final Project Status",
    template='plotly_white',
    height=600,
    showlegend=False,
)

fig_strip.show()


####################
## Duration and goal $
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean Goal and Duration
df['goal_$'] = pd.to_numeric(df['goal_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
df['duration_days'] = pd.to_numeric(df['duration_days'], errors='coerce')

# Capping at $100k and 60 days ensures the bins aren't stretched too thin
df_view = df[(df['goal_$'] <= 100000) & (df['duration_days'] <= 60)].copy()

failed_df = df_view[df_view['project_success'] == False]

fig_danger = px.density_heatmap(
    failed_df, 
    x='duration_days', 
    y='goal_$', 
    nbinsx=20, 
    nbinsy=20,
    color_continuous_scale='YlOrRd', # Yellow to Red for "Danger"
    title='<b>The Danger Zone:</b> Where High Goals Meet Short Deadlines',
    labels={'duration_days': 'Campaign Duration (Days)', 'goal_$': 'Funding Goal ($)'},
    template='plotly_white'
)

fig_danger.update_layout(
    title={'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'},
    xaxis_title="Days the Campaign Lasted",
    yaxis_title="Financial Goal ($)",
    coloraxis_colorbar=dict(title="Concentration of Failures"),
    height=600
)

fig_danger.add_annotation(
    x=10, y=85000, # Points to the top-left (Short duration, High goal)
    text="<b>DANGER ZONE</b><br>High goals with very short windows<br>show the highest risk of failure.",
    showarrow=True, arrowhead=2,
    ax=50, ay=0,
    bgcolor="white", bordercolor="#EF553B"
)

fig_danger.show()

####################
## Most valuable backers
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['avg_amt$_per_pledger'] = pd.to_numeric(df['avg_amt$_per_pledger'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
# We group by both category and success to see if successful projects attract "higher value" backers
category_stats = df.groupby(['major_category', 'project_success'])['avg_amt$_per_pledger'].mean().reset_index()
# We find the order of categories based on the highest average pledge for successful projects
sort_order = category_stats[category_stats['project_success'] == True].sort_values('avg_amt$_per_pledger', ascending=False)['major_category'].tolist()
success_data = category_stats[category_stats['project_success'] == True]
failed_data = category_stats[category_stats['project_success'] == False]

fig_value = go.Figure()

# Successful Projects Trace
fig_value.add_trace(go.Bar(
    x=success_data['major_category'],
    y=success_data['avg_amt$_per_pledger'],
    name='Reached Goal',
    marker_color='#00CC96',
    text=success_data['avg_amt$_per_pledger'].map('${:,.0f}'.format),
    textposition='auto'
))

# Unsuccessful Projects Trace
fig_value.add_trace(go.Bar(
    x=failed_data['major_category'],
    y=failed_data['avg_amt$_per_pledger'],
    name='Did Not Reach Goal',
    marker_color='#EF553B',
    text=failed_data['avg_amt$_per_pledger'].map('${:,.0f}'.format),
    textposition='auto'
))

fig_value.update_layout(
    title={'text': '<b>The Backer Value Index:</b> Which Categories Attract the Highest Pledges?', 'x': 0.5},
    xaxis_title="Project Category",
    yaxis_title="Average Amount per Backer ($)",
    xaxis={'categoryorder': 'array', 'categoryarray': sort_order}, # Applies our custom sort
    barmode='group',
    template='plotly_white',
    height=600,
    legend_title="Project Status"
)

fig_value.show()


####################
### Engagement elasticity
####################

from sklearn.linear_model import LinearRegression
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean Numeric Data
df['amt_pledged_$'] = pd.to_numeric(df['amt_pledged_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
df['project_update_count'] = pd.to_numeric(df['project_update_count'], errors='coerce')

df_clean = df[(df['amt_pledged_$'] <= 50000) & (df['project_update_count'] <= 50)].dropna(subset=['amt_pledged_$', 'project_update_count'])
success_df = df_clean[df_clean['project_success'] == True].sort_values('project_update_count')
failed_df = df_clean[df_clean['project_success'] == False].sort_values('project_update_count')

# 3. Robust Regression Function
def calculate_roi_line(sub_df):
    if len(sub_df) < 2: # Need at least 2 points for a line
        return None, 0
    
    # Prepare X and y
    X = sub_df['project_update_count'].values.reshape(-1, 1)
    y = sub_df['amt_pledged_$'].values
    
    # Fit Model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict and FLATTEN the output
    predictions = model.predict(X).flatten() 
    roi_val = model.coef_[0]
    
    return predictions, roi_val

# Calculate
s_preds, s_roi = calculate_roi_line(success_df)
f_preds, f_roi = calculate_roi_line(failed_df)


fig = go.Figure()

# Success Trace
if s_preds is not None:
    fig.add_trace(go.Scatter(x=success_df['project_update_count'], y=success_df['amt_pledged_$'], mode='markers', name='Reached Goal', marker=dict(color='#00CC96', opacity=0.3)))
    fig.add_trace(go.Scatter(x=success_df['project_update_count'], y=s_preds, mode='lines', name=f'Success ROI: ${s_roi:.2f}/upd', line=dict(color='#008B66', width=3)))

# Failure Trace
if f_preds is not None:
    fig.add_trace(go.Scatter(x=failed_df['project_update_count'], y=failed_df['amt_pledged_$'], mode='markers', name='Did Not Reach Goal', marker=dict(color='#EF553B', opacity=0.3)))
    fig.add_trace(go.Scatter(x=failed_df['project_update_count'], y=f_preds, mode='lines', name=f'Failure ROI: ${f_roi:.2f}/upd', line=dict(color='#B22222', width=3)))

fig.update_layout(
    title={'text': "<b>Engagement Elasticity:</b> Funding Return per Update", 'x': 0.5},
    xaxis_title="Updates Posted",
    yaxis_title="Total Pledged ($)",
    template='plotly_white'
)

fig.show()

### business outcomes
"""The ROI of a Post: "Our analysis shows that for successful projects, each update is statistically worth $X. If you spend 20 minutes writing an update, you are essentially earning a high hourly rate for that communication."
###The Success Gap: You will likely notice the Green line is much steeper than the Red line. This proves that Engagement Elasticity is higher for winners—updates don't just happen because they are winning; updates drive the winning momentum.
###Diminishing Returns: By looking at the spread of dots, you can see if the "ROI" stays consistent at 40+ updates or if there is a "Sweet Spot" (usually between 10–25) where the most funding is captured."""

####################
## Anatomy of an overachiever
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Create the segments based on Percent Raised
def segment_success(percent):
    if percent >= 500: return 'Overachiever (500%+)'
    elif percent >= 100: return 'Standard Winner (100-499%)'
    else: return 'Failed Project (<100%)'

df['Success_Tier'] = df['percent_raised'].apply(segment_success)

# Calculating means for Update Counts and Pledge Level Counts
anatomy_stats = df.groupby('Success_Tier').agg({
    'project_update_count': 'mean',
    'total_count_of_pledge_levels': 'mean',
    'project_id': 'count'
}).reindex(['Overachiever (500%+)', 'Standard Winner (100-499%)', 'Failed Project (<100%)']).reset_index()

fig = go.Figure()

# Add Bars for Update Frequency
fig.add_trace(go.Bar(
    x=anatomy_stats['Success_Tier'],
    y=anatomy_stats['project_update_count'],
    name='Avg Updates',
    marker_color='#636EFA',
    text=anatomy_stats['project_update_count'].round(1),
    textposition='auto'
))

# Add Bars for Pledge Levels
fig.add_trace(go.Bar(
    x=anatomy_stats['Success_Tier'],
    y=anatomy_stats['total_count_of_pledge_levels'],
    name='Avg Pledge Tiers',
    marker_color='#00CC96',
    text=anatomy_stats['total_count_of_pledge_levels'].round(1),
    textposition='auto'
))

fig.update_layout(
    title='<b>Anatomy of an Overachiever:</b> Updates vs. Reward Complexity',
    xaxis_title='Project Success Segment',
    yaxis_title='Average Count',
    barmode='group',
    template='plotly_white',
    title_x=0.5,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.show()

# Print Summary for Interpretation
print(anatomy_stats)

"""
Findings: Overachievers update their backers x more often than failed projects (8.5 updates vs. 4.7 on average).
Successful projects offer an average of 10.6 pledge levels, providing significantly more entry points than the 8.4 levels offered by failures.
A direct linear correlation exists between update frequency and the final funding percentage.

1. The "Update" Correlation

The Trend: Typically, Overachievers have a significantly higher update count.
The Insight: This suggests that viral success isn't a "set it and forget it" event. 
Overachievers likely use updates to maintain momentum, announce "stretch goals," and keep the community engaged during the exponential growth phase.
Actionable Advice: If you want to break out of the "Standard Winner" pack, double your communication frequency.

2. The "Pledge Tier" Strategy
The Trend: If Overachievers have more pledge levels than Failures, it indicates that Choice Architecture matters.
The Insight: More tiers allow for "Price Discrimination"—it lets small backers in for $5 while giving high-net-worth fans a way to spend $1,000.
The Trap: If Overachievers have fewer levels than Standard Winners, it suggests that Simplicity wins when a project goes viral. Too many choices can cause "Analysis Paralysis."

3. The "Standard Winner" Gap
Look at the distance between the Standard Winner and the Overachiever. If the Update count jumps significantly (e.g., from 10 to 25 updates), 
that is your "Viral Threshold." That is the extra effort required to cross from "Successful" to "Legendary."
"""

####################
## Social Proof signal
####################
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
df['amt_pledged_$'] = pd.to_numeric(df['amt_pledged_$'].astype(str).str.replace(r'[$,]', '', regex=True), errors='coerce')
df['facebook_friends_count'] = pd.to_numeric(df['facebook_friends_count'], errors='coerce')
df['number_of_pledgers'] = pd.to_numeric(df['number_of_pledgers'], errors='coerce')
df['project_success_numeric'] = df['project_success'].astype(int)

# 2. Calculate Spearman Correlation 
corr_results = df[['facebook_friends_count', 'project_success_numeric', 'amt_pledged_$', 'number_of_pledgers']].corr(method='spearman')

# Extract the specific correlations for Facebook Friends
labels = ['Winning (Success)', 'Total Funding ($)', 'Crowd Size (Backers)']
values = [
    corr_results.loc['facebook_friends_count', 'project_success_numeric'],
    corr_results.loc['facebook_friends_count', 'amt_pledged_$'],
    corr_results.loc['facebook_friends_count', 'number_of_pledgers']
]

fig_signal = go.Figure()

fig_signal.add_trace(go.Bar(
    x=labels,
    y=values,
    marker_color=['#636EFA', '#00CC96', '#AB63FA'],
    text=[f"{v:.2f}" for v in values],
    textposition='auto',
) )

fig_signal.update_layout(
    title={'text': "<b>The Social Proof Signal:</b> Is Facebook a Vanity Metric?", 'x': 0.5},
    yaxis_title="Spearman Correlation Strength (0 to 1)",
    xaxis_title="Success Metric",
    template='plotly_white',
    yaxis=dict(range=[0, 1]), # Correlation scales from 0 to 1
    height=500
)


fig_signal.show()

# Print the Verdict for your presentation
print(f"Correlation with Success: {values[0]:.2f}")
print(f"Correlation with Funding: {values[1]:.2f}")


"""
The Vanity Threshold: If the "Winning" bar is much higher than the "Total Funding" bar, tell your audience: "Facebook friends are a vanity metric for scale. They help you get enough backers to meet your goal, but they don't necessarily attract the high-value investors who drive total funding into the millions."
The "Leading Indicator": A score above 0.40 is a "Strong Signal." If the "Crowd Size" bar is the highest, it proves that your personal network is your "Seed Crowd"—they are the ones who show up first so that strangers feel safe pledging later.
The "Social Proof" Takeaway: "Success isn't just about how many people you know; it's about how many people you know who are willing to act as a 'signal' to the rest of the world that your project is worth backing."
"""

####################
## Branding and anchor effect 
####################
from collections import Counter
import re
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Clean Currency
df['avg_amt$_per_pledger'] = pd.to_numeric(
    df['avg_amt$_per_pledger'].astype(str).str.replace(r'[$,]', '', regex=True), 
    errors='coerce'
)

# 2. NLP: Simple Tokenization & Cleaning
def get_tokens(text):
    if not isinstance(text, str): return []
    # Lowercase, remove punctuation, and split
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = text.split()
    # Filter out "Stop Words" (common words with no branding value)
    stop_words = {'the', 'and', 'for', 'with', 'your', 'this', 'from', 'that', 'a', 'of', 'to', 'in', 'on'}
    return [w for w in words if len(w) > 3 and w not in stop_words]

# Apply tokenization
df['name_tokens'] = df['project_name'].apply(get_tokens)

# We find words that appear at least 10 times to ensure statistical relevance
all_words = [word for tokens in df['name_tokens'] for word in tokens]
word_counts = Counter(all_words)
power_word_candidates = [word for word, count in word_counts.items() if count >= 10]

# Calculate the "Anchor Value" (Average Pledge) for each word
word_values = []
for word in power_word_candidates:
    # Find rows where the project name contains this word
    mask = df['name_tokens'].apply(lambda tokens: word in tokens)
    avg_val = df.loc[mask, 'avg_amt$_per_pledger'].mean()
    word_values.append({'word': word.capitalize(), 'anchor_value': avg_val})

# Create DataFrame and sort by Value
word_df = pd.DataFrame(word_values).sort_values('anchor_value', ascending=False).head(15)

fig_branding = go.Figure()

fig_branding.add_trace(go.Bar(
    x=word_df['anchor_value'],
    y=word_df['word'],
    orientation='h', # Horizontal bar for readability
    marker_color='#636EFA',
    text=word_df['anchor_value'].map('${:,.0f}'.format),
    textposition='outside'
))

fig_branding.update_layout(
    title={'text': "<b>The Anchor Effect:</b> Which Branding Words Command Higher Pledges?", 'x': 0.5},
    xaxis_title="Average Pledge Amount per Backer ($)",
    yaxis_title="Power Word in Project Name",
    template='plotly_white',
    height=600,
    yaxis=dict(autorange="reversed") # Highest value at the top
)

fig_branding.show()

### Explanation
"""
Premium Signals: Point to the top of the list. "When creators use words like 'Titanium' or 'Automatic,' they are anchoring the backer's mind to a higher price point. This shows that branding isn't just about 'looking cool'—it's a financial lever."
The Contextual Lift: If words like "Film" have a lower anchor value than "Lens," you can explain: "Backers associate physical hardware with higher value than digital content, and our data proves that this bias shows up in the project name itself."
Strategy Takeaway: "If you want to raise more money per person, you shouldn't just change your product—you should change your vocabulary. Use words that the market already associates with high-tier investments."
"""

# ML Model section
##=====================
# Predictive Modeling
##=====================
df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()
# Date update
df['date_launched'] = pd.to_datetime(df['date_launched'], dayfirst=True)
# Use the correct method to get the day name
df['week_name'] = df['date_launched'].dt.day_name()
df['year'] = df['date_launched'].dt.year
df['month'] = df['date_launched'].dt.month
# Remove unames columns
df = df.drop(['Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29'], axis=1) #drop unnamed columns
# drop facebook friends count
df = df.drop('facebook_friends_count',axis=1)
# drop city, drop minor category, project id and name, percent raised,
df = df.drop(['minor_category','project_id','project_name','percent_raised'],axis=1)
# drop date launched column
df = df.drop(['date_launched'],axis=1)
# drop city
df = df.drop('city',axis=1)
# check for target ratio
df['project_success'].value_counts().plot.bar()
# recode target variable 'project_has_video','project_has_facebook_page','project_has_pledge_rewards'
df['project_success'] = df['project_success'].replace({False: 0, True: 1, "FALSE": 0, "TRUE": 1})
df['project_has_video'] = df['project_has_video'].replace({False: 0, True: 1, "FALSE": 0, "TRUE": 1})
df['project_has_facebook_page'] = df['project_has_facebook_page'].replace({"No": 0, "Yes": 1})
df['project_has_pledge_rewards'] = df['project_has_pledge_rewards'].replace({"No": 0, "Yes": 1})
# split categorical variables
df_cat = df[['major_category','region','week_name']]
df_cat = pd.get_dummies(df_cat, columns=['major_category','region','week_name'], drop_first=False)
# cts
scaler = preprocessing.MinMaxScaler()
df_cts = df[['duration_days',
 'goal_$',
 'amt_pledged_$',
 'project_update_count',
 'number_of_pledgers',
 'comments_count',
 'project_has_video',
 'project_has_facebook_page',
 'project_has_pledge_rewards',
 'year',
 'month']] 
df_cts = scaler.fit_transform(df_cts)
df_cts = pd.DataFrame(df_cts, columns=['duration_days',
 'goal_$',
 'amt_pledged_$',
 'project_update_count',
 'number_of_pledgers',
 'comments_count',
 'project_has_video',
 'project_has_facebook_page',
 'project_has_pledge_rewards',
 'year',
 'month'])


df_cts = df_cts.reset_index(drop=True)
df_cat = df_cat.reset_index(drop=True)
target_col = df['project_success'].astype(int).reset_index(drop=True)
df_final = pd.concat([df_cts, df_cat, target_col], axis=1)
train = df_final.sample(frac=0.8, random_state=200)
test = df_final.drop(train.index)

# 4. Features & Target
features = train.drop('project_success', axis=1)
target = train['project_success']

models = {
    #'Logistic Regression': LogisticRegression(random_state=22, C=1e-9, solver='liblinear', max_iter=200),
    #'Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier(n_estimators=200, random_state=22),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=200),
    #'KNN': KNeighborsClassifier(),
    'Decision Tree': DecisionTreeClassifier(),
    #'LDA': LinearDiscriminantAnalysis(),
    'Bagging Classifier': BaggingClassifier()
}

# Create Ensemble
#ensemble_members = [(name.lower()[:2], m) for name, m in models.items()]
#models['Ensemble'] = VotingClassifier(estimators=ensemble_members, voting='hard')

# 6. Execution Loop
print(f"{'Model':<25} | {'Accuracy':<10}")
print("-" * 40)

for label, model in models.items():
    # cv=5 and scoring='accuracy'
    scores = cross_val_score(model, features, target, cv=5, scoring='accuracy')
    mean_score = scores.mean()
    print(f"{label:<25} | {mean_score:.4f}")

## testing
test_features = test.drop('project_success', axis=1)
test_target = test['project_success'].astype(int)
print(" ")
print(f"{'Model':<20} | {'Test Accuracy':<15} | {'Avg Precision':<15}")
print("-" * 55)
print(" ")
for name, model in models.items():
    # Fit the model using the training features and target
    model.fit(features, target)
    
    # Predict on the test set
    pred = model.predict(test_features)
    
    # Calculate Metrics
    acc = accuracy_score(test_target, pred)
    avg_prec = average_precision_score(test_target, pred)
    
    print(f"{name:<20} | {acc:.4f}          | {avg_prec:.4f}")

print(" ")
print("Confusion Matrix:")
print(confusion_matrix(test_target, pred))
print(" ")
print(" ")
print("\nClassification Report:")
print(classification_report(test_target, pred))
