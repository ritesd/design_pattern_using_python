from __future__ import annotations
from abc import ABC, abstractmethod


class FlyBehavior:
    @abstractmethod
    def fly(self):
        pass


class QuackBehavior:
    @abstractmethod
    def quack(self):
        pass


class Ducks:
    def __init__(
        self, type_name, flyBehavior: FlyBehavior, quackBehavior: QuackBehavior
    ) -> None:
        self.type_name = type_name
        self._flyBehavior = flyBehavior
        self._quackBehavior = quackBehavior

    def swim(self):
        print(f"{self.type_name} can swim, well all Ducks can swim")

    @abstractmethod
    def display(self):
        pass

    @property
    def flyBehavior(self):
        return self._flyBehavior

    @property
    def quackBehavior(self):
        return self._quackBehavior

    @flyBehavior.setter
    def flyBehavior(self, flyBehavior: FlyBehavior) -> None:
        self._flyBehavior = flyBehavior

    @quackBehavior.setter
    def quackBehavior(self, quackBehavior: QuackBehavior) -> None:
        self._quackBehavior = quackBehavior

    def performFly(self) -> None:
        self.flyBehavior.fly()

    def performQuack(self) -> None:
        self.quackBehavior.quack()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I',m flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cant't fly")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    """docstring for ClassName"""

    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    """docstring for Squeak"""

    def qauck(self):
        print("Squeak")


class MallardDuck(Ducks):
    """docstring for MallardDuck"""

    def __init__(self, args=None):
        super(MallardDuck, self).__init__("MallardDuck", FlyWithWings(), Quack())
        self.display()

    def display(self):
        print("I am real Mallard Duck")


"""
    Now lets change the fly behaviour on the fly with below example
"""


class ModelDuck(Ducks):
    """docstring for ModelDuck"""

    def __init__(self):
        super(ModelDuck, self).__init__("ModelDuck", FlyNoWay(), Quack())
        self.display()

    def display(self):
        print("I'm model duck")


class FlyRocketPowered(FlyBehavior):
    """docstring for FlyRocketPowered"""

    def fly(self):
        print("I'm flying with Rocket")


def main():
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

    print("****")

    modelduck = ModelDuck()
    modelduck.performFly()
    modelduck.performQuack()

    modelduck.flyBehavior = FlyRocketPowered()

    print("dynamically set")

    modelduck.performFly()


if __name__ == "__main__":
    main()
