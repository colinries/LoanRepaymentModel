#!usr/bin/env python3

import math


class Loan:
    """Store and represent a loan in a portfolio"""

    # Fundamental Methods

    def __init__(self, principal, minimumMonthlyPayment, interestRate, actualMonthlyPayment=0):
        self.principal = principal
        self.minimumMonthlyPayment = minimumMonthlyPayment
        self.interestRate = interestRate
        self.actualMonthlyPayment = actualMonthlyPayment

    def __repr__(self):
        return "<Principal: {} Interest: {} Minimum Payment: {}>".format(self.get_principal(),
                                                                         self.get_interestRate(),
                                                                         self.get_minimumMonthlyPayment())

    def __str__(self):
        return self.get_principal() + ' at ' + self.get_interestRate() + '%'

    # Predicates

    def __lt__(self, other):
        """Loan ordered by interest rate"""

        if type(self) != type(other):
            raise Exception('Incompatible argument to __lt__: ' + str(other))
        return self.get_interestRate() < other.get_interestRate()

    # Access Methods

    def get_principal(self):
        return self.principal

    def get_minimumMonthlyPayment(self):
        return self.minimumMonthlyPayment

    def get_actualMonthlyPayment(self):
        return self.actualMonthlyPayment

    def get_interestRate(self):
        return self.interestRate

    # Modifier Methods

    def set_MonthlyPayment(self, contribution):
        self.actualMonthlyPayment = contribution

    # Action Methods

    def NextMonthBalance(self):
        balance = (self.principal * math.exp(self.interestRate * (1/12))) - self.actualMonthlyPayment
        if balance <= 0:
            return self.principal
        return balance

