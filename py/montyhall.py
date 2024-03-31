from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian network structure
model = BayesianModel([('C', 'G'), ('H', 'G'), ('C', 'H')])

# Define conditional probability distributions (CPDs)
cpd_c = TabularCPD(variable='C', variable_card=3, values=[[1/3], [1/3], [1/3]])

cpd_h = TabularCPD(variable='H', variable_card=3, values=[[0, 0, 1, 1, 0, 1],
                                                          [0.5, 0, 0, 0, 1, 0],
                                                          [0.5, 1, 0, 0, 0, 0]],
                   evidence=['C'], evidence_card=[3])

cpd_g = TabularCPD(variable='G', variable_card=3, values=[[0, 1, 1, 1, 0, 0],
                                                          [0, 0, 0, 0, 0.5, 1],
                                                          [1, 0, 0, 0, 0.5, 0]],
                   evidence=['C', 'H'], evidence_card=[3, 3])

# Add CPDs to the model
model.add_cpds(cpd_c, cpd_h, cpd_g)

# Check if the model is valid
print("Model valid?", model.check_model())

# Perform inference using Variable Elimination
inference = VariableElimination(model)

# Calculate probability of winning the car given that the contestant chose door 1 and Monty opened door 3
query_result = inference.query(variables=['G'], evidence={'C': 0, 'H': 2})
print(query_result)
