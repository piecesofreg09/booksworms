'''
Main function
'''

import os
import sys
import json
import argparse

parser = argparse.ArgumentParser(description = 'bookworms portal')
parser.add_argument('functionality', help = 'Actions that can be done. \
    Actions are:\n train (t), visualize (v)')
parser.add_argument('-f', '--file', nargs = '*', 
                    dest = 'file', help = 'The files that are used for training')

parser.add_argument('-s', '--support', dest = 'support',
                    help = 'set up support for ASM training',
                    default = 10, type = int)

args = parser.parse_args()

if args.functionality == 'train' or args.functionality == 't':
    from .train import train
    train(args.file, args.support)
    
if args.functionality == 'visualize' or args.functionality == 'v':
    from .visualize import visualize
    visualize()