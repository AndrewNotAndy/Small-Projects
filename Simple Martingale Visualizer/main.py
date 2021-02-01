from matplotlib import pyplot as plt
import random

runs = 0
bal = 10000
baseBet = 100
amountHistory = []
runHistory = []
win = False
multiplier = 1


def bet(b):
    global bal
    global win
    global multiplier
    if random.randint(1, 2) % 2 == 0:
        bal += b
        win = True
        #multiplier *= 2

    else:
        bal -= b
        win = False
        #multiplier = 1


while bal > 0:
    # if win:
    #     bet(baseBet)
    # else:
    #     bet(baseBet * multiplier)
    bet(baseBet/2)
    runs += 1
    amountHistory.append(bal)
    runHistory.append(runs)


plt.plot(runHistory, amountHistory)

plt.show()
