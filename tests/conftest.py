import logging
from datetime import datetime
from typing import Any, Generator

import pytest
import yaml
from playwright.sync_api import sync_playwright, Browser

from data.user import User
from pages.login_page import LoginPage


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        handlers=[
            logging.FileHandler(f'run_artifacts/test_log_{timestamp}.log', mode='w'),
            logging.StreamHandler()
        ],
        force=True
    )
    logging.info('Logging configured for test session')


@pytest.fixture(scope='function')
def browser() -> Generator[Browser, Any, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def login_page(browser) -> Generator[LoginPage, Any, None]:
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    yield login_page
    page.close()


@pytest.fixture(scope='session')
def credentials():
    # The credentials should be environment variables and kept in secret.
    # This is just for demonstration purposes
    with open('data/user_data.yaml', 'r') as f:
        credentials = yaml.safe_load(f)
    yield credentials


@pytest.fixture(scope='session')
def main_user(credentials) -> Generator[User, Any, None]:
    main_user = User(
        str(credentials['main_user']['username']),
        str(credentials['main_user']['password']),
        str(credentials['main_user']['first_name']),
        str(credentials['main_user']['last_name']),
        str(credentials['main_user']['zip_code'])
    )
    yield main_user


@pytest.fixture(scope='session')
def incorrect_user(credentials) -> Generator[User, Any, None]:
    incorrect_user = User(
        str(credentials['incorrect_user']['username']),
        str(credentials['incorrect_user']['password'])
    )
    yield incorrect_user
