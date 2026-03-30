
Persona: Python and streamlit app developer
Context:
I would like to build a one page streamlit app that has these sections.  Overview, Region Insights, City Insights, Category Insights, Success Prediction. ALl graphs will be built using plotly and data manipulation using pandas.
To toggle between section it would use a radio button


Overview Section
- It will have no sidebar. 
- It will use Use st.metric to display # of cities, # of regions, "Overall Success Rate",Average duration, Avg. goal $,  and "Average Pledge.  
- It would then have two columns
 In the first column
 - top 10 countries (region) by amount pledged
 - ranked vertical  bar chart looking at major category by amount pledged
 - top 10 projects by amount pledged
 In the second column
 - top 10 cities by amount pledged
 - ranked vertical bar chart looking at minor category by amount pledged
 - donut chart based on project success
 
Region Insights Section
- Region will have one multi-select field called Region in the sidebar

City Insights Section
City Insights will have one multi select field called City in the sidebar

Category Insights Section
Category Insights will have two multiselect fields called Major Cateogry and Minor Category.  Major Category should filter Minor Category.  Both Major Category and Minor Category will be on the sidebar

Success Prediction
It should use the Predictive Modeling code and simple user inputs for the user to enter and then it would use the best model to generate a success prediction.  Lets give the user to have 5 - 10 inputs

All sections should have these tabs except overview and Success Prediction section should have these sections
- Category and Markets
- Flow and Distribution
- Success Drivers & Indicators
- Performance Trends and Comparisons

USE THE ATTACHED DATASET AND code below for the design.  Show reasoning

persona: data analytics and visualization expert
for the images provided, analyze them and generate insights from them.  The insights should be understood by a non-technical audience.  The data it was built from was based on crowdfunding data.
Show reasoning for the insights.





<!-- 4. Section 3: Predictions (The "Actionable" Tool)

Goal: Transform historical data into a forward-looking consultant.
Reasoning: * The "What-If" Engine: Instead of just showing what happened, give the user st.slider and st.number_input widgets. A creator can input their "Goal Amount," "Category," and "Social Media Count."

Real-time Probability: Behind the scenes, use the Logistic Regression or Random Forest model from Part 1 to output a "Success Probability %" in real-time.

Prescriptive Analytics: If the prediction is low, the app could show a message like: "Increasing your updates from 0 to 5 could improve your success probability by 12%." This turns a chart into a strategy. -->