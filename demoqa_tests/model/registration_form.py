from selene.support.shared import browser
from selene import have, command
from demoqa_tests.controls import dropdown


def given_opened():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))


def submit():
    browser.element('#submit').click()


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)

