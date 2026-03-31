
#### Category Grouping Treemap #####

####################

##=====================

df = pd.read_csv('PleaseFundThis.csv')
df.columns = df.columns.str.strip()


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




## Inspiration
The inspiration for LibTO was to explore the city of Toronto open data as part of the open data week challenge.  
## What it does
LibTO leverages City of Toronto Open Data library dataset to understand key trends and metrics impacting the Toronto Public Libary Network.  It does trend analysis for key metrics like workstation usage, visitations, registration and circulation. It looks at the different Branch tiers and their sizes.  Also shows correlations among the different metrics.  In the streamlit version, you can also go down to the Branch level as well as see the overall Library insights. 
## How we built it
- The app was built using Toronto Open data
- zerve.ai served as the analysis platform
- Python libraries were used for the analysis and visualization (Pandas and Plotly)
- Streamlit was used to deploy as web app leverage the analysis done 
## Project Summary 

The key goal was to explore the current dataset, key questions where: understanding what metrics are available, finding hidden insights and exploring trends.

### Key Insights
1. Annual Card Registrations
Library memberships saw a massive surge starting in 2021, reaching an all-time peak of over 220,000 new sign-ups in 2023. This suggests the library is more relevant to Torontonians today than it was before the pandemic.

2. Annual Circulation
The number of physical items (like books and DVDs) being borrowed has been on a steady decline since 2012. Despite a small recovery in 2022, borrowing dropped again in 2023, showing a shift away from physical media.

3. Annual Visits
Foot traffic crashed during the pandemic but has been climbing back steadily. While visits haven't yet reached 2012 levels, the upward trend shows that people are returning to the library as a physical "third space" for work and study.

4. Branch Metrics vs. Square Footage
There is a nearly perfect "stair-step" relationship between size and usage: Neighborhood libraries do well, District libraries do better, and massive Reference libraries see the most action across the board. Essentially, if you build more library space, the public will immediately fill it.

5. Branch Metrics Correlation
The data shows that people who come to use the computers are almost certain to also be cardholders and frequent visitors. Providing internet and workstations is currently the library’s most effective way to get people through the door and signed up.

6. Top 10 / Bottom 10 Branch Metrics
The Toronto Reference Library and North York Central are the "powerhouses" of the system, often seeing ten times the activity of smaller branches. Meanwhile, branches like Swansea Memorial and Todmorden Room see the lowest total volume, likely due to their limited size and resources.

7. Annual Workstation Usage
Computer sessions dropped by nearly 90% during the pandemic when branches were closed. However, usage has more than tripled since 2021, proving that a significant portion of the population still relies on the library for essential internet access.

8. Toronto Library Branches by Square Footage Map
The library's resources are heavily concentrated in the city center and along major transit lines. This leaves "service gaps" in the outer corners of the city, where branches are smaller and further apart.

9. Library Impact Index
This chart identifies the "overachievers." While big libraries have the most total visitors, smaller branches like Bridlewood and Woodside Square have a much higher "impact score" because they serve a huge number of people despite having very little square footage.


## Challenges we ran into
- The main challenge was understanding how the Zerve.ai platform worked.  I wanted to apply some forecasting but the current setup does not allow for that in the free version.  Hopefully in a future version you would be able to add your own requirements in the free version.  
## Accomplishments that we're proud of
- The ability to learn about the Zerve.ai platform, do analysis and deploy an app using streamlit
## What's next for LibTO
- Predictive Modeling: Design circulation, registrations, visits and workstation usage forecast.
- Program & Events Recommendations: Design recommendation engine for Toronto Denizens.
- Deeper Branch Intelligence: Provide predictive Branch level Insights and forecasts.