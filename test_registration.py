import os
from selene import browser, have, be
import pytest
from selene.core.condition import Condition


@pytest.fixture(autouse=True)
def browser_base_url_and_resolution():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1920
    browser.config.window_height = 1400
    yield
    browser.quit()


def test_registration_form():
    browser.open('/')
    # Заполнение формы
    browser.element('#firstName').should(be.visible).type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('name@google.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('8999456123')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1993"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="4"]').click()
    browser.element('[aria-label="Choose Thursday, May 20th, 1993"]').click()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').type(os.path.abspath('cat.jpg'))
    browser.element('#currentAddress').type('BII357, Block B 2, Raghubir Nagar, Tagore Garden Extension')
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    # Отправка формы
    browser.element('#submit').click()
    # Проверки
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('td').should(
        have.exact_texts(
            'Student Name', 'Ivan Ivanov',
            'Student Email', 'name@google.com',
            'Gender', 'Male',
            'Mobile', '8999456123',
            'Date of Birth', '20 May,1993',
            'Subjects', 'History',
            'Hobbies', 'Sports',
            'Picture', 'cat.jpg',
            'Address', 'BII357, Block B 2, Raghubir Nagar, Tagore Garden Extension',
            'State and City',	'Haryana Panipat',
        )
    )
    browser.element('#closeLargeModal').should(
        Condition.by_and(be.visible, be.clickable)
    )


