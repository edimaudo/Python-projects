#================
# Smart Rehabililtation
# A client of yours is Maha, a Physiotherapist who helps people build customized rehabilitation plans that fits their
# health conditions and abilities. Maha told you that it takes her a long time to build rehabilitation exercise
# plans for her customers since it varies according to the customer Age Category, Condition and No. of Exercises.
# So, she decided to reach out to your company to see if AI can make her job easier. You told her that she is
# lucky since this is a common AI problem, known as optimization, and you can help her by building a Genetic algorithm solution
#================

# Load libraries
import streamlit as st
import pandas as pd
import pygad
import numpy

st.title('Smart Rehabililtation')

#=================
# Sidebar
#=================
age_choice = st.sidebar.selectbox("Age Category", ["Adult", "Child"])
condition_choice = st.sidebar.selectbox("Condition Type", ["Brain Injury","Spinal Cord","Stroke"])
elbow_choice = st.sidebar.selectbox("Elbow Exercise", [1, 2])
upper_arm_choice = st.sidebar.selectbox("Upper Arm Exercise", [1, 2])
knee_leg_choice = st.sidebar.selectbox("Knee/Lower Leg Exercise", [1, 2])
wrist_choice = st.sidebar.selectbox("Wrist Exercise", [0, 1])
submit_button = st.sidebar.button("Submit")

#=================
# GA Logic
#=================

if age_choice == "Adult":
	age_option_choice = 1
else:
	age_option_choice = 2


if condition_choice == "Brain Injury":
	condition_option_choice = 1
elif condition_choice == "Spinal Cord":
	condition_option_choice = 2
else:
	condition_option_choice = 3

function_inputs_temp = [age_option_choice, condition_option_choice, elbow_choice, upper_arm_choice, knee_leg_choice, wrist_choice]
total = sum(function_inputs_temp)

function_inputs = []
for i in range(0,len(function_inputs_temp)-1):
	function_inputs.append(function_inputs_temp[i]/total)


desired_output = 1

def fitness_func(solution, solution_idx):
	output = numpy.sum(solution*function_inputs)
	fitness = 1.0 / (numpy.abs(output - desired_output) + 0.000001)
	return fitness

ga_instance = pygad.GA(num_generations=1000,
                       sol_per_pop=100,
                       num_genes=len(function_inputs),
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       mutation_type="random")

if submit_button:
	data_load_state = st.text('Running GA...')
	ga_instance.run()
	data_load_state.text('')
	st.pyplot(ga_instance.plot_result())
	solution, solution_fitness, solution_idx = ga_instance.best_solution()
	st.write("Parameters of the best solution : {solution}".format(solution=solution))
	st.write("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

	prediction = numpy.sum(numpy.array(function_inputs)*solution)
	st.write("Predicted output based on the best solution : {prediction}".format(prediction=prediction))



#=================
# GA Output
#=================
if submit_button:
	st.write("Your rehabilitation plan is ready! Your plan is presented below with these exercises per day. ")
