# Title: Project
# Description: Project for the course of Analysis and Synthesis of Algorithms
# Author: Maria Ramos, 105875 Guilherme Campos, 106909

import time
from pulp import LpProblem, LpVariable, LpMaximize, LpInteger, lpSum, GLPK, value

# Start the timer
start_time = time.time()

# Read the number of toys, number of special packages, and maximum number of toys that can be produced per day
n, p, max_toys = map(int, input().split())

# Initialize the problem
prob = LpProblem("MaximizeProfit", LpMaximize)

# Create a list for toys and their profits and production capacities
toys = []
profits = {}
capacities = {}

for i in range(1, n+1):
    profit, capacity = map(int, input().split())
    toys.append(i)
    profits[i] = profit
    capacities[i] = capacity

# Create a list for special packages and their profits
packages = []
package_profits = {}
package_toys = {}

for i in range(1, p+1):
    toy1, toy2, toy3, profit = map(int, input().split())
    packages.append(i)
    package_profits[i] = profit
    package_toys[i] = [toy1, toy2, toy3]

# Create the decision variables
toy_vars = LpVariable.dicts("Toy", toys, 0, None, LpInteger)
package_vars = LpVariable.dicts("Package", packages, 0, None, LpInteger)

# Add the objective function to the problem
prob += lpSum([profits[i]*toy_vars[i] for i in toys]) + lpSum([package_profits[i]*package_vars[i] for i in packages]), "Total Profit"

# Add the constraints to the problem
for i in toys:
    prob += toy_vars[i] + lpSum([package_vars[j] for j in packages if i in package_toys[j]]) <= capacities[i], f"Capacity_{i}"

prob += lpSum([toy_vars[i] for i in toys]) + 3*lpSum([package_vars[i] for i in packages]) <= max_toys, "MaxToys"

# Solve the problem
prob.solve(GLPK(msg=0))

# Print the results
print(value(prob.objective))

# Stop the timer and print the execution time
end_time = time.time()
execution_time = (end_time - start_time)  # Convert to milliseconds
print(f"Execution time: {execution_time:.3f} s")