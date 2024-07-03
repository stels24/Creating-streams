import time
from threading import Thread


def num(n):
    for a in range(1, 11):
        time.sleep(1)
        print(a)


def chars():
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for a in ch:
        time.sleep(1)
        print(a)


thr_one = Thread(target=num, args=(10,))
thr_two = Thread(target=chars)

thr_one.start()
thr_two.start()

thr_one.join()
thr_two.join()