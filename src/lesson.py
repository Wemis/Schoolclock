class Lesson:
    name: str
    DURATION_MINUTES = 40

    def __init__(self, name: str) -> None:
        self.name = name


def to_list_lessons(lessons: list[str]) -> list[Lesson]:
    output_lessons = []

    for lesson in lessons:
        output_lessons.append(
            Lesson(
                lesson
            )
        )

    return output_lessons
