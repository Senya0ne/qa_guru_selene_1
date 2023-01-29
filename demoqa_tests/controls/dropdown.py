from selene.support.shared import browser
from selene import have, command


def select(selector, by_text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(by_text)).click()
