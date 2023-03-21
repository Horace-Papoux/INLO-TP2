"""Module that lets you manipulate a wallet"""


class InsufficientAmount(Exception):
    """Exception triggered when you try to spend more money than a wallet has"""

    pass


class Wallet(object):
    """Wallet class that lets your create a Wallet and add or spend money"""

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount, deferred=False):
        """Removes the specified amount of money from the current Wallet object"""
        if self.balance < amount:
            raise InsufficientAmount(f"Not enough available to spend {amount}")

        self.balance -= amount

    def add_cash(self, amount):
        """Adds the specified amount of money to the current Wallet object"""
        self.balance += amount

    def spend_money(self, amount, deferred=False):
        """Removes the specified amount of money from the current Wallet object"""
        if self.balance < amount:
            raise InsufficientAmount(f"Not enough available to spend {amount}")

        self.balance -= amount
