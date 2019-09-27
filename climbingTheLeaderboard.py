import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.


def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    print(scores)
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index)
    return rank_list

scores = [20,13,24]
alice = [1,2,3]

print(climbingLeaderboard(scores,alice))
