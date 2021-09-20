import os


windows_os_name = "nt"

def clear_console() -> None:
    clr_consl_wind_command = "cls"
    clr_consl_other_sys_command = "clear"

    if (os.name == windows_os_name):
        execute_command(clr_consl_wind_command)
    else:
         execute_command(clr_consl_other_sys_command)


def execute_command(command: str) -> None:
    os.system(command)