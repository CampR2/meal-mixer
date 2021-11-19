''' Converted recipe-scrapers object


    Author: Rob Camp (campR2) last modified: 09/21/2021
'''

from requests.exceptions import MissingSchema, InvalidURL, ConnectionError
from recipe_scrapers import scrape_me, WebsiteNotImplementedError, NoSchemaFoundInWildMode
from ..recipes.base import Base
from ..recipes.verify_scrape import VerifyScrape
from tools import _util as util
import logging

class Scraper(Base):
    """ A scraped recipe object

        scraper source: https://pypi.org/project/recipe-scrapers/,
                        https://github.com/hhursev/recipe-scrapers/

        A class decorator is used to modify the initial recipe-scrapers object.

    """

    def __init__(self):
        super(Scraper, self).__init__()
        self.console_log = logging.getLogger('console_log')
        self.scraper_recipe = self.get_scraper_recipe()
        while self.scraper_recipe is None:
            self.console_log.error('There may have been a problem with the URL.\
 For some reason an empty recipe was returned from it. Please check to see \
that the recipe is included in the url. E.g., https://cookieandkate.com has no \
recipe included, but https://cookieandkate.com/gluten-free-banana-bread-recipe/\
does.')
            self.scraper_recipe = self.get_scraper_recipe()

        if self.scraper_recipe == 0:
            # I.e., if get_scraper_recipe() below returns 0
            return(None) # go back to the menu
        self.name = self.scraper_recipe.title()
        self._ingredients = self.scraper_recipe.ingredients()
        self._instructions = self.scraper_recipe.instructions()
        self.reviews = self.scraper_recipe.reviews()
        self._url = self.scraper_recipe.canonical_url()
        self._cook_time = self.scraper_recipe.cook_time()
        self._prep_time = self.scraper_recipe.prep_time()
        self._total_time = self.scraper_recipe.total_time()
        self._nutrients = self.scraper_recipe.nutrients()
        self._yields = self.scraper_recipe.yields()
        self._category = self.scraper_recipe.category()
        self._host = self.scraper_recipe.host()
        self._image = self.scraper_recipe.image()
        self._language = self.scraper_recipe.language()
        self._links = self.scraper_recipe.links()
        self._scraped_rating = self.scraper_recipe.ratings()
        self._site_name = self.scraper_recipe.site_name()

    @VerifyScrape
    def get_scraper_recipe():
        ''' get a recipe-scrapers object '''
        console_log = logging.getLogger('console_log')
        get_scraper = True # base case, stops infinite loop below if False
        scraped_recipe = None
        while get_scraper is True:
            url = input("What is the URL of the recipe?: ")
            try:# look for the base URL the SCRAPERS dict
                # see: https://github.com/hhursev/recipe-scrapers/blob/master/recipe_scrapers/__init__.py
                scraped_recipe = scrape_me(url, wild_mode=False)
                get_scraper = False
            except WebsiteNotImplementedError:
                try:# try to parse the recipe URL schema on the fly
                    scraped_recipe = scrape_me(url, wild_mode=True)
                    get_scraper = False
                except (MissingSchema,
                        NoSchemaFoundInWildMode,
                        InvalidURL,
                        ConnectionError) as err:
                    console_log.error('%s: Either the URL entered is invalid, \
or the web-scraper used in this application is unable to pull from the URL \
provided: '%(err.__str__()))
                    print('Do you want to try again? ', end='')
                    yn = util.yes_no_loop()
                    if yn is True:
                        pass
                    elif yn is False:
                        scraped_recipe = 0
                        get_scraper = False
                        # break

        return scraped_recipe

    # property block
    @property
    def ingredients(self):
        return self._ingredients

    @property
    def instructions(self):
        return self._instructions

    @property
    def url(self):
        return self._url

    @property
    def cook_time(self):
        return self._cook_time

    @property
    def prep_time(self):
        return self._prep_time

    @property
    def total_time(self):
        return self._total_time

    @property
    def nutrients(self):
        return self._nutrients

    @property
    def yields(self):
        return self._yields

    @property
    def category(self):
        return self._category

    @property
    def host(self):
        return self._host

    @property
    def image(self):
        return self._image

    @property
    def language(self):
        return self._language

    @property
    def links(self):
        return self._links

    @property
    def scraped_rating(self):
        return self._scraped_rating

    @property
    def site_name(self):
        return self._category
