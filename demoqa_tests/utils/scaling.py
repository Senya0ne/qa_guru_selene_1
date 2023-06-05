from selene.support.shared import browser


def zoom_out(value: float):
    browser.execute_script(f'document.querySelector(".body-height").style.transform = "scale({value})"')
