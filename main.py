import random
import math

def monte_carlo(count):
    ''' 円周率をモンテカルロ法で調べるプログラム
        countは試行回数
    '''
    ok = 0
    for _ in range(count):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            ok += 1
    return 4 * ok / count

print('   100の場合{0}'.format(monte_carlo(100)))
print('  1000の場合{0}'.format(monte_carlo(1000)))
print(' 10000の場合{0}'.format(monte_carlo(10000)))
print('100000の場合{0}'.format(monte_carlo(100000)))
