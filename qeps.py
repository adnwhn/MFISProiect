import random
import numpy as np
import time
import pickle


class QEPS:
    def __init__(self, num_variables, num_clauses, formula):
        self.num_variables = num_variables
        self.num_clauses = num_clauses
        self.formula = formula
        self.num_membranes = 10
        self.population_size = 40
        self.qubits = np.random.rand(self.population_size, self.num_variables) > 0.5

    def evaluate(self, solution):
        # Evalueaza o solutie data ca parametru
        score = 0
        for clause in self.formula:
            if any(solution[var - 1] if var > 0 else not solution[-var - 1] for var in clause):
                score += 1
        return score

    def update_qubits(self, qubit, fitness, best_fitness):
        # Functie care actualizeaza qubitii
        theta = np.pi / 4 if fitness > best_fitness else -np.pi / 4
        p_flip = 0.5 + theta / np.pi

        for i in range(self.num_variables):
            if random.random() < p_flip:
                qubit[i] = not qubit[i]
        return qubit

    def run(self):
        best_solution = None
        best_score = -1

        for generation in range(50):
            for i in range(self.population_size):
                solution = self.qubits[i]
                fitness = self.evaluate(solution)

                if fitness > best_score:
                    best_score = fitness
                    best_solution = solution

                self.qubits[i] = self.update_qubits(solution, fitness, best_score)

            print(f"Generatia {generation}, Scor: {best_score}/{self.num_clauses}")

        return best_solution


def measure_performance(func, *args):
    # Functie care masoara timpul de executie
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def load_formula_from_file(file_path):
    # Functie care preia exemplul de testare din fisierul pickle
    with open(file_path, 'rb') as f:
        formula = pickle.load(f)
    return formula


def run_tests(file_path, num_vars, num_clauses):
    formula = load_formula_from_file(file_path)

    qeps_solver = QEPS(num_vars, num_clauses, formula)
    qeps_result, qeps_time = measure_performance(qeps_solver.run)
    print("Solutie QEPS:", qeps_result, "\nTimp Execuție:", qeps_time, "secunde")


run_tests('sat_formula.pkl', num_vars=20, num_clauses=50)
