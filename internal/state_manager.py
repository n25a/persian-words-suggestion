from internal import suggestor
from rich.console import Console
import os


console = Console()
clear = lambda: os.system('clear')
suggerstor_object = suggestor.Suggerstor()


def main_state() -> str:
    states = {
        "1": "start",
        "2": "exit",
        "3": "about",
    }

    console.print(
        "Select number: \n",
        style="bold blue",
        justify="left",
        width=40,
    )
    console.print(
        "1. Start",
        style="bold green",
        justify="left",
        width=40,
    )
    console.print(
        "2. Exit",
        style="bold red",
        justify="left",
        width=40,
    )
    console.print(
        "3. About\n",
        style="bold magenta",
        justify="left",
        width=40,
    )
    choice = input("Input:").encode('utf-8').decode('utf-8')
    state = states.get(choice, "start")

    return state

def about_state() -> str:
    clear()

    text = """
🫀  Thanks to use this program! 🫀
🫀  This program is created by Nima Mashhadi M. Reza (@n25a) 🫀
"""
    console.print(
        text,
        style="bold yellow",
        justify="center",
        width=400,
    )
    input("Press Enter to continue...")

    return "main"

def start_state() -> str:
    clear()
    states = {
        "1": "set_length",
        "2": "set_charector",
        "3": "not_set_charector",
        "4": "contains",
        "5": "not_contains",
        "6": "suggest",
        "7": "exit",
    }
    console.print(
        "Select number: \n",
        style="bold blue",
        justify="left",
        width=40,
    )
    console.print(
        "1. set length",
        style="bold green",
        justify="left",
        width=40,
    )
    console.print(
        "2. set charector",
        style="bold red",
        justify="left",
        width=40,
    )
    console.print(
        "3. not set charector",
        style="bold red",
        justify="left",
        width=40,
    )
    console.print(
        "4. contains",
        style="bold red",
        justify="left",
        width=40,
    )
    console.print(
        "5. not contains",
        style="bold magenta",
        justify="left",
        width=40,
    )
    console.print(
        "6. suggest",
        style="bold magenta",
        justify="left",
        width=40,
    )
    console.print(
        "7. exit\n",
        style="bold magenta",
        justify="left",
        width=40,
    )
    choice = input("Input:").encode('utf-8').decode('utf-8')
    state = states[choice]

    return state

def set_length_state() -> str:

    clear()
    console.print(
        "what's your charector length?\n",
        style="bold magenta",
        justify="left",
    )
    length = input("length:").encode('utf-8').decode('utf-8')
    suggerstor_object.set_length(int(length))

    return "start"

def set_charector_state() -> str:
    clear()
    console.print(
        "position of charector",
        style="bold magenta",
        justify="left",
    )
    position = input("position:").encode('utf-8').decode('utf-8')

    console.print(
        "charector",
        style="bold magenta",
        justify="left",
    )
    char = input("charector:").encode('utf-8').decode('utf-8')
    suggerstor_object.set(
        char=char,
        position=int(position)-1,
    )

    return "start"

def not_set_charector_state() -> str:
    clear()
    console.print(
        "position of charector",
        style="bold magenta",
        justify="left",
    )
    position = input("position:").encode('utf-8').decode('utf-8')

    console.print(
        "charector",
        style="bold magenta",
        justify="left",
    )
    char = input("charector:").encode('utf-8').decode('utf-8')
    suggerstor_object.not_set(
        char=char,
        position=int(position)-1,
    )

    return "start"

def contains_state() -> str:
    clear()
    console.print(
        "what is your charectors?\n",
        style="bold magenta",
        justify="left",
    )
    chars = input("Input (like: س ب ف غ):").encode("utf-8").decode("utf-8")
    print(chars)
    char_list = list(set(chars.split(" ")))

    if "" in char_list:
        char_list.remove("")
    if " " in char_list:
        char_list.remove(" ")

    suggerstor_object.contains(
        chars=char_list,
    )

    return "start"

def not_contains_state() -> str:
    clear()
    console.print(
        "what is your charectors?\n",
        style="bold magenta",
        justify="left",
    )
    chars = input("Input (like: س ب ف غ):").encode("utf-8").decode("utf-8")
    char_list = list(set(chars.split(" ")))

    if "" in char_list:
        char_list.remove("")
    if " " in char_list:
        char_list.remove(" ")

    suggerstor_object.not_contains(
        chars=char_list,
    )

    return "start"

def commands():
    state = "main"
    while True:
        clear()
        console.print(
            "💥 Welcome to the persian words suggestor! 💥\n",
            style="bold magenta",
            justify="center",
        )
        
        if state == "main":
            state = main_state()
        elif state == "start":
            state = start_state()
        elif state == "exit":
            break
        elif state == "about":
            state = about_state()
        elif state == "set_length":
            state = set_length_state()
        elif state == "set_charector":
            state = set_charector_state()
        elif state == "not_set_charector":
            state = not_set_charector_state()
        elif state == "contains":
            state = contains_state()
        elif state == "not_contains":
            state = not_contains_state()
        elif state == "suggest":
            suggerstor_object.suggest(console, clear)
            break
