from selene import browser, have, be
import pytest


@pytest.fixture(autouse=True)
def browser_base_url_and_resolution():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1400
    yield
    browser.quit()


def test_registration_form():
    browser.open('/')
    browser.element('#firstName').should(be.visible).type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('name@google.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8999456123')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1993"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="4"]').click()
    browser.element('[aria-label="Choose Thursday, May 20th, 1993"]').click()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').type('BII357, Block B 2, Raghubir Nagar, Tagore Garden Extension')
    browser.element('#state').click()
    browser.element('//div[text()="NCR"]').click()
    browser.element('#city').click()
    browser.element('//div[text()="Delhi"]').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))



