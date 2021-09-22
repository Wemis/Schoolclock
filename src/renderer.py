from rich import print as printf

from extensions import clear_console


def render_msg(msg: str):
    clear_console()
    printf(f"[bold magenta]{msg}")
