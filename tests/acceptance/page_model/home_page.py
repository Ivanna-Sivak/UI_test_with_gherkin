from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class Homepage(BasePage):
    @property
    def url(self):
        return super(Homepage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)