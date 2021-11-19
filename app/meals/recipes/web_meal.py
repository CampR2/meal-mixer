''' Converted recipe-scrapers object


    Author: Rob Camp (campR2) last modified: 11/01/2021
'''

from requests.exceptions import MissingSchema, InvalidURL, ConnectionError, InvalidSchema
from recipe_scrapers import scrape_me, WebsiteNotImplementedError, NoSchemaFoundInWildMode
from ..recipes.base import Base
from ..recipes.verify_scrape import VerifyScrape
from app.tools import _util as util
import logging

class WebMeal(Base):
    """ A scraped recipe object

        scraper source: https://pypi.org/project/recipe-scrapers/,
                        https://github.com/hhursev/recipe-scrapers/

        A class decorator is used to modify the initial recipe-scrapers object.

    """

    def __init__(self, url):
        super(WebMeal, self).__init__()
        self.log = logging.getLogger('root')
        scraper_recipe = self.get_scraper_recipe(url)
        if scraper_recipe is None:
            log_message = 'There may have been a problem with the URL [%s].\
 For some reason an empty recipe was returned from it. Please check to see \
that the recipe is included in the url. E.g., https://cookieandkate.com has no \
recipe included, but https://cookieandkate.com/gluten-free-banana-bread-recipe/\
does.'%(url)
            self.log.error(log_message)

            return None

        self.name = scraper_recipe.title()
        self._ingredients = scraper_recipe.ingredients()
        self._instructions = scraper_recipe.instructions()
        self.reviews = scraper_recipe.reviews()
        self._url = scraper_recipe.canonical_url()
        self._cook_time = scraper_recipe.cook_time()
        self._prep_time = scraper_recipe.prep_time()
        self._total_time = scraper_recipe.total_time()
        self._nutrients = scraper_recipe.nutrients()
        self._yields = scraper_recipe.yields()
        self._category = scraper_recipe.category()
        self._host = scraper_recipe.host()
        self._image = scraper_recipe.image()
        self._language = scraper_recipe.language()
        self._links = scraper_recipe.links()
        self._scraped_rating = scraper_recipe.ratings()
        self._site_name = scraper_recipe.site_name()

    @VerifyScrape
    def get_scraper_recipe(url):
        ''' get a recipe-scrapers object '''
        log = logging.getLogger('root')
        scraped_recipe = None
        try:# look for the base URL the SCRAPERS dict
            # see: https://github.com/hhursev/recipe-scrapers/blob/master/recipe_scrapers/__init__.py
            scraped_recipe = scrape_me(url, wild_mode=False)
        except (WebsiteNotImplementedError, TypeError, InvalidSchema):
            try:# try to dynamically parse the recipe URL schema
                scraped_recipe = scrape_me(url, wild_mode=True)
            except (MissingSchema,
                    NoSchemaFoundInWildMode,
                    InvalidURL,
                    ConnectionError,
                    TypeError,
                    InvalidSchema) as err:
                log.error('[%s]: Either the URL entered is invalid, \
or the web-scraper used was unable to pull from the URL \
provided: '%(err.__str__()))

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
