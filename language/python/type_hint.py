from typing import TypedDict
from datetime import datetime


class Coupon(TypedDict):
    """
    PEP 589 TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys
    Support Python 3.8
    """
    name: str
    created: datetime
    expired: datetime


coupon = Coupon(name='11', created=datetime.now(), expired=datetime.now())
print(coupon)


def print_score(name: str, score: int) -> None:
    now: datetime = datetime.now()
    print(f'{now} score {score} of {name}')


print_score('Flynn', 88)


