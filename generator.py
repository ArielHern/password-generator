import string
from random import choice


class Password:
    """
    A simple password generator class
    """

    def __init__(self):
        self.chars_nums = string.ascii_letters + string.digits
        self.special_char = string.punctuation

    def simplePass(self):
        """
        a simple password generator can be memorize
        """
        selector = self.chars_nums
        password = ''.join(choice(selector) for i in range(8))

        return password

    def strongPass(self):
        """
        robust password
        """
        selector = self.chars_nums + self.special_char
        password = ''.join(choice(selector) for i in range(15))

        return password

    def superStrongPass(self):
        """
        root or admin password very secure
        """
        selector = self.chars_nums + self.special_char
        password = ''.join(choice(selector) for i in range(30))

        return password
