from extensions import clear_сonsole
import time
from types.lesson import Lesson


MINUTE = 1
go_home_message = "Go home!!!"


def run(lessons: list[Lesson]):
    # all constants in minutes
    DELAY = 1 * MINUTE
    BREAK_DURATION = 5 * MINUTE

    for i in range(len(lessons)):
        current_lesson = lessons[i].name
        next_lesson = get_next_lesson(lessons, i)
        start_lesson(current_lesson, next_lesson, DELAY)
        pause(BREAK_DURATION)


def get_next_lesson(lessons: list[Lesson], current_lesson: Lesson) -> Lesson:
    if current_lesson+1 == len(lessons):
        return go_home_message
    return lessons[current_lesson+1].name


def start_lesson(current_lesson: str, next_lesson: str, update_console_delay: int):
    for time_left in range(Lesson.DURATION_MINUTES * MINUTE, 0, -1):
        update_console(
            f"Time to end lesson {time_left / MINUTE} minutes\nCurrent lesson is {current_lesson}\nNext lesson is {next_lesson}",
            update_console_delay
        )


def pause(break_duration: int):
    print(f"🐠 Break {break_duration} minutes")
    time.sleep(break_duration)


def update_console(msg: str, delay: int):
    clear_сonsole()
    print(msg)
    time.sleep(delay)
