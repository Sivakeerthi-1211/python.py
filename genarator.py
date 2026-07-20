def gen():
    yield 10
    yield 20
    yield 30
    yield 40
d = gen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))