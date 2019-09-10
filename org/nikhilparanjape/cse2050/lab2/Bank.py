class CreditCard:
    _account = ""
    _balance = ""
    _bank = ""
    _customer = ""
    _limit = ""

    def __init__(self, account, balance, bank, customer, limit):
        self._account = account
        self._balance = balance
        self._bank = bank
        self._customer = customer
        self._limit = limit

    def get_account(self):
        return self._account

    def get_balance(self):
        return self._balance

    def get_bank(self):
        return self._bank

    def get_customer(self):
        return self._customer

    def get_limit(self):
        return self._limit

    def make_payment(self, amount):
        self._balance -= amount
        acc_num = str(self.get_account())
        result = acc_num[-4:]

        print("Payment received for the account ending in '{}', your remaining balance is ${}, your limit is ${}".format(result,
                                                                                                             self.get_balance(),
                                                                                                             self.get_limit()))

    def charge(self, price):
        if (self._balance + price) <= self._limit:
            self._balance += price

            print("You were charged, your current balance is ${}".format(self.get_balance()))
            if self.get_balance() == self.get_limit():
                print("You have no more credit remaining. Please make a payment as soon as possible")

            return True

        else:
            print("Your purchase is will go over the limit, or your account is already over the limit")
            return False


class PredatoryCreditCard(CreditCard):
    _apr = 0

    def __init__(self, account, balance, bank, customer, limit, apr):
        self._apr = apr
        super(PredatoryCreditCard, self).__init__(account, balance, bank, customer, limit)

    def process_month(self):
        return "yep"

    def charge(self, price):
        if CreditCard.charge(price):
            print("Everything all good")


mycard = CreditCard(392173311124934, 0, "Citizens Bank", "Nikhil Paranjape", 20000)

mycard.charge(250)

print("Current balance: ${}".format(mycard.get_balance()))
