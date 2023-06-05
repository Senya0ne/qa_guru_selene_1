from selene.support.shared import browser
from selene import have
from demoqa_tests.controls import dropdown, radiobutton, checkbox, datepicker
from demoqa_tests.data.users import User
from demoqa_tests.utils import file, scroll, scaling


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
        scaling.zoom_out(0.7)

    def submit(self):
        browser.element('#submit').click()

    def select_state(self, value: str):
        dropdown.select('#state', by_text=value)

    def select_city(self, value: str):
        dropdown.select('#city', by_text=value)

    def select_gender(self, gender: str):
        radiobutton.select_gender('[name=gender]', gender)

    def select_date_of_birth(self, year, month, day_value):
        browser.element('#dateOfBirthInput').click()
        datepicker.select('.react-datepicker__month-select', month)
        datepicker.select('.react-datepicker__year-select', year)
        browser.element(f'[class$="react-datepicker__day--0{day_value} react-datepicker__day--weekend"]').click()

    def type_first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)

    def type_email(self, email: str):
        browser.element('#userEmail').type(email)

    def type_phone_number(self, value: str):
        browser.element('#userNumber').type(value)

    def type_subject(self, subject: str):
        browser.element('#subjectsInput').type(subject).press_enter()

    def type_address(self, address: str):
        browser.element('#currentAddress').type(address)

    def select_hobby(self, hobby: str):
        checkbox.select_hobby('[for^=hobbies-checkbox]', hobby)

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.select_gender(user.gender)
        self.type_phone_number(str(user.phone_number))
        self.select_date_of_birth(user.birthdate_year, user.birthdate_month, user.birthdate_day)
        self.type_subject(user.subject)
        self.select_hobby(user.hobby)
        file.upload_image()
        scroll.to('#currentAddress')
        self.type_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)

        self.submit()

    def should_have_registered(self, user: User):
        full_name = f'{user.first_name} {user.last_name}'
        date_of_birth = f'{user.birthdate_day} {user.birthdate_month},{user.birthdate_year}'
        subject = user.subject
        hobby = user.hobby
        state_city = f'{user.state} {user.city}'
        browser.all('.table td').even.should(have.texts(full_name,
                                                           user.email,
                                                           user.gender,
                                                           str(user.phone_number),
                                                           date_of_birth,
                                                           subject,
                                                           hobby,
                                                           user.filename,
                                                           user.address,
                                                           state_city))

    def should_have_modal_title_text(self, text: str):
        browser.element('[class^=modal-title]').should(have.text(text))

    def should_have_table_values(self, value: int):
        browser.all('.table tbody tr td').should(have.size_greater_than_or_equal(value))

    def should_have_table_lines(self, value: int):
        browser.all('.table tbody tr').should(have.size_greater_than_or_equal(value))