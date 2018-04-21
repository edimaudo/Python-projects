#After refueling your space ship at a particularly sketchy space gas station, the chief engineer notices that the engines are 
#behaving abnormally.He thinks that the captain may have been scammed, and that the fuel has been cut with a less efficient isotope. 
#As the lead analyst on the ship, you're given the engineer's data. Your mission now is to determine if the fuel has truly been 
#contaminated, and to recommend an appropriate course of action.
#
#Step 1: Create the models.
#
#Download the engineer's data of the fuel's decay, and fit two linear regression models. 
#First, with the uncontaminated equation N(t)=A r_1 e^{-r_1 t}+C, and 
#second with the contaminated equation N(t)=A r_1 e^{-r_1 t}+B r_2 e^{-r_2 t}+C. A and B represent the amount of good 
#and bad fuel, and C represents background radiation. The decay rates r1 and r2 are 0.4 and 0.1, respectively.
#
#Step 2: Choose the more likely model.
#Perform a likelihood-ratio test with the two models, and compare the test statistic to a chi-squared distribution. 
#What's the probability that the peculiarities in the data are due to random chance? If you're using the statsmodels module, 
#you can easily access the log-likelihood of the regressions through the llf attribute of the fitted model.
#
#Step 3: Quantify the contamination.
#
#Calculate B/(A+B) to determine what percentage of the fuel supply was contaminated, 
#along with the associated uncertainty of the value. If you're using the statsmodels module, 
#you can use the bse attribute of the fitted models to get the errors of the parameters. If the contamination is more than 20%,
# you'll need to refuel before reaching your next destination.

import numpy as np
import pandas as pd
import scipy.stats as sps
import statsmodels.formula.api as smf

def fuel_decay(time_info, rate_info):
    return rate_info*np.exp(-rate_info*time_info)

def main():
    engine_data = pd.read_csv('engine.csv')
    
    #linear models
    model1 = smf.ols('N ~ fuel_decay(t,0.4)', data=engine_data).fit()
    model2 = smf.ols('N ~ decay(t,0.4) + decay(t,0.1)', data=engine_data).fit()

    # Perform the likelihood-ratio test
    D = 2*(model2.llf - model1.llf)
    print('{:.3e}'.format(sps.chi2.sf(D, 2)))
    # p-value is less than 0.05
    
    # Pull out relevant parameters and variances ('v' prefix)
    a, b = model2.params[1:]
    va, vb = model2.bse[1:]**2
    
    # Calculate percent contamination and uncertainty
    p = b/(a+b)
    vp = p**2 * ( va/(a**2) + (va+vb)/((a+b)**2) )
    print('{:.3f} ± {:.3f} %'.format(p, np.sqrt(vp)))
    
    # Check if it's reasonable for contamination
    # to be greater than 20%
    print(p + np.sqrt(vp) > 0.2)
    
    

if __name__ == "__main__":
    main()