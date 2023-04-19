import constraint


def normal(lessons, days, *args):
    problem = constraint.Problem()

    problem.addVariables(lessons, days)
    for arg in args:
        problem.addConstraint(arg)

    return problem.getSolution()


def min_conflicts(lessons, days, *args):
    problem = constraint.Problem(constraint.MinConflictsSolver())

    problem.addVariables(lessons, days)
    for arg in args:
        problem.addConstraint(arg)

    return problem.getSolution()


def recursive_backtrack(lessons, days, *args):
    problem = constraint.Problem(constraint.RecursiveBacktrackingSolver())

    problem.addVariables(lessons, days)
    for arg in args:
        problem.addConstraint(arg)

    return problem.getSolution()


def backtrack(lessons, days, *args):
    problem = constraint.Problem(constraint.BacktrackingSolver())

    problem.addVariables(lessons, days)
    for arg in args:
        problem.addConstraint(arg)

    return problem.getSolution()





