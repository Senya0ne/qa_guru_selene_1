from demoqa_tests.model import registration_form
from demoqa_tests.utils import scailing, file, scroll


def test_student_registration_form():
    registration_form.given_opened()
    scailing.zoom_out(0.7)

    registration_form.type_first_name('Sergei')
    registration_form.type_last_name('Vasilchenko')
    registration_form.type_email('test@test.com')
    registration_form.select_gender('Male')
    registration_form.type_phone_number('1234567890')
    registration_form.select_date_of_birth(year='1993', month='January', day_value='31')

    registration_form.type_subject('Maths')
    registration_form.select_hobby('Sports')
    file.upload_image()
    scroll.to('#currentAddress')
    registration_form.type_address('Varshavskoe road, 1')
    registration_form.select_state('NCR')
    registration_form.select_city('Delhi')

    registration_form.submit()

    registration_form.assert_modal_title_text('Thanks for submitting the form')
    registration_form.assert_table_lines(10)
    registration_form.assert_table_values(20)
    registration_form.assert_table_fields('Sergei Vasilchenko', 'test@test.com', 'Male', '1234567890',
                                          '31 January,1993', 'Maths',
                                          'Sports', 'image.png', 'Varshavskoe road, 1', 'NCR Delhi')
