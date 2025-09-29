from __future__ import annotations

import logging
from abc import ABC

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


class BasePage(ABC):
    BASE_URL = r'https://www.saucedemo.com/v1/'
    PAGE_URL = 'undefined'

    def __init__(self, page: Page):
        self.page = page

    def __str__(self):
        return f'<{self.__class__.__name__}, {self.PAGE_URL}>'

    def navigate(self):
        logger.info(f'Going to {self.PAGE_URL}, {self.__class__}')
        self.page.goto(self.PAGE_URL)
        self.wait_until_loaded()

    def wait_until_loaded(self):
        logger.info(f'Waiting for page {self} to load')
        self.page.wait_for_url(self.PAGE_URL)
        self.page.wait_for_load_state()
        logger.info(f'Page {self} has loaded')

    def check_redirected_to(self):
        assert self.page.url == self.PAGE_URL
