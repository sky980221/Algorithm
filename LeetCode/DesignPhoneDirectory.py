# 379
def __init__(self, maxNumbers: int):
    self.avail = set(range(maxNumbers))


def get(self) -> int:
    if self.avail:
        return self.avail.pop()
    return -1


def check(self, number: int) -> bool:
    return number in self.avail


def release(self, number: int) -> None:
    self.avail.add(number)
