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
import numpy as np

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
else if condition_choice == "Spinal Cord":
	condition_option_choice = 2
else:
	condition_option_choice = 3

function_input
desired

# Best rehabilitation
# exercise(s) that maximize your fitness function and output a complete plan for each body parts (elbow,
# upper arm, knee/lower leg and wrist). Each main rehabilitation plan should contain at least one exercise
# for (elbow, upper arm, and knee/lower leg) and a maximum of two exercises, while the wrist may contain
# no exercise or up to one exercise per plan.
# Your fitness function includes three parameters; Age Category, Condition Type and No. of Exercises, where
# Age Category and No. of Exercises are equally important but as half important as Condition Type. Your
# fitness function can be designed as weighted sum and importance of factors can be encoded as weights wi in
# the fitness function, where Σ	�� = 1.


#=================
# GA Output
#=================
st.write("Your rehabilitation plan is ready! Your plan is presented below with these exercises per day. ")
