from pomegranate import *
# say library doesnt work. cos it literally doesnt. sorry i couldnt fix it
# Define the Bayesian network structure
guest = Node(DiscreteDistribution({
    "A": 1./3,
    "B": 1./3,
    "C": 1./3
}), name="guest")

prize = Node(DiscreteDistribution({
    "A": 1./3,
    "B": 1./3,
    "C": 1./3
}), name="prize")

monty = Node(ConditionalProbabilityTable(
    [["A", "A", "A", 0.0],
     ["A", "A", "B", 0.5],
     ["A", "A", "C", 0.5],
     ["A", "B", "C", 1.0],
     ["A", "C", "B", 1.0],
     ["B", "A", "C", 1.0],
     ["B", "B", "B", 0.0],
     ["B", "B", "A", 0.5],
     ["B", "B", "C", 0.5],
     ["B", "C", "A", 1.0],
     ["C", "A", "B", 1.0],
     ["C", "B", "A", 1.0],
     ["C", "C", "C", 0.0],
     ["C", "C", "A", 0.5],
     ["C", "C", "B", 0.5]],
    [guest, prize]), name="monty")

# Create the Bayesian network
network = BayesianNetwork()
network.add_states(guest, prize, monty)
network.add_edge(guest, monty)
network.add_edge(prize, monty)
network.bake()

# Simulate the Monty Hall problem
num_trials = 100000
wins = 0

for _ in range(num_trials):
    # Set initial states
    guest_state = np.random.choice(["A", "B", "C"], p=[1./3, 1./3, 1./3])
    prize_state = np.random.choice(["A", "B", "C"], p=[1./3, 1./3, 1./3])
    network.predict(guest.array_index(guest_state), prize.array_index(prize_state))

    # Guest's initial choice
    guest_choice = guest_state

    # Monty opens a door
    monty_open = monty.value

    # Guest switches their choice
    new_choice = "A" if (guest_choice != "A" and monty_open != "A") else \
                  "B" if (guest_choice != "B" and monty_open != "B") else "C"

    # Check if the guest wins
    if new_choice == prize_state:
        wins += 1

# Print the result
print(f"Wins by switching: {wins / num_trials * 100:.2f}%")