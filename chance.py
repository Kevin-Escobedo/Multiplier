#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import random

def dice_roll(s:sides) -> int:
    '''Rolls an s sided die'''
    return random.randrange(1, s+1)

def coin_toss() -> bool:
    '''Tosses a coin; 1 is heads, 0 is tails'''
    return random.randint(0, 1)

