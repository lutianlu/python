# from functools import wraps


# def inject(func):
#     @wraps(func)
#     def wrap(self, **kwargs):
#         self.__dict__ = kwargs
#         return func(self, **kwargs)
#     return wrap


# class Test:

#     @inject
#     def __init__(self, x, y):
#         pass


# t = Test(x=6, y=9)
# print(t.__dict__)


# class x(dict):

#     def __init__(self,  **kwargs):
#         super().__init__(self,  **kwargs)
#         self.__dict__ = self
#         print(self.__dict__, type(self))


# y = x(x=7, y=8)
# y['z'] = 9
# print(y.x, y.y, y.__dict__)


from time import time, sleep
from contextlib import ContextDecorator


class Timed:

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time()
        cost = self.end - self.start
        print(f'Cost: {cost}')


class Timed2(ContextDecorator):

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time()
        cost = self.end - self.start
        print(f'Cost: {cost}')


with Timed():
    sleep(2)


@Timed2()
def f():
    sleep(2)


f()
