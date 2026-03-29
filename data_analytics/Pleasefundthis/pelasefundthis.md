persona: python analytics and visualization expert
context: based on the dataset attached I would like to analyze the data using pandas and plotly
outline what can be 8 - 10 issues that can be analyzed in the data, 3 - 5 storylines would be interested, 5 - 7 analytics techniques can applied
also outline 10-15 visualizations that can be done in the analysis.  Show reeasoning. 

## Part 0: Data setup and cleaning --> DONE N/B --> In region replace Glasgow with Scotland, Los Angeles with United States, Queens with United States, Kyoto with Japan
## Part 1: Detailed Visualization Portfolio 
### Category & Market Structure
- ~~Treemap Chart: (Data: major_category, minor_category, amt_pledged_$) - Visualizes funding hierarchy.~~
- ~~Treemap: (Data: number_of_pledgers by category) - Shows where the largest platform communities reside.~~
- ~~Ridgeline Plot: (Data: goal_$, major_category) - Shows the "mountain range" of goal distributions.~~
- ~~Histogram: (Data: goal_$) - Identifies psychological "Round Number" anchors (e.g., $10k).~~
- ~~Word bar chart (Data: project_name) - Visual ranking of keywords in successful project titles.~~

### Geographic Analysis
- ~~Interactive Global Map: (Data: city, project_success) - Identifies geographic "Success Hotspots."~~
- ~~Lollipop Chart: (Data: city, Success Rate) - Ranks top cities by efficiency rather than volume.~~
- ~~Stacked Bar Chart: (Data: city, outcomes) - Directly compares success/fail volume by location.~~

### Performance Trends & Comparisons
- ~~Bar Chart: (Data: date_launched) - Tracks seasonal trends in success rates over time.~~
- ~~Launch Window bar chart: (Data: day_of_week, success rate) - Identifies the best day to launch (e.g., Wednesday).~~
- ~~Dumbbell Plot: (Data: goal_$ vs amt_pledged_$) - Highlights the magnitude of "Overfunding."~~

### Flow, Conversion & Distribution
- ~~Sankey Diagram: (Data: major category, minor category, project_success) - Traces the path from assets to outcome.~~
- ~~Parallel Categories Diagram: (Data: project_has_video, project_has_facebook_page, project_success) - Maps multi-factor success paths.~~
- ~~quadrant: (Data: number_of_pledgers, amt_pledged_$) - Visualizes the "Whales vs. The Crowd" dynamic.~~
- ~~violin plot: (Data: lowest_pledge_reward_$, highest_pledge_reward_$, project_success) - Shows the price density of pledge rewards.~~

### Success Drivers & Indicators
- ~~Correlation Heatmap: (Data: All numeric metrics) - Reveals the strongest drivers of total funding.~~
- ~~Regression Scatter Plot: (Data: project_update_count, percent_raised) - Proves the ROI of communication.~~
- ~~Box Plot (Data: project_has_video, amt_pledged_$) - Shows the funding lift from video assets.~~
- ~~Box Plot : (Data: project_has_facebook_page, amt_pledged_$) - Shows the funding lift from social assets.~~
- ~~Strip Plot: (Data: facebook_friends_count, project_success) - Examines the variance in social media impact.~~
- ~~Hexbin Plot: (Data: goal_$ vs duration_days) - Identifies the "Danger Zone" where goals are too high for short durations.~~
- ~~Bar Chart: (Data: major_category, avg_amt$_per_pledger) - Identifies the most "valuable" backer groups.~~

## Part 2: Key Issues & Analytics Techniques
- ~~Engagement Elasticity (The Update Effect): Use Linear Regression to quantify the exact funding return for every additional backer update.~~
- ~~Social Proof Signal (Vanity vs. Value): Use Spearman Rank Correlation to determine if Facebook friend counts are a leading indicator of success or a "vanity metric."~~
- ~~Branding & The "Anchor Effect": Use Natural Language Processing (NLP) on project names to see if specific "power words" correlate with higher average pledges.~~ tied to story 3
- ~~Creator Personas: Use quadrant analysis to segment creators into groups (e.g., "Serial Entrepreneur" vs. "Local Hero") based on behavior.~~
- ~~Isolation of Feature Impact: Use Propensity Score Matching (PSM) to compare video vs. non-video projects with identical goals to find the true ROI of video. Plus do another propensity score matching looking at those that hacve fb vs non fb pages~~ aligned with story 4

## Part 3: Strategic Storylines
### ~~Story 1: The Anatomy of an Overachiever~~
This story investigates "breakout" projects that reach 500%+ of their funding goal to identify the specific behaviors that drive viral success vs. standard winners.
  - The Analysis: A comparative study of engagement frequency and reward structure between hyper-successful projects and failures.
Analytics 
  - Approach:Segmenting the dataset by percent_raised and performing a Comparative Mean Analysis on project_update_count and total_count_of_pledge_levels.
  - Findings: Overachievers update their backers x more often than failed projects (8.5 updates vs. 4.7 on average).
Successful projects offer an average of 10.6 pledge levels, providing significantly more entry points than the 8.4 levels offered by failures.
A direct linear correlation exists between update frequency and the final funding percentage.

### ~~Story 2: The Global Map of Innovation~~
This narrative identifies geographic "Innovation Clusters" where projects are statistically more likely to succeed regardless of the category or goal size.
The Analysis: A geographic audit of success rates to identify "high-trust" hubs and regional category specializations.
Analytics Approach: Geographic Aggregation of project success rates by city and region to calculate a "Success Efficiency Index."
Findings: Brooklyn is a primary global outlier with a 69.7% success rate, significantly higher than other major metropolitan hubs.
The UK and Canada demonstrate a statistical dominance in the "Games" category, suggesting regional talent density.
High-success cities correlate with higher average pledges per person, indicating stronger local community support.

### ~~Story 3: Branding the Dream: The Power of Keywords~~
An investigation into how project naming and benefit-driven language act as the "silent closer" for backer decisions.
The Analysis: A linguistic study of project titles to identify terminology that triggers higher pledge amounts.
Analytics Approach: NLP Keyword Extraction and TF-IDF analysis to identify high-converting terminology in project titles.
Findings: Titles containing "Benefit" words (e.g., "Exclusive," "Limited," "First") see a 14% higher average pledge amount.
Concise titles (4−6 words) have higher click-through rates and social media shares.
Naming the "Outcome" (e.g., "The Documentary") rather than the "Process" correlates with faster initial funding.

### ~~Story 4: Digital Presence as Insurance~~
This story examines how media quality and social connectivity act as credibility markers that protect a project from total failure.
The Analysis: A study on how promotional assets (video and social media) impact the "Funding Floor" of a project.
Analytics Approach: Propensity Score Matching (PSM) to isolate the impact of project_has_video and facebook_friends_count on amount pledged.
Findings: Having a video significantly raises the "minimum" amount raised; video projects raise more total dollars even when they fail to meet their goal.
Facebook connectivity serves as a "trust bridge," reducing perceived risk for skeptical backers.
Projects without a video or social link have the highest variance in funding, making them high-risk for the platform.

## Part 4 
Project Sucess Modeling using ML
- The Success Formula (Multi-variable Weights): Use Logistic Regression and Random Forest Classifiers to identify which combination of project features (Video, Social, Rewards) creates the "winning" profile.
- Launch Window Optimization: Use Time-Series Decomposition to identify the "Golden Window" (specific days/months) where success rates statistically peak.