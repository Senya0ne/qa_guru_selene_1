from selene.support.shared import browser
from selene import have


def select(selector, value):
    browser.element(selector).all('option').element_by(have.exact_text(value)).click()
