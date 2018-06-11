import pulp

# We are trying to maximize output
production = pulp.LpProblem('Production planning', pulp.LpMaximize)

# Our decision variables are continuous and >= 0
chairs = pulp.LpVariable('chairs', 0)
tables = pulp.LpVariable('tables', 0)

# We want to maximize production
z = pulp.LpVariable('z', 0)
production += z == chairs + tables
production.setObjective(z)

# Resources used for each product can't exceed what's available
production += 2*chairs + 1*tables <= 6 # labor
production += 1*chairs + 2*tables <= 6 # lumber

# Solving the model
assert production.solve() == pulp.LpStatusOptimal

print 'Objective value: ', pulp.value(z)
print 'Number of chairs:', pulp.value(chairs)
print 'Number of tables:', pulp.value(tables)