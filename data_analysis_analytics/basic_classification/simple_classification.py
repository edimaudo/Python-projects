# Here's our data, but with "woke up early" or "didn't wake up early" added.
days = [["ran", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["ran", "was tired", "woke up early"]]

# We're trying to predict whether or not the person was tired on this day.
new_day = ["ran", "didn't wake up early"]

def calc_y_probability(y_label, days):
  return len([d for d in days if d[1] == y_label]) / len(days)

def calc_ran_probability_given_y(ran_label, y_label, days):
  return len([d for d in days if d[1] == y_label and d[0] == ran_label]) / len(days)

def calc_woke_early_probability_given_y(woke_label, y_label, days):
  return len([d for d in days if d[1] == y_label and d[2] == woke_label]) / len(days)

denominator = len([d for d in days if d[0] == new_day[0] and d[2] == new_day[1]]) / len(days)
# Plug all the values into our formula.  Multiply the class (y) probability, and the probability of the x-values occuring given that class.
prob_tired = (calc_y_probability("was tired", days) * calc_ran_probability_given_y(new_day[0], "was tired", days) * calc_woke_early_probability_given_y(new_day[1], "was tired", days)) / denominator

prob_not_tired = (calc_y_probability("was not tired", days) * calc_ran_probability_given_y(new_day[0], "was not tired", days) * calc_woke_early_probability_given_y(new_day[1], "was not tired", days)) / denominator

# Make a classification decision based on the probabilities.
classification = "was tired"
if prob_not_tired > prob_tired:
  classification = "was not tired"
print("Final classification for new day: {0}. Tired probability: {1}. Not tired probability: {2}.".format(classification, prob_tired, prob_not_tired))