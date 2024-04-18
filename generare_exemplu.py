import numpy as np
import pickle


def generate_sat_formula(num_vars, num_clauses):
    formula = []
    for _ in range(num_clauses):
        # Genereaza 3 variabile aleatorii per clauza negative sau pozitive
        clause = np.random.choice(range(1, num_vars + 1), 3, replace=False) * np.random.choice([-1, 1], 3)
        formula.append(clause.tolist())
    return formula


def save_formula_to_file(formula, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(formula, f)


num_vars = 20
num_clauses = 50  #
formula = generate_sat_formula(num_vars, num_clauses)
file_path = 'sat_formula.pkl'
save_formula_to_file(formula, file_path)
