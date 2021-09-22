import os


def clear_console():
    windows_os_name = "nt"
    clr_command_win = "cls"
    clr_command_other_os = "clear"

    if os.name == windows_os_name:
        execute_command(clr_command_win)
    else:
        execute_command(clr_command_other_os)


def execute_command(command: str):
    os.system(command)
