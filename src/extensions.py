import os


def clearConsole():
    WINDOWS_OS_NAME = "nt"
    CLR_COMMAND_WIN = "cls"
    CLR_COMMAND_OTHER_OS = "clear"

    if (os.name == WINDOWS_OS_NAME):
        executeCommand(CLR_COMMAND_WIN)
    else:
        executeCommand(CLR_COMMAND_OTHER_OS)


def executeCommand(command: str):
    os.system(command)
