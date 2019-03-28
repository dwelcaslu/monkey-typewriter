# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:21:25 2019

@author: Weld
"""

from monkey_typewriter import typewriter


if __name__ =='__main__':
    
    # Defining the text that will written by the monkeys:
    text = 'Aa'
    # Creating the monkey object:
    monkey = typewriter(text)
    # Performing the monkey writing test:
    monkey.text_write()

