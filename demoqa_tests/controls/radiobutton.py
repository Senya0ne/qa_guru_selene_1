from selene.support.shared import browser
from selene import have


def select_gender(selector: str, gender: str):
    browser.all(selector).element_by(have.value(gender)).element('..').click()