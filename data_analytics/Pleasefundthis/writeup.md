## Inspiration
The inspiration for doing the analysis was listening the Exploding Kittens episode of <b>How I Built This</b> podcast by Guy Raz.  The episode was talking about how an entrepreneur used crowdfunding to sell their card product.  I wanted to explore this more from an analytics standpoint.
## What it does (Project Summary)
The analysis looks at crowdfunding from different perspective leveraging visualization, analytics and machine learning.  It focused on 4 core themes.
- **Category & Market Insights (The "Where")**: This theme establishes the environment. It helps the user get a good performance baseline.
- **Performance Trends & Comparison (The "When & How Much")**: This theme focuses on benchmarking. It moves from what the market is to how it behaves over time and against expectations.
- **Flow & Distribution** (The "Who & What"): This theme analyzes the mechanics of the crowd. It looks at how many people are involved and at what price points.
- **Success Drivers & Indicators** (The "Why"): This theme attempts to find metrics that would drive crowdfunding outcomes.
The analysis was done using the zerve.ai platform.  Also a sucess prediction classification model was built.  Peformed training and tested the data using different machine learning models and experiments.  I then settled on a gradient boosting model.  the finalized model had an accuracy of 66%
A web version was built using In the **streamlit**. It has an overview section, Country Insights, City Insights, Category Insights and Success Prediction. 
## How it was built
- The app was built using Crowdfunding data
- zerve.ai served as the analysis and prediction platform
- Python libraries were used for the analysis (Pandas), visualization (Plotly) and machine learning (scikit-learn)
- Streamlit was used to deploy as web app
## Key Insights
The key insights are aligned to the themes show in the Project Summary section.
### Category and Market Insights
1. **Creator Persona: Value vs. Volume**: Most creators are stuck in the "Struggles" phase; moving to "Star" status requires a rare "double threat" of high prices and massive popularity. See Createor Persona Value vs Volume chart. 
2. **Cities by Success Rate**: High success isn't about being in a "big" city; smaller, specialized creative hubs like Edinburgh are much more effective for crowdfunding. This suggests that smaller, high-trust communities provide better support for local projects. See Cities by Success Rate Chart.
3. **Keywords of Succes**s: Backers are most attracted to "firsts" and physical, traditional media. The word "Album" is the single most powerful driver of funded projects. See Keyword of Success chart.
4. **Funding Goal Target Amount Distribution**: Creators rely on "psychological round numbers" like $5,000 and $10,000 to set their goals, rather than calculating exact project costs. See Funding Goal Target Distribution chart.
5. **The "Mountain Range" of Goal Distributions**: Different industries have completely different "normal" costs; Technology projects typically ask for 10x more than Art or Dance projects. See Mountain range of goal distribution chart.
6. **Pledgers by Category**: Video Games and Narrative Film are the "community kings." They don't just raise money; they attract the highest volume of individual people. See Pledgers by Category chart.
7. **Pledge Amount by Minor Category**: Within the gaming world, Video Games are the undisputed heavyweight, earning more than double the next most successful sub-category (Documentaries). See Pledge Amount by Minor Category chart.
8. **Pledge Amount by Major Category**: There is a "Top 5" elite group of categories (Games, Film, Design, Tech, Music) that captures the vast majority of all crowdfunding dollars. See Pledge Amount by Major Category chart.
9. **Funding Hierarchy - Major to Minor Breakdown:** Success in "Design" and "Technology" is extremely narrow; almost all the money goes to Product Design and Hardware, leaving very little for software or graphics. See Funding Hierarchy - Major to Minor Breakdown chart.
### Performance Trends and Comparison
1. Seasonal Success: Which Months Win?

Insight: There is a massive "Spring-Summer Peak" for crowdfunding success, while the end of the year is a graveyard for new projects.

Reasoning: The success rate climbs steadily through the spring, peaking in June at 72.4%. Conversely, as soon as August hits, the rate crashes to 42.0% and stays low through December. This suggests that backers are more engaged and willing to pledge during the first half of the year, perhaps due to "donor fatigue" or holiday spending competition in the later months.

2. Success Rate by Day of Week

Insight: The specific day you launch your project is surprisingly irrelevant—unless you launch on a Saturday.

Reasoning: Most days of the week show a very consistent success rate of around 49-50%. However, Saturday is the clear outlier with a dip to 46.7%. This indicates that while mid-week launches are generally safe, weekends are likely "dead zones" where potential backers are less likely to be checking emails or browsing crowdfunding platforms.

3. "Funding Gap" by Category

Insight: Some industries are much more realistic about their value than others; Technology and Design creators set high goals but come closest to hitting them, while Publishing and Fashion projects are significantly over-ambitious.

Reasoning: This chart compares the median goal (red) to the median amount pledged (green). In Technology, the green dot is very close to the red dot, showing a small "gap." In Publishing, however, the green dot is far to the left, indicating that these projects often raise only a tiny fraction of their high funding goals.

4. Magnitude of Overfunding: Top 20 Most Successful Projects

Insight: The "Super-Successes" of crowdfunding (like Oculus Rift or OUYA) aren't just hitting their goals; they are often exceeding them by millions of dollars.

Reasoning: This visualization shows that for the top 20 projects, the "Goal" (red dot) is often a tiny fraction of the "Pledged Amount" (green dot). For example, the OUYA console had a goal well under $1M but ended up nearing the $10M mark. This highlights the "viral" nature of crowdfunding, where a project that captures the public's imagination can blow past its initial requirements almost instantly.

## Flow and Distribution
1. Success Rate by Project Type

Insight: High volume is the strongest predictor of success, but mass appeal at a low cost is nearly as effective.

Reasoning: "The Unicorns" (high volume and high value) have the highest success rate at 95.3%. However, "The Crowd" (mass appeal, low cost) follows closely at 93.7%. This shows that you don't necessarily need high-priced items to succeed; a large number of backers at a lower price point is a statistically "safe" bet.

2. Entry-Level Pledge Rewards Density

Insight: Successful projects keep their "buy-in" price low and focused, while failed projects often try to offer extremely expensive entry-level tiers.

Reasoning: Successful projects (green) have a very tight density near the $0–$200 range. Unsuccessful projects (red) show "outlier" dots stretching all the way up to $10,000. If your lowest reward is too expensive, you lose the "crowd" that drives momentum.

3. High-Tier Pledge Rewards Density

Insight: Both successful and failed projects offer "VIP" rewards at the $10k mark, but successful projects have a much higher concentration of rewards in the $1k–$2k "sweet spot."

Reasoning: The "violin" shape for successful projects is wider (thicker) around the $2,000 mark. This suggests that having reachable "high-tier" rewards is more effective than just having one or two "impossible" $10,000 rewards.

4. Multi-Factor Success Paths: Video & Facebook

Insight: A video is a "must-have," but Facebook presence is the ultimate "deal-maker."

Reasoning: The widest green path (Success) flows from Video: True through Facebook: Yes. Notice the red path (Failure) for projects that have a video but no Facebook presence. This indicates that while a video explains the project, a social network is required to actually bring people to the page.

5. Project Flow: From Category to Success

Insight: Creative "niche" categories like Dance, Theater, and Comics have a much higher flow toward "Successful" than broad categories like Technology or Publishing.

Reasoning: Looking at the teal lines (Success) vs. the coral lines (Failed), the lines coming from Dance and Comics are almost entirely teal. In contrast, the "Technology" and "Publishing" paths are heavily split with coral, showing these categories are much riskier and have a higher rate of total failure.

## Success Drivers and Indicators
1. The ROI of Communication: Updates vs. Funding Percentage

Analysis: This scatter plot shows a dense vertical cluster of successful projects (green) between 10 and 40 updates, often achieving 200% to 800% of their goals. Unsuccessful projects (red) are almost entirely flatlined at the bottom, rarely exceeding 5–10 updates.

Reasoning: Regular updates function as "social proof" and momentum builders. Each update triggers an email to backers, keeping the project top-of-mind and encouraging "viral" sharing. A lack of updates signals a dead or abandoned project to potential donors.

2. Funding Lift: Impact of Video Assets

Analysis: The box-and-whisker plot shows that projects "With Video" have a median pledge amount significantly higher (roughly $3,200) than those "Without Video" (roughly $1,500).

Reasoning: Crowdfunding is an exercise in trust. A video humanizes the creator and demonstrates a working prototype or a clear vision, reducing the "perceived risk" for the backer. This higher trust translates directly into a willingness to pledge larger amounts.

3. Social Lift: Impact of Facebook Pages

Analysis: This chart mirrors the video asset trend but with even more drastic disparity. Projects with a Facebook presence show a much tighter and higher distribution of success, while the "No Facebook" category has a median funding near zero.

Reasoning: A Facebook page provides an external community "landing pad." It allows for targeted advertising and organic social discovery. Without this infrastructure, a project is forced to rely entirely on the platform’s internal traffic, which is rarely enough to hit a goal.

4. The Drivers of Success: Correlation Heatmap

Analysis: The strongest positive correlation is between amt_pledged_$ and number_of_pledgers (0.86), followed by comments_count (0.72). Interestingly, duration_days has a negligible or slightly negative correlation with success (-0.12).

Reasoning: Success is driven by the size of the crowd rather than the length of the campaign. Adding more days to a campaign doesn't help if you aren't actively acquiring new backers; in fact, longer campaigns often lose momentum and urgency.

5. Anatomy of an Overachiever: Updates vs. Reward Complexity

Analysis: Overachievers (500%+) average 12.8 updates and 12.7 pledge tiers. Standard winners drop to 4.6 updates and 9.9 tiers.

Reasoning: High-performing projects offer "something for everyone." By having more tiers, they capture different levels of disposable income. By having more updates, they maintain the "hype cycle" required to blow past their original goal.

6. The Backer Value Index: Category-Specific Pledges

Analysis: Technology leads with an average pledge of $140 for successful projects, while Comics and Games sit at the bottom around $45–$46.

Reasoning: This reflects the "unit price" of the industry. A new tech gadget costs more to produce and buy than a single comic book or a digital game download. Tech creators need fewer backers to hit a $10k goal than a comic creator does.

7. The Anchor Effect: Power Words in Branding

Analysis: Projects using the word "Affordable" command an average pledge of $533, while "Speaker" or "Wonderland" sit below $200.

Reasoning: This is a psychological "anchor." Paradoxically, labeling something "affordable" often attracts high-value buyers looking for a "deal" on a premium item (like high-end audio or tech), leading to higher individual transaction values.

8. Crowdsourcing Power: Personal Networks

Analysis: The distribution of Facebook friends for those who "Reached Goal" vs. those who "Did Not" is nearly identical in density, with both groups clustering heavily under 1,000 friends.

Reasoning: This proves that while having a Facebook page (Image 3) is vital, having a massive personal friend list is a "vanity metric." Successful creators convert strangers into backers through marketing, rather than just relying on friends and family.

9. The Danger Zone: Goals vs. Deadlines

Analysis: The heat map shows a massive concentration of failures (dark red) at the 30-day mark for goals under $10,000.

Reasoning: Many creators choose the 30-day default and a "modest" goal but fail because they lack the marketing assets (Video/Facebook) to fill that window. It’s the "zone" where lack of preparation meets the reality of platform competition.

10. The Social Proof Signal: Correlation Strength

Analysis: This bar chart quantifies the Spearman Correlation of Facebook presence. It shows a very low correlation (0.07 to 0.11) between Facebook metrics and the actual "Winning" outcome.

Reasoning: This reinforces Image 8. Facebook is a tool for communication, not a guarantee of funds. A project needs a Facebook presence to look legitimate, but the presence itself doesn't "force" people to spend money; the product and the updates (Image 1) do that.

## Challenges 
- The main challenge was understanding how the Zerve.ai platform worked.  I noticed if I made to many block the app slowed down so had to reduce the number of blocks used.  
## Accomplishments 
- The ability to learn about the Zerve.ai platform, do analysis and deploy an app using streamlit.
## Next steps for PleaseFundThis
<li><strong>Next Best Pledge:</strong> Build Predictive model to Find the right Pledge Amount to ask for</li>
<li><strong>Category Intelligence:</strong> Give the users the ability to ask questions using an LLM so that they are better setup for success</li>


