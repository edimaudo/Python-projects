PROBLEM SETTING


Commercial corn is processed into multiple food and industrial products. It is widely known as one of the world’s most important crops. Each year, plant breeders create new corn products, known as experimental hybrids, by crossing two “parents” together. The parents are known as inbreds and the development of the inbreds takes up the bulk of a corn breeding program. Most of that effort is spent evaluating the inbreds by crossing to another inbred, called a “tester.” 

It is a plant breeder’s job to identify the best parent combinations by creating experimental hybrids and assessing the hybrids’ performance by “testing” it in multiple environments to identify the hybrids that perform best. Historically, identifying the best hybrids has been by trial and error, with breeders testing their experimental hybrids in a diverse set of locations and measuring their performance, then selecting the highest yielding hybrids. The process of selecting the correct parent combinations and testing the experimental hybrids can take many years and is inefficient, simply due to the number of potential parent combinations to create and test.

RESEARCH QUESTION
Given historical hybrid (inbred by tester) performance data across years and locations, how can we create a model to predict/impute the performance of the crossing of any two inbred and tester parents? 

For example, given 5,000 inbreds (parents), the number of potential crosses is 12,497,500 —far more than can be created or tested. Due to limited testing resources, breeders are only able to select a small subset of all the possible inbred combinations, which can lead to lost opportunities. 

This issue is the basis for the 2020 Syngenta Crop Challenge in Analytics. Can an accurate model be constructed to predict the performance of crossing any two inbreds? Such a model would allow breeders to focus on the best possible combinations. 

In simpler terms, can we use hybrid data collected from crossing inbreds and testers together to predict the result of cross combinations that have not yet been created and tested? Namely, are we able to construct a recommender system to propose new parent combinations based on the hybrid performance from other parent combinations and attributes they have in common? 

The following Table 1 is an illustration of the challenge. Each “X” is the set of observed performance data points of hybrids from their corresponding inbred by tester combinations. With the information from the table, how can a model be built to predict/impute the mean yield of each missing combinations (“?”)?


RESEARCH QUESTION
Given historical hybrid (inbred by tester) performance data across years and locations, how can we create a model to predict/impute the performance of the crossing of any two inbred and tester parents? 

OBJECTIVE
The objective is to estimate yield performance of the cross between inbred and tester combinations in a given holdout set. Specifically, we are asking for the mean yield performance of each inbred by tester combination in the holdout set. 

Notes
Each response in the holdout must be completed
Many approaches can be used such as statistical approaches, machine learning and collaborative filtering

Deliverables
Predicted yield values of the cross between inbred and tester combinations in the test set.
Additionally, observing the standards for academic publication, entries should include a written report with the following:
Quantitative results to justify your modeling and classification techniques
A clear description of the methodology and theory used
References or citations as appropriate

Evaluation
The entries will be evaluated based on:
Accuracy of the predicted values in the test set based on root mean squared error
Simplicity and intuitiveness of the solution
Clarity in the explanation
The quality and clarity of the finalist’s presentation at the 2020 INFORMS Conference on Business Analytics and Operations Research

dataset
Training Dataset: This dataset contains the observed yield (consistently scaled to an internal benchmark) for a large set of corn hybrids tested across multiple environments between 2016 and 2018. These hybrids are created through the crossing of 593 unique inbreds and 496 unique testers. Creating a two-way table of means with inbreds as rows and testers as columns results in a data table with approximately 96% missing values. Each row contains the year and location ID of the observation. Additionally, each row includes a cluster value for each inbred and tester. This represents the genetic grouping of the inbreds and testers and has been determined using internal methods. Inbreds and testers are not treated any differently when clustering, so a shared cluster value indicates genetic similarity regardless of whether a parent is defined as an inbred or a tester. Contestants may (or may not) find these columns useful.

Test Dataset: This dataset contains a set of inbred and tester combinations that need to be predicted as part of the challenge. The mean yield is to be predicted for each listed combination of inbred by tester.


Training Dataset	

YEAR	Year grown

LOCATION	ID for each location

INBRED	ID for Inbred

INBRED_CLUSTER	Cluster association for each inbred which denotes genetic grouping

TESTER	ID for Tester

TESTER_CLUSTER	Cluster association for each tester which denotes genetic grouping

YIELD	The performance of the Line and Tester combination


Testing Dataset	

INBRED	ID for INBRED

INBRED_CLUSTER	Cluster association for each line which denotes genetic grouping

TESTER	ID for Tester

TESTER_CLUSTER	Cluster association for each tester which denotes genetic grouping

YIELD	The performance of the Line and Tester combination – to be predicted



