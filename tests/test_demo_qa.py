from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.utils import scailing, file, scroll


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.given_opened()
    scailing.zoom_out(0.7)

    registration_page.type_first_name('Sergei')
    registration_page.type_last_name('Vasilchenko')
    registration_page.type_email('test@test.com')
    registration_page.select_gender('Male')
    registration_page.type_phone_number('1234567890')
    registration_page.select_date_of_birth(year='1993', month='January', day_value='31')

    registration_page.type_subject('Maths')
    registration_page.select_hobby('Sports')
    file.upload_image()
    scroll.to('#currentAddress')
    registration_page.type_address('Varshavskoe road, 1')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')

    registration_page.submit()

    registration_page.assert_modal_title_text('Thanks for submitting the form')
    registration_page.assert_table_lines(10)
    registration_page.assert_table_values(20)
    registration_page.assert_table_fields('Sergei Vasilchenko', 'test@test.com', 'Male', '1234567890',
                                          '31 January,1993', 'Maths',
                                          'Sports', 'image.png', 'Varshavskoe road, 1', 'NCR Delhi')
