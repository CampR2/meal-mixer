from datetime import datetime
from dateutil.tz import gettz, UTC
import logging

''' _utility functions that may be useful to more than one module '''


def tz_dt(time_zone='American/Chicago'):
    ''' return a datetime object for a specific timezone'''
    log = logging.getLogger('root')
    log.info(f'the TZ_DATETIME is: {datetime.now(gettz(time_zone))}: tools__util.py')
    return(datetime.now(gettz(time_zone)))

