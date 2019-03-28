# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:05:45 2019

@author: Weld
"""
import random
import string

class typewriter(object):
    
    def __init__(self,text):
        '''
        Monkey builder method
        '''
        # Basic monkey attributes:
        self.text = text
        self.n = len(text)
        self.n_attempts = 0        
        # Attempts configuration variables:
        self.attempts_limit = 1e9
        self.attempts_print = 1e5
    
    
    def text_write(self):
        '''
        '''
        print('Monkeys start!')
        text_pass = False
        while text_pass == False:
            self.n_attempts += 1
            # Writing the text:
            new_text = self.write()
            if new_text == self.text.lower():
                text_pass = True
                print('The text was successfully writen by the monkeys!')
                print('Given text:\n' + self.text)
                print('Monkey text:\n' + new_text)
                print('Number of Attempts:',self.n_attempts)
            elif self.n_attempts > self.attempts_limit:
                print('The limit number os attempts was reached!')
                break
            elif self.n_attempts%self.attempts_print == 0:
                print('Attempt number:',self.n_attempts)

    
    def write(self):
        '''
        '''
        # Defining the possible characters:
        characters = string.ascii_lowercase + ' '
#        characters = string.ascii_lowercase + ' ' + string.digits
        text = ''
        for i in range(self.n):
            text += random.choice(characters)
        return text

