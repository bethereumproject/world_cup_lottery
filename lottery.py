import sys
import json
import urllib2
import random


def fetch_data():
    with open('users.txt', 'r') as f:
        return list(l.strip() for l in f.readlines())


def random_sample(users):
    total = 0
    for item in users:
        total += 1
        if 1 > random.random() * total:
            chosen = item
    return chosen


def draw(users):
    user = random_sample(users)
    users.remove(user)
    return user


if __name__ == '__main__':
    random.seed(sys.argv[1])

    users = fetch_data()

    winner = draw(users)
    second_prizes = list()

    for _ in range(50):
        second_prizes.append(draw(users))

    print(json.dumps(dict(winner=winner, second_prizes=second_prizes), sort_keys=True))
