class Lesson:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name