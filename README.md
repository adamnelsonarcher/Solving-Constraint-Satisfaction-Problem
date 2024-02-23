**Generalized Constraint Satisfaction**

This code attempts to solve a highly generalized constraint satisfaction problem by use of recursive backtracking and heavy domain pruning. 

The pruning is in two parts - forward looking, and sorting the domains in order of least to most constricting. 

Almost all of the program customization is contained in these lines::

    variables = ['A', 'B', 'C', ...]
    Vrange = (1,120)
    assignment = {}
    constraints = [...]
    numConstraints = 5  # Number of constraints to actually use
    numVariables = 6   # Number of variables to actually use

Variables are characters, assign them into the variables array.
Vrange is two numbers, you input the min and max for any value a variable can be.
Assignment{} is where the final results are stored, you can input values here if you wish to predetermine a variable value. 
Example usage: `assignment = {'A': 5, ‘B’: 5}`

To use this program, constraints need to be coded into the program. They are all in the format of :: `(lambda x: x['A'] == x['B']**2 - x['C']**2, ['A', 'B', 'C'])`. This is a tuple where the first part is the function/constraint itself and the second part names each variable that this constraint acts on.

You can give your variables a min/max by modifying `Vrange(_, _)`, where the first number is the min and the second is the max.
Currently the range for all variables is 1-120.

You can then decide how many of your constraints you want to use, and how many variables you select. If a constraint is selected that contains a nonexistent variable, it will not be applied, so you do not need to worry about input validation on that level.

There are two .py files here, “`LauncherVersion.py`” only exists to fulfill specific requirements I was given that this program needed to satisfy. It breaks the problem up into 3 parts, and solves for 4-5 variables at a time (all solutions), and uses those domains to create the next "level”of solutions. This is a good solution, but only works for constraints that are applied hierarchically.
