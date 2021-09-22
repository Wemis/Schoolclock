import time

from lesson import Lesson
from renderer import *

MINUTE = 60
go_home_message = "Go home!!!"


def start(lessons: list[Lesson]) -> None:
    delay = MINUTE
    break_duration = 5 * MINUTE

    for curr_lesson_by_number in range(len(lessons)):
        current_lesson = lessons[curr_lesson_by_number].name
        next_lesson = get_next_lesson(lessons, curr_lesson_by_number)

        start_lesson(current_lesson, next_lesson, delay)
        pause(break_duration)


def get_next_lesson(lessons: list[Lesson], current_lesson: int) -> str:
    if current_lesson + 1 == len(lessons):
        return go_home_message
    return lessons[current_lesson + 1].name


def start_lesson(current_lesson: str, next_lesson: str, update_console_delay: int) -> None:
    for time_left in range(Lesson.DURATION_MINUTES * MINUTE, 0, -1):
        render_msg(
            f"Time to end lesson {round(time_left / MINUTE, 2)} minutes\n"
            f"Current lesson is {current_lesson}\n"
            f"Next lesson is {next_lesson}"
        )
        time.sleep(update_console_delay)


def pause(break_duration: int) -> None:
    render_msg(f"🐠 Break {break_duration} minutes")
    time.sleep(break_duration)
