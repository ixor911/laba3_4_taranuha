import json
from Lesson import Lesson
from Teacher import Teacher


def get_data_json() -> dict:
    return json.load(open("data.json", 'r'))


def get_lessons() -> list:
    data = get_data_json()
    lessons = []
    for lesson in data.get('lessons'):
        lessons.append(Lesson(lesson.get('lesson'), Teacher(lesson.get('teacher'))))

    return lessons


def get_days() -> list:
    return get_data_json().get('days')



