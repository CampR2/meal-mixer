''' bring logging functionality to MealMixer

    info links:
    - https://docs.python.org/3/howto/logging-cookbook.html#using-concurrent-futures-processpoolexecutor
        (from the "A more elaborate multiprocessing" example)
    - https://docs.python.org/3/library/logging.html?highlight=logging#module-logging

    Author: Rob Camp (CampR2)
    last modified: 11/09/2021

 '''
from os.path import abspath, dirname, join
import logging
import logging.config
import logging.handlers
import time

# Replace dt1 with dt0 below to create unique logs for each run of MealMixer.
dt0 = time.strftime('%m.%d.%y-%H.%M.%S.%p')
dt1='1'
# file names
app_log = (f'meal_mixer_{dt1}.log')
debug_log = (f'debug_{dt1}.log')
# path to _logging package
logging_path = abspath(dirname(__file__))
# paths to logging files
app_log = join(logging_path + "/logs", app_log)
debug_log = join(logging_path + "/logs", debug_log)

''' logging configuration

    references:
        - https://docs.python.org/3/library/logging.config.html #logging-config-dictschema

    Notes:
        - When bugs occur the debug log can be used to isolate the problem.
        - Use the root logger to write to the standard logging file
        - Use the debug logger to write to the debug file for bug isolation
            * This is not meant ot be a replacement for testing but instead
            a replacement for the print statement when a more persistant text
            ouput is needed.
'''

LOG_CONFIG = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': ' *** \nTime: %(asctime)s\
                                \nlogger: %(name)s\
                                \nlog level: %(levelname)s\
                                \npath: %(pathname)s , line: %(lineno)s\
                                \nmessage: %(message)s)'
            },
            'simple': {
                'class': 'logging.Formatter',
                'format': '***\nlog message: %(message)s\n***'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                'level': 'WARNING',
                'stream': 'ext://sys.stderr'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': app_log,
                'mode': 'w',
                'formatter': 'detailed',
                'level': 'INFO'
            },
            'debug_file': {
                'class': 'logging.FileHandler',
                'filename': debug_log,
                'mode': 'w',
                'formatter': 'detailed',
                'level': 'DEBUG'
            }
        },
        'loggers': {
            'console': {
                'handlers': ['console'],
                'level': 'WARNING',
                'propagate': False
            },
            'console_log': {
                'handlers': ['file', 'console'],
                'level': 'WARNING',
                'propagate': False
            },
            'debug': {
                'handlers': ['debug_file'],
                'level': 'DEBUG',
                'propagate': False
            }
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    }

# configure logging for MealMixer
logging.config.dictConfig(LOG_CONFIG)
