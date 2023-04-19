import functions

lessons = functions.get_lessons()
days = functions.get_days()


def get_teachers(li):
    pass


def distribution_constraint(*args):
    unique_count = [0, 0, 0, 0, 0]
    for arg in args:
        unique_count[int(arg) - 1] += 1

    if max(unique_count) - min(unique_count) > 1:
        return False

    return True


def teachers_constraint(*args):
    args = list(args)

    lessons_day = []
    for day in days:
        indices = [index for index, value in enumerate(args) if value == day]
        lessons_day.append(indices)

    teachers_days = []
    for day in lessons_day:
        teachers = []

        for lesson_index in day:
            lesson = lessons[lesson_index]
            teachers.append(lesson.teacher.name)

        teachers_days.append(teachers)


    for teachers in teachers_days:
        if len(teachers) > len(set(teachers)):
            return False

    return True


def lessons_constraint(*args):
    args = list(args)

    lessons_day = []
    for day in days:
        indices = [index for index, value in enumerate(args) if value == day]
        lessons_day.append(indices)

    lessons_days = []
    for day in lessons_day:
        subjects = []

        for lesson_index in day:
            lesson = lessons[lesson_index]
            subjects.append(lesson.name)

        lessons_days.append(subjects)

    for subj in lessons_days:
        if len(subj) > len(set(subj)):
            return False

    return True


