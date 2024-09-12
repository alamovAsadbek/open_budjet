from colorama import init, Fore, Style

from main_files.decorator.decorator_func import log_decorator

init(autoreset=True)


@log_decorator
def color_text(text, color, is_bold=False):
    if color == 'green':
        text = f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    elif color == 'yellow':
        text = f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    elif color == 'blue':
        text = f"{Fore.BLUE}{text}{Style.RESET_ALL}"
    elif color == 'magenta':
        text = f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    elif color == 'cyan':
        text = f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    elif color == 'white':
        text = f"{Fore.WHITE}{text}{Style.RESET_ALL}"
    else:
        text = f"{Fore.WHITE}{text}{Style.RESET_ALL}"
        
    if is_bold:
        text = f'{Style.BRIGHT}{text}{Style.RESET_ALL}'
    return text
