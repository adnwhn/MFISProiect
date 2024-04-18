import pickle


def load_and_print_formula(file_path):
    # Functie care incarca exemplul de testare si il afiseaza in consola
    with open(file_path, 'rb') as f:
        formula = pickle.load(f)

    print("Formula SAT din fisierul pickle:")
    for clause in formula:
        print(clause)


file_path = 'sat_formula.pkl'
load_and_print_formula(file_path)
