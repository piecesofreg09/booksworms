'''
Tested on python 3.6

This function trains the data input.
First it transform the data into 4 subdatasets.


Usage:

python visualize
'''


import sys, os
import random
import json

def visualize():
    
    try:
        with open('reader_basket', 'r') as input:
            reader_basket = json.load(input)
    except:
        print('------------------------------------------------------')
        print('No input "reader_basket" file is found. Using sample_data instead.')
        script_dir = os.path.dirname(__file__)
        rel_path = 'sample_data'
        file_name = 'reader_basket'
        sample_data_path = os.path.join(script_dir, rel_path, file_name)
        # open the file
        with open(sample_data_path, 'r') as input:
            reader_basket = json.load(input)
        

    # get the users and generate one random user    
    users = list(reader_basket.keys())
    random_user = random.choice(users)

    # prepare for the flask
    print('Setting web browser')