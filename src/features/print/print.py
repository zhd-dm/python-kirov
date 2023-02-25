from termcolor import colored


class Print:
    def print_info(self, message: str):
        print(colored(
            f"""
            {message}
            """,
            'cyan'))

    def print_success(self, message: str):
        print(colored(f"""
            ------ SUCCESS ----------------------------------------------------------- SUCCESS ------
                {message}
            """, 'green'
        ))

    def print_error(self, error: Exception):
        print(colored(f"""
            ------ ERROR --------------------------------------------------------------- ERROR ------
            !!!!! {error}                                                                       !!!!!
            -----------------------------------------------------------------------------------------
            """, 'red'
        ))