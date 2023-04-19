import constraint
from Lesson import Lesson
from Teacher import Teacher
from constraints import *
import functions
from qwe import *


lessons = functions.get_lessons()
days = functions.get_days()

# solution = normal(lessons, days, distribution_constraint, teachers_constraint, lessons_constraint)
# solution = min_conflicts(lessons, days, distribution_constraint, teachers_constraint, lessons_constraint)
solution = recursive_backtrack(lessons, days, distribution_constraint, teachers_constraint, lessons_constraint)
# solution = backtrack(lessons, days, distribution_constraint, teachers_constraint, lessons_constraint)

print(f"Solution:")
for key in solution:
   print(f"{key.name}: {solution.get(key)}")

