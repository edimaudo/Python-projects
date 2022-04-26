### Background
Within the human gut there are trillions of microorganisms, referred collectively to as the gut
microbiome, that contribute to many aspects of human health. The gut microbiome influences a wide range of human health, from food digestion to function of the immune system and mental health. The large influence the gut microbiome has on human health means that shifts in the microorganisms present can actually alter human health and lead to the development of some diseases. One goal in the medical community is to be able to diagnose different diseases based on the type and amount of bacteria present in a patient’s gut microbiome. Several research groups have demonstrated the ability to accurately classify diseases, such as inflammatory bowel disease, depression, colorectal cancer, and Parkinson’s disease.

### The Problem
Commonly, researchers assess disease classification for one disease at a time. The training
dataset contains gut microbiome information from patients with the disease and a similar number of healthy individuals. This leads to the potential that the machine learning model is simply recognizing the gut microbiome as “unhealthy” instead of identifying a specific signature for each disease. For example, a machine learning model trained to classify inflammatory bowel disease would also classify a patient that has colorectal cancer as having inflammatory bowel disease. The misclassification substantially reduces the ability to use machine learning models to classify different diseases in a clinical setting.


### Objective
Develop a multi-label classification model to classify different diseases based on the
microorganisms in the gut microbiome.

### The dataset 
It consists of the microorganisms in the gut microbiomes of people with different
diseases. There are 1949 samples for Disease-0, 1213 samples for Disease-1, 578 samples
for Disease-2, and 3741 healthy samples. Each row corresponds to a sample collected from
an individual and each column refers to a bacteria identified in at least one person’s gut
microbiome. The “disease” column indicates the label for each sample. 
The sum of all the microorganisms in each sample can vary substantially. This variation is not biologically significant and in fact an artifact of the technology used to collect the data. You will need to implement a way to transform the data of each sample to remove this artifact.

### Metrics for scoring
F1 score
Cohen’s kappa
Accuracy

### Other metrics
Innovation
- AI fairness
- Accounting for the unbalanced dataset?

Documentation
- How well documented is the submitted code?
- Is the code easy to follow?

Performance
- How good was the disease classification for
- the final model generated?

Code
- How organized is the submitted code?
- How concise is the code for building the model?



