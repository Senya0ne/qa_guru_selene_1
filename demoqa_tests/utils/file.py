from selene.support.shared import browser
import os


def upload_image():
    browser.element('#uploadPicture').send_keys(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/image.png')))
