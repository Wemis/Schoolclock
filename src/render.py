import time

from extensions import clear_console


def update_console(msg: str, delay: int):
    clear_console()
    print(msg)
    time.sleep(delay)
