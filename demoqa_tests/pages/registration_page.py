from selene.support.shared import browser
from selene import have
from demoqa_tests.controls import dropdown, radiobutton, checkbox, datepicker


class RegistrationPage:

    def given_opened(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def submit(self):
        browser.element('#submit').click()

    def select_state(self, value: str):
        dropdown.select('#state', by_text=value)

    def select_city(self, value: str):
        dropdown.select('#city', by_text=value)

    def select_gender(self, gender: str):
        radiobutton.select_gender(selector='[name=gender]', gender=gender)

    def select_date_of_birth(self, year: str, month: str, day_value: str):
        browser.element('#dateOfBirthInput').click()
        datepicker.select(selector='.react-datepicker__month-select', value=month)
        datepicker.select(selector='.react-datepicker__year-select', value=year)
        browser.element(f'[class$="react-datepicker__day--0{day_value} react-datepicker__day--weekend"]').click()

    def type_first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)

    def type_email(self, email: str):
        browser.element('#userEmail').type(email)

    def type_phone_number(self, phone_number: str):
        browser.element('#userNumber').type(phone_number)

    def type_subject(self, subject: str):
        browser.element('#subjectsInput').type(subject).press_enter()

    def type_address(self, address: str):
        browser.element('#currentAddress').type(address)

    def select_hobby(self, hobby: str):
        checkbox.select_hobby(selector='[for^=hobbies-checkbox]', hobby=hobby)

    def assert_table_fields(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))

    def assert_modal_title_text(self, text: str):
        browser.element('[class^=modal-title]').should(have.text(text))

    def assert_table_values(self, value: int):
        browser.all('.table>tbody>tr>td').should(have.size_greater_than_or_equal(value))

    def assert_table_lines(self, value: int):
        browser.all('.table>tbody>tr').should(have.size_greater_than_or_equal(value))
