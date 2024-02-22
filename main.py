######################
# COSC 4368          #
# Adam Nelson-Archer #
######################


def forwardCheck(assignment, domains, constraints, var_assigned):
  updated_domains = {var: list(domains[var]) for var in domains}

  for constraint, vars_involved in constraints:
    # check if the constraint involves the variable that was just assigned
    if var_assigned in vars_involved:
      # Determine the number of unassigned variables involved in this constraint
      unassigned_vars = [var for var in vars_involved if var not in assignment]

      # Proceed only if there's exactly one unassigned variable left in the constraint
      # It is pretty much useless to run with more than 
      # 1 unassigned variable given these constraints
      if len(unassigned_vars) == 1:
        unassigned_var = unassigned_vars[0]  # The only unassigned variable
        for value in updated_domains[unassigned_var][:]:  # Iterate over a copy
          hypothetical_assignment = assignment.copy()
          hypothetical_assignment[unassigned_var] = value

          # Check if the constraint is satisfied with this hypothetical assignment
          if not constraint(hypothetical_assignment):
            updated_domains[unassigned_var].remove(value)  # Prune value if constraint fails

        if not updated_domains[unassigned_var]:  # If domain becomes empty, fail
          return None

  return updated_domains

def getLCV(var, assignment, domains, constraints):
  value_counts = []
  for value in domains[var]:
      new_assignment = assignment.copy()
      new_assignment[var] = value
      pruned_domains = forwardCheck(new_assignment, domains, constraints, var)

      if pruned_domains is not None:
          # Count how many options are left for the other variables
          options_left = sum(len(pruned_domains[v]) for v in pruned_domains if v not in new_assignment)
          value_counts.append((value, options_left))
      else:
          # If domain is pruned to nothing, consider this as least preferable
          value_counts.append((value, -1))

  # Sort by the number of options left, preferring higher counts (more options left)
  value_counts.sort(key=lambda item: -item[1])

  # Return the values in sorted order
  return [value for value, _ in value_counts]

def recursiveBacktracking(assignment, variables, domains, constraints, nva):
  if len(assignment) == len(variables):
      return assignment
  
  unassigned_vars = [var for var in variables if var not in assignment]
  var = unassigned_vars[0]
  # here we sort the domain of the unassigned value to prefer the optimal values
  least_constraining_values = getLCV(var, assignment, domains, constraints)
  
  for value in least_constraining_values:
      new_assignment = assignment.copy()
      new_assignment[var] = value
      nva[0] += 1
      pruned_domains = forwardCheck(new_assignment, domains, constraints, var)
      if pruned_domains is not None:
          result = recursiveBacktracking(new_assignment, variables, pruned_domains, constraints, nva)
          if result is not None:
              return result
  return None
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def runCSP():
  return

def main():
  variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
  domains = {var: list(range(1, 121)) for var in variables}
  assignment = {}
  constraints = [
    #(lambda x: x['A'] > x['B'] + x['C'], ['A', 'B', 'C']),
    (lambda x: x['A'] == x['B']**2 - x['C']**2, ['A', 'B', 'C']),
    (lambda x: x['E'] + x['F'] > x['B'], ['E', 'F', 'B']),
    (lambda x: x['D'] == x['B']**2 - 3 * x['A'], ['D', 'B', 'A']),
    (lambda x: (x['B'] - x['C']) ** 2 == x['E'] * x['F'] * x['C'] - 1861, ['B', 'C', 'E', 'F']),
    (lambda x: x['C'] + x['D'] + x['E'] + x['F'] < 120, ['C', 'D', 'E', 'F']),
    # Problem B constraints
    (lambda x: (x['G'] + x['I'])**3 == (x['H'] - x['A'] - 1)**2, ['G', 'I', 'H', 'A']),
    (lambda x: x['B'] * x['E'] * x['F'] == x['H'] * x['B'] - 200, ['B', 'E', 'F', 'H']),
    (lambda x: (x['C'] + x['I'])**2 == x['B'] * x['E'] * (x['G'] + 1), ['C', 'I', 'B', 'E', 'G']),
    (lambda x: x['G'] + x['I'] < x['E'], ['G', 'I', 'E']),
    (lambda x: x['D'] + x['H'] > 180, ['D', 'H']),
    (lambda x: x['J'] < x['H'] - x['C'] - x['G'], ['J', 'H', 'C', 'G']),
    (lambda x: x['J'] > x['B'] * x['G'] + x['D'] + x['E'] + x['G'], ['J', 'B', 'G', 'D', 'E']),
    # Problem C constraints
    (lambda x: x['K'] * x['L'] * x['M'] == x['B'] * (x['B'] + 5), ['K', 'L', 'M', 'B']),
    (lambda x: x['F']**3 == x['K']**2 * x['M']**2 * 10 + 331, ['F', 'K', 'M']),
    (lambda x: x['H'] * x['M']**2 == x['J'] * x['K'] - 20, ['H', 'M', 'J', 'K']),
    (lambda x: x['J'] + x['L'] == x['I'] * x['L'], ['J', 'L', 'I']),
    (lambda x: x['A'] + x['D'] + x['M'] == x['B'] * (x['F'] - 2), ['A', 'D', 'M', 'B', 'F'])
  ]


  # Example usage:
  numConstraints = 5  # Number of constraints to actually use
  numVariables = 6   # Number of variables to actually use
  nva = [0]  # Number of variable assignments tracker

  # Select a subset of constraints and variables based on the specified numbers
  print("selected constraints:", numConstraints)
  print("selected variables: ", variables[:numVariables])

  # find one solution for the given inputs
  solution = recursiveBacktracking(
    assignment, 
    variables[:numVariables], 
    domains, 
    constraints[:numConstraints], 
    nva
  )

  if solution is not None:
    print(f"Solution found: {solution}")
  else:
    print("No solution exists")
  print(f"\nNumber of variable assignments: {nva[0]}")

if __name__ == "__main__":
  main()