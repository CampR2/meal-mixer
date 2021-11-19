''' decorator class designed to clean a 'recipe-scrapers' object before it is
    processed by MealMixer

    reference: https://pypi.org/project/recipe-scrapers/
        -
    Author: Rob Camp (campR2)
'''

from recipe_scrapers._exceptions import SchemaOrgException, ElementNotFoundInHtml
import logging


class VerifyScrape():
    ''' verify the information passed by "recipe-scrapers" is valid

        parameters:
            - get_scraper_recipe: the function from Scraper in ./scraper.py
            passed VerifyScrape
    '''

    def __init__(self, get_scraper_recipe):
        self.get_scraper_recipe = get_scraper_recipe

    def __call__(self, *args, **kwargs):
        ''' reference get_scraper_recipe from the scraper.py module'''

        scraped_recipe = self.get_scraper_recipe(*args)  # get recipe-scrapers object
        if scraped_recipe != None:
            verified_recipe = self.verify(scraped_recipe)
        else:
            verified_recipe = None
        return verified_recipe

    def verify(self, scraped_recipe):
        ''' verify the information passed by "recipe-scrapers" is valid

            Depending on which site the recipe is scraped from the
            recipe-scrapers module returns different info. verify() helps work
            around when info is not returned from any calls to the wrapped
            recipe_scrapers module. If nothing for a method call to recipe-scrapers
            is returned that method is monkey-patched with a method provided
            below that returns default data suitable for MealMixer to work with
            in the next phase of the Scraper object initalization.

            If a name, ingredients, or instructions are not present at the end
            of verification the Object initalization is assumed FAILED. This
            will kick the user back to the previous URL entry menu.

            parameters:
                - scraped_recipe: a recipe-scrapers object

            return:
                - None: if object initalization fails.
                - verified_recipe:  a verified and properly monkey-patched
                recipe-scrapers object
        '''
        verified_recipe = scraped_recipe
        error_pass = (TypeError,
                      NotImplementedError,
                      AttributeError,
                      NotImplementedError,
                      SchemaOrgException,
                      ElementNotFoundInHtml)
        try:
            verified_recipe.author()
        except error_pass:
            verified_recipe.author = self.author
        try:
            verified_recipe.title()
        except(error_pass):
            verified_recipe.title = self.title
        try:
            verified_recipe.cook_time()
        except(error_pass):
            verified_recipe.cook_time = self.cook_time
        try:
            verified_recipe.reviews()
        except(error_pass):
            verified_recipe.reviews = self.reviews
        try:
            verified_recipe.canonical_url()
        except(error_pass):
            verified_recipe.canonical_url = self.canonical_url
        try:
            verified_recipe.category()
        except(error_pass):
            verified_recipe.category = self.category
        try:
            verified_recipe.host()
        except(error_pass):
            verified_recipe.host = self.host
        try:
            verified_recipe.image()
        except(error_pass):
            verified_recipe.image = self.image
        try:
            verified_recipe.ingredients()
        except(error_pass):
            verified_recipe.ingredients = self.ingredients
        try:
            verified_recipe.instructions()
        except(error_pass):
            verified_recipe.instructions = self.instructions
        try:
            verified_recipe.language()
        except(error_pass):
            verified_recipe.language = self.language
        try:
            verified_recipe.links()
        except(error_pass):
            verified_recipe.links = self.links
        try:
            verified_recipe.nutrients()
        except(error_pass):
            verified_recipe.nutrients = self.nutrients
        try:
            verified_recipe.prep_time()
        except(error_pass):
            verified_recipe.prep_time = self.prep_time
        try:
            verified_recipe.ratings()
        except(error_pass):
            verified_recipe.ratings = self.ratings
        try:
            verified_recipe.site_name()
        except(error_pass):
            verified_recipe.site_name = self.site_name
        try:
            verified_recipe.total_time()
        except(error_pass):
            verified_recipe.total_time = self.total_time
        try:
            verified_recipe.site_name()
        except(error_pass):
            verified_recipe.site_name = self.site_name
        try:
            verified_recipe.yields()
        except(error_pass):
            verified_recipe.yields = self.yields

        if verified_recipe.title() == 'name error'\
        or verified_recipe.ingredients() == []\
        or verified_recipe.instructions() == '':

            verified_recipe = None

        return verified_recipe

    def total_time(self):
        return -1

    def author(self):
        return ''

    def cook_time(self):
        return -1

    def title(self):
        return 'name error'

    def reviews(self):
        return {}

    def canonical_url(self):
        return ''

    def category(self):
        return ''

    def host(self):
        return ''

    def image(self):
        return ''

    def ingredients(self):
        return []

    def instructions(self):
        return ''

    def nutrients(self):
        return {}

    def prep_time(self):
        return -1

    def ratings(self):
        return -1.0

    def schema(self):
        return None

    def site_name(self):
        return ''

    def yields(self):
        return ''
