# coding: utf-8

class Test(object):

    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b
    #
    # def test(self):
    #     print("{}的分数是{}".format(self.a, self.b))

    def __call__(self, a):
        print("计算工资")
        s = a*12
        d = a//22.5
        return dict(s=s, d=d)


a = Test()
print(a(24))
