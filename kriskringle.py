#!/usr/bin/python

"""
KRIS KRINGLE SIMULATOR 2021
Run as kris-kringle.py name1 name2 name3
Will exclude any illegal pairings (partners, self)

Written for python/2.7.9

"""
import sys
import random
import os

# prepare the hat
def pull_names(name_buys, name_for):
        print("%s gets present for %s.\n" % (name_buys, name_for))

if len(sys.argv) < 3 :
    print "OOPS! You didn't run it properly. Run as python", sys.argv[0], "name1 name2 name3..."

names = sys.argv[1:]

# put everyones names in the hat
random.shuffle(names)

# exclude spouse pairs
# currently not able to do this  

# pull names out of the house 
print(r"""
               ___
             /`   `'.
            /   _..---;
            |  /__..._/  .--.-.
            |.'  e e | ___\_|/____
           (_)'--.o.--|    | |    |
          .-( `-' = `-|____| |____|
         /  (         |____   ____|
         |   (        |_   | |  __|
         |    '-.--';/'/__ | | (  `|
         |      '.   \    )"";--`\ /
         \        ;   |--'    `;.-'
         |`-.__ ..-'--'`;..--'`

    __          _          __          _                __               _                    __        __
   / /__ _____ (_)_____   / /__ _____ (_)____   ____ _ / /___     _____ (_)____ ___   __  __ / /____ _ / /_ ____   _____
  / //_// ___// // ___/  / //_// ___// // __ \ / __ `// // _ \   / ___// // __ `__ \ / / / // // __ `// __// __ \ / ___/
 / ,<  / /   / /(__  )  / ,<  / /   / // / / // /_/ // //  __/  (__  )/ // / / / / // /_/ // // /_/ // /_ / /_/ // /
/_/|_|/_/   /_//____/  /_/|_|/_/   /_//_/ /_/ \__, //_/ \___/  /____//_//_/ /_/ /_/ \__,_//_/ \__,_/ \__/ \____//_/
                                             /____/

""")

for index in range(0, len(names) - 1):
    pull_names(names[index], names[index + 1])
pull_names(names[len(names) - 1], names[0])
