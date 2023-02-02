from selene.support.shared import browser
from selene import have
from demoqa_tests.controls import dropdown


def given_opened():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))


def submit():
    browser.element('#submit').click()


def select_state(value: str):
    dropdown.select('#state', by_text=value)


def select_city(value: str):
    dropdown.select('#city', by_text=value)


def select_gender(gender: str):
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()


def select_date_of_birth(year: str, month: str, day_value: str):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(month)
    browser.element('.react-datepicker__year-select').type(year)
    browser.element(f'[class$="react-datepicker__day--0{day_value} react-datepicker__day--weekend"]').click()


def type_first_name(first_name: str):
    browser.element('#firstName').type(first_name)


def type_last_name(last_name: str):
    browser.element('#lastName').type(last_name)


def type_email(email: str):
    browser.element('#userEmail').type(email)


def type_phone_number(phone_number: str):
    browser.element('#userNumber').type(phone_number)


def type_subject(subject: str):
    browser.element('#subjectsInput').type(subject).press_enter()


def type_address(address: str):
    browser.element('#currentAddress').type(address)


def select_hobby(hobby: str):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()


def assert_table_fields(*args):
    browser.element('.table').all('td').even.should(have.texts(args))


def assert_modal_title_text(text: str):
    browser.element('[class^=modal-title]').should(have.text(text))


def assert_table_values(value: int):
    browser.all('.table>tbody>tr>td').should(have.size_greater_than_or_equal(value))


def assert_table_lines(value: int):
    browser.all('.table>tbody>tr').should(have.size_greater_than_or_equal(value))
