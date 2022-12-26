import os

from selene.support.shared import browser
from selene import have


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
    browser.element('#firstName').type('Sergei')
    browser.element('#lastName').type('Vasilchenko')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('January')
    browser.element('.react-datepicker__year-select').type('1993')
    browser.element('[class$="react-datepicker__day--031 react-datepicker__day--weekend"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/image.png')))
    browser.element('#currentAddress').type('Varshavskoe road, 1')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.element('[class^=modal-title]').should(have.text('Thanks for submitting the form'))
    browser.all('.table>tbody>tr').should(have.size_greater_than_or_equal(10))
    browser.all('.table>tbody>tr>td').should(have.size_greater_than_or_equal(20))
    browser.all('.table>tbody>tr>td:nth-child(2)').should(
        have.exact_texts('Sergei Vasilchenko', 'test@test.com', 'Male', '1234567890',
                         '31 January,1993', 'Maths',
                         'Sports', 'image.png', 'Varshavskoe road, 1', 'NCR Delhi'))
