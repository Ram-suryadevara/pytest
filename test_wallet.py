import os
import pytest


class wallet:
    def add_cash(self, earned):
        self.earned = earned
        return self.earned

    def spent_cash(self, spent):
        self.spent = spent
        return self.spent

    def balance(self):
        balance = self.earned - self.spent
        return balance


ls_count = [(40, 10, 30), (60, 10, 50), (70, 30, 40), (50, 25, 30)]


@pytest.mark.parametrize(('earned', 'spent', 'expected'), ls_count)
def test_transaction(earned, spent, expected):
    my_wallet = wallet()
    my_wallet.add_cash(earned)
    my_wallet.spent_cash(spent)
    assert my_wallet.balance() == expected


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
