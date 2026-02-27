from colorama import init, Fore, Style

init(autoreset=True)


class Console:
    @staticmethod
    def info(message):
        print(Fore.CYAN + "📘 " + message)

    @staticmethod
    def success(message):
        print(Fore.GREEN + "📗 " + message)

    @staticmethod
    def warning(message):
        print(Fore.YELLOW + "📙 " + message)

    @staticmethod
    def error(message):
        print(Fore.RED + "📕 " + message)

    @staticmethod
    def input(message):
        return input(Fore.MAGENTA + "✏️ " + message + Style.RESET_ALL)