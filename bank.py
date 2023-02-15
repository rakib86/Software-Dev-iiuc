class MyBank:
    def __init__(self, balance):
        self._balance = balance
        self._min_withdraw = 500
        self._max_withdraw = 10000

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount < self._min_withdraw:
            return f"Cannot withdraw. Minimum amount to withdraw is {self._min_withdraw}"
        elif amount > self._max_withdraw:
            return f"Cannot withdraw. Maximum amount to withdraw is {self._max_withdraw}"
        elif amount > self._balance:
            return "Insufficient balance"
        else:
            self._balance -= amount
            return f"Withdrawal successful. Your new balance is {self._balance}"

    def deposit(self, amount):
        self._balance += amount
        return f"Deposit successful. Your new balance is {self._balance}"
