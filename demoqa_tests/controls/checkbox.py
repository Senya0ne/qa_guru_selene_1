from selene.support.shared import browser
from selene import have


def select_hobby(selector: str, hobby: str):
    browser.all(selector).element_by(have.text(hobby)).click()
