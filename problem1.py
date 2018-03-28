"""
SUMMER IS COMMING - 'Tame of Thrones' , A coding challenge for GeekTrust.

Problem 1 - ( The Golden Crown ) : There is no ruler in the universe of
Southeros and pandemonium reigns. Shan, the gorilla king of the Space kingdom
wants to rule all Six Kingdoms in the universe of Southeros. He needs the
support of 3 more kingdoms to be the ruler.

This module solves the first problem using code written in python3 adhereing to
PEP8 Coding Guidelines and Test Driven Development.

"""

import sys
import re
import os

Kingdoms = {"LAND": "PANDA", "WATER": "OCTOPUS", "ICE": "MAMMOTH",
            "AIR": "OWL", "FIRE": "DRAGON"}


class Input():

    def check_format(filename):
        # Get input from file and returns each line as a list element
        try:
            f = open(os.getcwd()+"/"+filename, 'rU')
        except FileNotFoundError:
            print('File not found Error.')
        else:
            txt = f.read()
            f.close()
            return txt.split('\n')

    def check_for_min_msg(all_msg):
        # Checks if there are atleast three messages
        if len(all_msg) >= 3:
            return True
        else:
            return False


class Message():

    def check_msg_format(message):
        # Checks the format of each line
        m = re.search("(^([a-zA-Z]+)[,]\s\"(.*)\")", message)
        try:
            if m and m.group() == message:
                return m.group(2), m.group(3)
            else:
                raise ValueError('The message format is wrong.')
                return False
        except ValueError as err:
            print(err.args)
            return False

    def decrypt_secret_msg(reciever, message):
        for ch in Kingdoms[reciever]:
            if ch in message:
                message = message[0:message.index(ch)] + message[message.index(ch)+1:]
            else:
                return False
            return True


def output(res, kingdoms_allies):
    print "Who is the ruler of Southeros?"
    print res
    print "Allies of Ruler?"
    if kingdoms_allies:
        print ', '.join(str(e) for e in kingdoms_allies)
    else:
        print "None"
    return True


def golden_crown(filename):
    allies = 0
    kingdoms_allies = []
    txt = input_format(filename)
    all_msg = list(filter(None, txt))  # Removes blank lines
    try:
        for each in all_msg:
            message = list(check_msg_format(each))
            if message[0].upper() in Kingdoms:
                i = Kingdoms.keys().index(message[0].upper())
                if decrypt_secret_msg(message[0].upper(), message[1].upper()):
                    allies = allies + 1
                    kingdoms_allies.append(message[0])
            else:
                raise ValueError("Check Kingdom Name.")
    except ValueError as err:
            print(err.args)
    else:
        if allies >= 3:
            res = "King Shan"
        else:
            res = "None"
        output(res, kingdoms_allies)
        if output:
            return True


if __name__ == '__main__':
    golden_crown(sys.argv[1])
