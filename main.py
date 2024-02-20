# Combined list of all constraints
constraints = [
    # Problem A constraints
        (lambda assignment: assignment['A'] == assignment['B']**2 - assignment['C']**2, ['A', 'B', 'C']),
        (lambda assignment: assignment['E'] + assignment['F'] > assignment['B'], ['E', 'F', 'B']),
        (lambda assignment: assignment['D'] == assignment['B']**2 - 3 * assignment['A'], ['D', 'B', 'A']),
        (lambda assignment: (assignment['B'] - assignment['C']) ** 2 == assignment['E'] * assignment['F'] * assignment['C'] - 1861, ['B', 'C', 'E', 'F']),
        (lambda assignment: assignment['C'] + assignment['D'] + assignment['E'] + assignment['F'] < 120, ['C', 'D', 'E', 'F']),
        # Problem B constraints
        (lambda assignment: (assignment['G'] + assignment['I'])**3 == (assignment['H'] - assignment['A'] - 1)**2, ['G', 'I', 'H', 'A']),
        (lambda assignment: assignment['B'] * assignment['E'] * assignment['F'] == assignment['H'] * assignment['B'] - 200, ['B', 'E', 'F', 'H']),
        (lambda assignment: (assignment['C'] + assignment['I'])**2 == assignment['B'] * assignment['E'] * (assignment['G'] + 1), ['C', 'I', 'B', 'E', 'G']),
        (lambda assignment: assignment['G'] + assignment['I'] < assignment['E'], ['G', 'I', 'E']),
        (lambda assignment: assignment['D'] + assignment['H'] > 180, ['D', 'H']),
        (lambda assignment: assignment['J'] < assignment['H'] - assignment['C'] - assignment['G'], ['J', 'H', 'C', 'G']),
        (lambda assignment: assignment['J'] > assignment['B'] * assignment['G'] + assignment['D'] + assignment['E'] + assignment['G'], ['J', 'B', 'G', 'D', 'E']),
        # Problem C constraints
        (lambda assignment: assignment['K'] * assignment['L'] * assignment['M'] == assignment['B'] * (assignment['B'] + 5), ['K', 'L', 'M', 'B']),
        (lambda assignment: assignment['F']**3 == assignment['K']**2 * assignment['M']**2 * 10 + 331, ['F', 'K', 'M']),
        (lambda assignment: assignment['H'] * assignment['M']**2 == assignment['J'] * assignment['K'] - 20, ['H', 'M', 'J', 'K']),
        (lambda assignment: assignment['J'] + assignment['L'] == assignment['I'] * assignment['L'], ['J', 'L', 'I']),
        (lambda assignment: assignment['A'] + assignment['D'] + assignment['M'] == assignment['B'] * (assignment['F'] - 2), ['A', 'D', 'M', 'B', 'F'])
]

def check_constraints(assignments, mode):
    # Determine the range of constraints to check based on the mode
    if mode == 'A':
        constraints_to_check = constraints[0:5] 
    elif mode == 'B':
        constraints_to_check = constraints[0:12] 
    elif mode == 'C':
        constraints_to_check = constraints[0:17] 
    else:
        return None
    
    # Iterate over the specified constraints
    for constraint, involved_vars in constraints_to_check:
        # Extract only the assignments for the involved variables
        sub_assignments = {var: assignments[var] for var in involved_vars}
        print(f"Checking constraint with variables: {sub_assignments}")
        result = constraint(assignments)  
        print(f"Constraint result: {result}")
        if not result:
            return False  # Stop checking further if any constraint fails
    return True  # All constraints passed


def main():
    mode = 'A'
    assignments = {chr(65 + i): 1 for i in range(13)}  # A to M

    result = check_constraints(assignments, mode)
    print(f"Problem {mode} constraints satisfied: {result}")

if __name__ == "__main__":
    main()