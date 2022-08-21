'''Capture user configurations
Author: Rob Camp (campR2) 
last modified: 04/18/2022
'''
import sys
import os.path
import configparser

global_config = 'global_config.ini'

def get_config_file(conf_file):
    '''generate generic config_parser object'''
    if conf_file:
        if os.path.exists(conf_file):
            parser = configparser.ConfigParser()
            parser.read(conf_file)
            print(f"READING IN CONFIG FILE: {conf_file}")
            return(parser)
        else: 
            print(f'CONFIG FILE NOT FOUND: {conf_file}')
            return(None)
            
    else:
        print('CONFIG FILE IS BLANK OR NONE: USING THE DEFAULT GLOBAL CONFIG')
        return(None)

class MealMixer_Config_Class(object):
    def __init__(self, user_config=None, global_config_new = None):
        if user_config: 
            self.user_config = get_config_file(user_config)
            self.user_log_level = self.user_config['MAIN_CONFIG']['log_lvl']
            self.user_log_file = self.user_config['MAIN_CONFIG']['log_file']
        if global_config_new: self.global_config = get_config_file(global_config_new)
        else:
            self.global_config = get_config_file(global_config)
        self.global_log_level = self.global_config['MAIN_CONFIG']['log_lvl']
        self.global_log_file = self.global_config['MAIN_CONFIG']['log_file']        