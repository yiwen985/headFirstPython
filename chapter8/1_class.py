class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        """类似于 toString"""
        return str(self.val)



# c = CountFromBy(100, 10)
c = CountFromBy()

c.increase()

print(c)