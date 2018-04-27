'''
Tested on python 3.6

This function visualizes the data from data transformation and
training. If no training and data transformation is done previously,
this function will load sample dataset, which is 100 readers.

Usage:

python visualize
'''


import sys, os
import random
import json

def visualize():
    # visualize() takes no input argument, as intput argument should be generated
    # from the training process. If train is not called, visualize() will use the 
    # predownloaded data for visualization
    
    
    try:
        # open input data
        with open('reader_basket', 'r') as input:
            reader_basket = json.load(input)
    except:
        # if no input data is generated, sample data from the folder 'sample_data'
        # will be used
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
    
    # get the first book of the random user for friend-weighted algorithm
    all_book_keys = list(reader_basket[random_user].keys())
    first_book = all_book_keys[0]

    # prepare for the flask website visulization
    print('Setting web page for visualization')
    # NEEDS IMPLEMENTATION
    
    
    
