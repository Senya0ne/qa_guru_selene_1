from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    user = User(first_name='Sergei', last_name='Vasilchenko', email='test@test.com', gender='Male',
                phone_number='1234567890', birthdate_year='1993', birthdate_month='January', birthdate_day='31',
                subject='Maths', hobby='Sports', filename='image.png', address='Varshavskoe road, 1', state='NCR',
                city='Delhi')

    registration_page.open()
    registration_page.register(user)

    registration_page.should_have_modal_title_text('Thanks for submitting the form')
    registration_page.should_have_table_lines(10)
    registration_page.should_have_table_values(20)
    registration_page.should_have_registered(user)
