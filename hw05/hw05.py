def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    
    incorrect_password = []
    def withdraw(amount, user):
        nonlocal balance
        if len(incorrect_password) == 3:
            return('Your account is locked. Attempts: ' + str(incorrect_password))
        if user != password:
            incorrect_password.append(user)
            return 'Incorrect password'
        elif amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
     
    return withdraw
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    ret = withdraw(0, old_password)

    def withdraw_joint(amount, secondary_password):
        if secondary_password == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, secondary_password)

    return ret if type(ret) is str else withdraw_joint

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        balance_and_price_difference = self.balance - self.price
        is_item_in_stock = True if (self.stock > 0) else False
        is_enough_money_inputted = True if (balance_and_price_difference >= 0) else False

        if is_item_in_stock and is_enough_money_inputted:
            self.balance = 0
            self.stock -= 1

            if balance_and_price_difference == 0:
                return 'Here is your ' + str(self.item) + '.'
            return 'Here is your ' + str(self.item) + ' and $' + str(balance_and_price_difference) + ' change.'
        
        elif is_item_in_stock:
            return 'You must deposit $' + str(-balance_and_price_difference) + ' more.'
        
        return 'Machine is out of stock.'

    def restock(self, amount):
        self.stock += amount
        return 'Current ' + str(self.item) + ' stock: ' + str(self.stock)

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'

        self.balance += amount
        return 'Current balance: $' + str(self.balance)

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    def __init__(self, inputted_object):
        self._object = inputted_object

    def ask(self, caller_input, *args):
        # store string after initial please
        method_requested = caller_input[7:]
        
        if 'please' not in caller_input.split():
            return 'You must learn to say please first.'
        elif hasattr(self._object, method_requested):
            return getattr(self._object, method_requested)(*args)
        return 'Thanks for asking, but I know not how to ' + method_requested

