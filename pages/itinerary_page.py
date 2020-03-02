from selenium.webdriver.common.by import By
from pages.page import Page


class ItineraryPage(Page):
    # LOCATORS


    def __init__(self, context):
        Page.__init__(self, context)
