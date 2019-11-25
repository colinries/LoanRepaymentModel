#!usr/bin/env python3

import math


class Loan:
    """Store and represent a loan in a portfolio

    Assumes fixed interest rate and fixed minimum monthly payment
    """

    # Fundamental Methods

    def __init__(self, principal, minimumMonthlyPayment, interestRate, actualMonthlyPayment=0,
                 paymentSchedule=dict()):
        self.principal = principal
        self.minimumMonthlyPayment = minimumMonthlyPayment
        self.interestRate = interestRate
        self.actualMonthlyPayment = actualMonthlyPayment
        self.paymentSchedule = paymentSchedule

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

    def get_paymentSchedule(self):
        assert self.paymentSchedule == {}, 'Payment schedule not populated'
        return self.paymentSchedule

    def get_NextMonthsBalance(self):
        """Calculate the loan balance at the beginning of the next monthly pay period"""
        balance = (self.principal * math.exp(self.interestRate * (1/12))) - self.actualMonthlyPayment
        if balance <= 0:
            return 0
        return balance

    # Modifier Methods

    def set_MonthlyPayment(self, contribution):
        """Set the monthly payment amount. Return extra contribution to portfolio

        Pairs with Portfolio.DistributePayment()"""
        if contribution >= self.principal:
            self.actualMonthlyPayment = self.principal
            return contribution - self.principal
        self.actualMonthlyPayment = contribution
        return 0

    def set_PaymentSchedule(self, schedule):
        self.paymentSchedule = schedule

    # Action Methods

    def makeMonthlyPayment(self):
        self.principal = self.get_NextMonthsBalance()



