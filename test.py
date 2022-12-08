import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the simulation
num_criminals = 2
probabilities = [0.3, 0.4]
payoff_matrix = [[[10, 0], [0, 5]], [[5, 0], [0, 10]]]

# Define a function to calculate the payoffs for each criminal
def calculate_payoffs(probabilities, payoff_matrix):
    payoffs = []
    for i in range(num_criminals):
        criminal_probability = probabilities[i]
        criminal_payoff = 0
        for j in range(num_criminals):
            opponent_probability = probabilities[j]
            criminal_payoff += payoff_matrix[i][j][int(opponent_probability > criminal_probability)]
        payoffs.append(criminal_payoff)
    return payoffs

# Initialize the list of payoffs for each criminal
payoffs = []

# Iterate over each criminal and calculate their optimal probability
for i in range(num_criminals):
    # Calculate the payoffs for each criminal based on their current probabilities
    current_payoffs = calculate_payoffs(probabilities , payoff_matrix)
    payoffs.append(current_payoffs)

    # Calculate the optimal probability for the current criminal
    criminal_probabilities = probabilities[i]
    max_payoff = max(current_payoffs)
    optimal_probability = criminal_probabilities[current_payoffs.index(max_payoff)]

    # Update the probabilities of the current criminal
    probabilities[i] = optimal_probability

# Visualize the results
plt.plot(payoffs)
plt.show()
