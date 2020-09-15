# coding: utf-8

class Foo(object):
    pass


class Bar(object):
    pass


v = [item() for item in [Foo, Bar]]
print(v)
