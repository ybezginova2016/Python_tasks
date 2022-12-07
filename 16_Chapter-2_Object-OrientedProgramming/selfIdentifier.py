# The self Identifier

"""
In Python, the self identifier plays a key role. In the context of the CreditCard
class, there can presumably be many different CreditCard instances, and each must
maintain its own balance, its own credit limit, and so on. Therefore, each instance
stores its own instance variables to reflect its current state.

Syntactically, self identifies the instance upon which a method is invoked. For
example, assume that a user of our class has a variable, my card, that identifies
an instance of the CreditCard class. When the user calls my card.get balance( ),
identifier self, within the definition of the get balance method, refers to the card
known as my card by the caller. The expression, self. balance refers to an instance
variable, named balance, stored as part of that particular credit card’s state.
"""

# The conclusion of the CreditCard class definition.
# These methods are indented within the class definition.

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'ProCreditBank')
        acnt        the acount identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in RSD)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

