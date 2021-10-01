from dataclasses import dataclass, asdict, astuple

# frozen option: immutable
# Order option: ordering
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    sex: str = "man"

"""
void boilerplate code for data object
"""
if __name__ == "__main__":
    p1 = Person(name="lay", age=23)
    p2 = Person(name="lay", age=23)
    p3 = Person(name="greg", age=40, sex="woman")

    print(p1) # print
    print(p1 == p2) # Ture -> same value, another object
    print(p2 == p3) # False -> diffrent value, another object

    # raise exception because of immutable class
    #p2.age = 4

    # ease conversion to dict or tuple
    print(asdict(p1))
    print(astuple(p1))
