from render import *
from types.lesson import Lesson

MINUTE = 60
go_home_message = "Go home!!!"


def run(lessons: list[Lesson]):
    # all constants in minutes
    delay = 1 * MINUTE
    break_duration = 5 * MINUTE

    for lesson in range(len(lessons)):
        current_lesson = lessons[lesson].name
        next_lesson = get_next_lesson(lessons, lesson)
        start_lesson(current_lesson, next_lesson, delay)
        pause(break_duration)


def get_next_lesson(lessons: list[Lesson], current_lesson: int) -> str:
    if current_lesson + 1 == len(lessons):
        return go_home_message
    return lessons[current_lesson + 1].name


def start_lesson(current_lesson: str, next_lesson: str, update_console_delay: int):
    for time_left in range(Lesson.DURATION_MINUTES * MINUTE, 0, -1):
        update_console(
            f"Time to end lesson {time_left / MINUTE} minutes\nCurrent lesson is {current_lesson}\nNext lesson is {next_lesson}",
            update_console_delay
        )


def pause(break_duration: int):
    print(f"🐠 Break {break_duration} minutes")
    time.sleep(break_duration)
