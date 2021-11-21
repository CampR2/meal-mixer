''' base meal-mixer object

    author: Robert Camp (CampR2)
    last modified: 11/19/2021

'''
from app.tools._util import Util as Util
import uuid
import copy

class Base():
    ''' the base object of most other recipe and meal objects in MealMixer

        - self._name: starts as [(Util().utc_dt(), 'base')] as a way of recording
        the objects creation datetime.
        - self._object_history: a place to record past versions of objects
        when they change (prototype mode)
        self._uuid: a unique identifier in case there are recipes with the same
        name that get added to the mixer
        - self._usage_log: place to record datetimes of when the object is used
        - self._notes = user notes about the object
        - self._star_rating: star rating 1...5 initilized as int() which defaults
        to zero when no argument is added
        - self._average_star_rating: the average of all star ratings for this
        object
        - self._star_rating_history: a place to store a running star_history so
        that it may be averaged
        - self._taste_and_service_ratings: more detailed ratings about the object
        - self._reviews: user reviews about the object
        - self._frequency: the frequency at which the user wishes a recipe
        to be incorporated in the meal-mixer menus


    '''

    def __init__(self):
        self._name = {Util().tz_dt('UTC'): 'base'}
        self._object_history = {}
        self._uuid = uuid.uuid4()
        self._usage_log = {}
        self._notes = {}
        self._star_rating = int()
        self._average_star_rating = int()
        self._star_rating_history = {}
        self._taste_and_service_ratings = {}
        self._reviews = {}
        self._frequency = int()

    @property
    def name(self):
        ''' return the most current name of the object

            when setting the name of an object it must be 2...75 chars long

        '''
        return list(self._name.items())[len(self._name)-1][1]

    @name.setter
    def name(self, value):
        # security measure: lenth of the name must be >2, but <75
        if len(value) > 2 and len(value) < 75:
            self._name[Util().tz_dt()] = value
        else:
            print('Choose a name that is 3...75 characters long.')

    @property
    def star_rating(self):
        ''' return the current star rating of an object

            A star rating must be an integer between 1...5.
            All star ratings for an object are automatically averaged
        '''
        return self._star_rating

    @star_rating.setter
    def star_rating(self, value):
        try:
            value = int(value)
            if value > 0 and value < 6:
                self._star_rating_history.append((Util().tz_dt(), value))
                self._star_rating = value
                self.star_rating_average()
                print(f"The star_rating is: {value}")
            else:
                print('Please enter a whole number between 1...5')
        except ValueError as V:
            print('Please enter a whole number between 1...5')

    def star_rating_average(self):
        '''records the running average of the objects star ratings over time'''
        self._average_star_rating = \
        sum([history[1] for history in self._star_rating_history])\
        /len(self._star_rating_history)

    @property
    def average_star_rating(self):
        ''' return the average star rating for the the object'''
        return round(self._average_star_rating, 1)


    @property
    def star_rating_history(self):
        ''' return the star rating history'''
        return self._star_rating_history

    @property
    def uuid(self):
        ''' return the objects UUID number'''
        return(self._uuid)

    @property
    def taste_and_service_ratings(self):
        ''' return the objects taste and service ratings

            this may be blank some objects
        '''
        return(self._taste_and_service_ratings)

    @taste_and_service_ratings.setter
    def taste_and_service_ratings(self, rating_dict):
        self._taste_and_service_ratings[Util().tz_dt()] = rating_dict

    @property
    def notes(self):
        ''' return a list of the user notes about the object'''
        return(self._notes)

    @notes.setter
    def notes(self, note):
        self._note.append[Util().tz_dt] = note

    @property
    def usage_log(self):
        ''' return the usage log of the object'''
        return self._usage_log

    @usage_log.setter
    def usage_log(self, value):
        self._usage_log.append[Util().tz_dt()] = value

    @property
    def object_history(self):
        ''' return the object history expressed in object 'self' copies'''
        return self._object_history

    def set_object_history(self):
        self._object_history[Util().tz_dt()] = copy.deepcopy(self)

    @property
    def reviews(self):
        ''' return object's reviews'''
        return self._reviews

    @reviews.setter
    def reviews(self, review):
        self.reviews[Util().tz_dt()] = review


if __name__ == '__main__':
    print('This is not meant to be run as a stand alone module.\nGoodbye')
    exit()
