"""
SUMMER IS COMMING - 'Tame of Thrones' , A coding challenge for GeekTrust.

Problem 2 - ( Breaker of Chains ) : The other kingdoms in the Universe also
yearn to be the ruler of Southeros and war is imminent! The High Priest of
Southeros intervenes and is trying hard to avoid a war and he suggests a ballot
system to decide the ruler.

This module solves the second problem using code written in python3 adhereing
to PEP8 Coding Guidelines and Test Driven Development.

"""

import sys
import re
import os
from random import *
import random
from problem1 import *


def gen_msg_list():
    with open('msg.txt', 'r') as f, open('msg_list.txt', 'w') as fo:
        for line in f:
            fo.write(line.replace('"', '').replace("'", "").replace(".", ""))
    s = open('msg_list.txt')
    msg_list = s.read().strip().split(',\n')
    return msg_list


msg_list = gen_msg_list()


def gen_random_msg():
    return random.choice(msg_list)


def add_to_ballot(sender, reciever, ballot):
    ballot.append([sender, reciever, gen_random_msg()])
    return ballot


def pick_random(n, ballot):
    msgs = []
    for i in range(n):
        random_int = randint(0, len(ballot)-1)
        msgs.append(ballot[random_int])
        ballot.remove(ballot[random_int])
    return msgs


def find_alliance(msgs):
    alliances = []
    for each in msgs:
        if decrypt_secret_msg(each[1], each[2]):
            alliances.append([each[0], each[1]])
    return alliances


def find_ruler(alliances, competitors):
    ruler = []
    maxx = 0
    msg_list = gen_msg_list()
    for each in competitors:
        count = 0
        for alliance in alliances:
            if alliance[0] == each:
                count += 1
        if count > maxx:
            ruler = []
            maxx = count
            ruler.append(each)
        elif count == maxx:
            ruler.append(each)
    return ruler


def break_tie(ruler):
    competitors = ruler
    breaker_of_chains(competitors)


def breaker_of_chains(competitors):
    ballot = []
    kings = ["LAND", "WATER", "ICE",
             "AIR", "FIRE"]
    for sender in competitors:
        for reciever in kings:
            if reciever not in competitors:
                add_to_ballot(sender, reciever, ballot)
    msgs = pick_random(6, ballot)
    alliances = find_alliance(msgs)
    ruler = find_ruler(alliances, competitors)
    if len(ruler) > 1:
        break_tie(ruler)
    else:
        print "Who is the ruler of Southeros?"
        print ruler[0]
        print "Allies of Ruler?"
        aliance = ''
        for each in alliances:
            if each[0] == ruler[0]:
                aliance = aliance + each[1] + " "
        print aliance
        return aliance


if __name__ == '__main__':
    competitors = raw_input().strip().upper().split(' ')
    breaker_of_chains(competitors)
