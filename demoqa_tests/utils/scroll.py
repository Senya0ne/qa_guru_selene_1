from selene.support.shared import browser
from selene import command


def to(selector: str):
    browser.element(selector).perform(command.js.scroll_into_view)
