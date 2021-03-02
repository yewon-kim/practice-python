import numpy as np
import pandas as pd
import threading


class SyncTask:
    def __init__(self):
        pass

    def TaskA(self):
        price = np.random.randint(2000, 30000)
        buy_at = np.random.randint(2000, 30000)

        if price >= buy_at - 5:
            print('%s \t %s [매수]' % (price, buy_at))
        else:
            print('%s \t %s' % (price, buy_at))

        threading.Timer(1, self.TaskA).start()


def main():
    inst = SyncTask()
    inst.TaskA()


if __name__ == '__main__':
    main()

