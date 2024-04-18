import time
import pickle


def is_satisfied(formula, assignment):
    # Verifica daca o anumita asignare a variabilelor satisface toate clauzele din formula
    for clause in formula:
        if not any((var > 0 and assignment[abs(var)] == True) or
                   (var < 0 and assignment[abs(var)] == False) for var in clause):
            return False
    return True


def solve_sat(formula, variables, index=0, assignment=None):
    # Functia de backtracking genereaza toate combinatiile posibile de True si False pentru toate variabilele
    if assignment is None:
        assignment = {}

    if index == len(variables):
        # Daca a ajuns la finalul listei de variabile, se verifica formula
        if is_satisfied(formula, assignment):
            return [assignment.get(v, False) for v in variables]  # Returnăm valorile ca o listă de booleeni
        else:
            return False

    # Incearca sa seteze variabila curenta la True
    assignment[variables[index]] = True
    result = solve_sat(formula, variables, index + 1, assignment)
    if result:
        return result

    # Incearca sa seteze variabila curenta la False
    assignment[variables[index]] = False
    result = solve_sat(formula, variables, index + 1, assignment)
    if result:
        return result

    # Sterge asignarea pentru backtracking
    del assignment[variables[index]]
    return False


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
    variables = list(range(1, num_vars + 1))

    bt_result, bt_time = measure_performance(solve_sat, formula, variables)
    print("Backtracking Solutie:", bt_result, "Timp Executie:", bt_time, "secunde")


num_vars = 20
num_clauses = 50

run_tests('sat_formula.pkl', num_vars, num_clauses)
