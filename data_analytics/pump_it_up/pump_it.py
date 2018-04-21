# Libraties
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sklearn.metrics import roc_curve
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold, cross_val_score, train_test_split

# Settings
pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', 1000)
sns.set_style('whitegrid')
sns.color_palette('pastel')
#%matplotlib inline

# Data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_target = pd.read_csv('target.csv')
# Concatenation
dummy_targets = pd.get_dummies(train_target, prefix='dummy')
dummy_targets = dummy_targets[dummy_targets.columns[1:]]
concat_train_data = pd.concat([train_data,dummy_targets],axis=1)

funder - 1898
installer - 2146
def funder_cat(x):
    if x <= 1:
        return 's1'
    elif (x>1) & (x<=5):
        return 's2'
    elif (x>5) & (x<=10):
        return 's3'
    elif (x>10) & (x<=20):
        return 's4'
    elif (x>20) & (x<=50):
        return 's5'
    elif (x>50) & (x<=100):
        return 's6'
    elif (x>100) & (x<=150):
        return 's7'
    elif (x>150) & (x<=200):
        return 's8'
    elif (x>200) & (x<=300):
        return 's9'
    elif (x>300):
        return 's10'

def funder_clean(data):
    funder_piv = data.pivot_table(index='funder', values='id', aggfunc=len)
    funder_df = pd.DataFrame()
    funder_df['type'] = funder_piv.index
    funder_df['count'] = funder_piv.values
    funder_df['funder_size'] = funder_df['count'].apply(lambda x: funder_cat(x))
    funder_map = dict(funder_df[['type', 'funder_size']].values)
    data['funder_size'] = data.funder.map(funder_map)
    data.funder_size.fillna('None', inplace=True)
    data = data.drop(['funder'], axis=1)
    return data

# response rate
# ward_feature
def score_brackets(x):
    if (x>=0) & (x<=0.1):
        return 1
    # ...
    elif (x>0.9):
        return 10
    else:
        return 0
def ward_rr_func(x):
    return len(concat_train_data[(concat_train_data.ward==x)&(concat_train_data['dummy_functional']==1)])/len(concat_train_data[concat_train_data.ward==x])
def ward_rr_rep(x):
    return len(concat_train_data[(concat_train_data.ward==x)&(concat_train_data['dummy_functional needs repair']==1)])/len(concat_train_data[concat_train_data.ward==x])
def ward_rr_nofunc(x):
    return len(concat_train_data[(concat_train_data.ward==x)&(concat_train_data['dummy_non functional']==1)])/len(concat_train_data[concat_train_data.ward==x])
ward_piv = pd.DataFrame(concat_train_data.pivot_table(index='ward', values='id', aggfunc=len))
ward_piv.sort_values(by='id',ascending=False,inplace=True)
ward_piv['name']=ward_piv.index
ward_piv['response_rate_functional'] = ward_piv['name'].apply(ward_rr_func)
ward_piv['response_rate_needs_repair'] = ward_piv['name'].apply(ward_rr_rep)
ward_piv['response_rate_non_functional'] = ward_piv['name'].apply(ward_rr_nofunc)
ward_piv['functional_label'] = ward_piv['response_rate_functional'].apply(score_brackets)
ward_piv['needs_repair_label'] = ward_piv['response_rate_needs_repair'].apply(score_brackets)
ward_piv['non_functional_label'] = ward_piv['response_rate_non_functional'].apply(score_brackets)
ward_map = ward_piv.iloc[:,[1,5,6,7]]
ward_func_map = dict(ward_map[['name','functional_label']].values)
ward_repair_map = dict(ward_map[['name','needs_repair_label']].values)
ward_non_func_map = dict(ward_map[['name','non_functional_label']].values)
ward_map.head()

# Removed features
# Feature Reductions
data.drop(['recorded_by'], axis=1, inplace=True)
data.drop(['extraction_type','extraction_type_group'], axis=1, inplace=True)
data.drop(['management'], axis=1, inplace=True)
data.drop(['payment'], axis=1, inplace=True)
data.drop(['water_quality'], axis=1, inplace=True)
data.drop(['quantity'], axis=1, inplace=True)
data.drop(['source','source_class'],axis=1,inplace=True)
data.drop(['waterpoint_type'], axis=1, inplace=True)

# feature cleaning
op_years = list(data.date_recorded_year-data.construction_year)
operational_years = []
for i in op_years:
    if (i > 500) or (i < 0):
        operational_years.append(0)
    else:
        operational_years.append(i)
data['operational_years'] = operational_years

iter_ = ['region','basin','scheme_management','extraction_type_class','management_group',
        'payment_type','quality_group','quantity_group','source_type','waterpoint_type_group',
        'funder_size','installer_size']
for idx in iter_:
    col_ = pd.Categorical.from_array(data[idx])
    data[idx]= col_.codes

#feature transformation
def transform_data(data):
    # Transformation of variables if required or for testing
    data['amount_tsh'] = data.amount_tsh.apply(lambda x: np.log(x+1))
    data['operational_years'] = data.operational_years.apply(lambda x: np.log(x+1))
    data['population'] = data.population.apply(lambda x: np.log(x+1))
    return data

# Random forest model
new_rf_model = RandomForestClassifier(random_state = 123, n_estimators = 100)
new_rf_model.fit(prep_new_data, new_targets_status)
predictions = new_rf_model.predict(prep_new_data)
print(len(new_targets_status[new_targets_status==predictions])/len(new_targets_status))

kf = KFold(prep_new_data.shape[0], n_folds=10,shuffle=True,random_state=123)
cvs = cross_val_score(new_rf_model,prep_new_data, new_targets_status,cv=kf)


#create differnt rf models and test
def iterate_rf(iterations,X_train,Y_train,X_final):
    kf = KFold(X_train.shape[0], n_folds=10,shuffle=True,random_state=123)
    pred_df = pd.DataFrame()
    accuracies = []
    for i in range(iterations):
        rf_model = RandomForestClassifier(n_estimators = 100)
        xtrain, xtest, ytrain, ytest = train_test_split(X_train, Y_train, test_size=0.25, random_state=123)
        rf_model.fit(xtrain,ytrain)
        predictions = rf_model.predict(xtest)
        acc = len(ytest[ytest==predictions])/len(ytest)
        accuracies.append(acc)
        final_predictions = rf_model.predict(X_final)
        pred_df[i] = final_predictions
    return pred_df, accuracies

rf_df, rf_accuracies = iterate_rf(200,prep_new_data, new_targets_status,new_prep_final)    

#submission
# best_idx = new_accuracies.index(max(new_accuracies))
# submission_best = pd.DataFrame()
# submission_best['id']=test_data['id']
# submission_best['status_group'] = new_df.iloc[:,best_idx]

# binary converter. To ensure, whether boolean or string value of whichever input
def binary(x):
	if (x == True) or (x == 'True'):
		return 1
	elif (x == False) or (x == 'False'):
		return 0