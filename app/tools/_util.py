
''' utilities module for meal-mixer
    Author: Robert Camp (CampR2)
    Last Modified: 11/19/2021

'''
from datetime import datetime
from dateutil.tz import gettz
import logging


class Util():
    ''' _utility functions that may be useful to more than one module

        no input
        core logger called in __init__
    '''

    def __init__(self):

        super(Util, self).__init__()
        self.log = logging.getLogger('root')

    def tz_dt(self, time_zone='America/Chicago'):
        ''' get datetime object for a specific timezone

            input:
                - default: 'American/Chicago' (CST/CDT)
                - str: a time zone in tz_database format
            output:
                - obj: datetime object for a specific timezone
            time-zone info: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        '''
        self.log.info(f'the TZ_DATETIME is: {datetime.now(gettz(time_zone))}: tools__util.py')
        return(datetime.now(gettz(time_zone)))

