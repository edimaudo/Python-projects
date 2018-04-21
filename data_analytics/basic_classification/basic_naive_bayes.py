# Here's a running history for the past week.
# For each day, it contains whether or not the person ran, and whether or not they were tired.
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

# Let's say we want to calculate the odds that someone was tired given that they ran, using bayes' theorem.
# This is P(A).
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B).
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A).
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was tired"])

# Now we can calculate P(A|B).
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran

print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))