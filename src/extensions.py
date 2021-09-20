import os


def clear_сonsole():
    WINDOWS_OS_NAME = "nt"
    CLR_COMMAND_WIN = "cls"
    CLR_COMMAND_OTHER_OS = "clear"

    if (os.name == WINDOWS_OS_NAME):
        execute_сommand(CLR_COMMAND_WIN)
    else:
        execute_сommand(CLR_COMMAND_OTHER_OS)


def execute_сommand(command: str):
    os.system(command)
