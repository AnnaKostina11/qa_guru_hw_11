import os
import allure
from selene import browser, have

def test_student_registration_form(setup_browser):
    browser = setup_browser
    browser.driver.set_window_size(1920, 2000)
    open_registration_forme(browser)
    filling_name(browser, 'Anna', 'Kostina')
    filling_email(browser, '111name@example.com')
    filling_gender(browser, 'Female')
    filling_mobile(browser, '8788888888')
    filling_date(browser, '30 July,2025') 
    filling_subjects(browser, 'Computer Science')
    filling_hobbies(browser, 'Reading, Music')
    filling_picture(browser, 'tests/test.jpg')
    filling_address(browser, 'Moscow')
    filling_state(browser, 'NCR')
    filling_city(browser, 'Delhi')
    filling_submit(browser)
    filling_check(browser)



@allure.step("Открываем форму")
def open_registration_forme(browser):
 browser.open('https://demoqa.com/automation-practice-form')

# заполнение Name: поля First Name и Last Name
@allure.step("Заполняем Name: поля First Name={first_name} и Last Name={last_name}")
def filling_name(browser, first_name, last_name):
    browser.element('[id="firstName"]').type(first_name)
    browser.element('[id="lastName"]').type(last_name)

# заполнение поля Email
@allure.step("Заполняем Email={email}")
def filling_email(browser, email):
    browser.element('[id="userEmail"]').type(email)

# выбор Gender
@allure.step("Заполняем Gender={gender}")
def filling_gender(browser, gender):
    browser.element('label[for="gender-radio-2"]').click()

# заполнение поля Mobile
@allure.step("Заполняем Mobile={mobile}")
def filling_mobile(browser, mobile):
    browser.element('[id="userNumber"]').type(mobile)

# выбор Date of Birth кликом из календаря
@allure.step("Заполняем Date of Birth={date}")
def filling_date(browser, date):
  browser.element('[id="dateOfBirthInput"]').click()
  browser.element('button[aria-label="Previous Month"]').click()
  browser.element('[aria-label="Choose Wednesday, July 30th, 2025"]').click()

@allure.step("Заполняем Subjects={subject}")
def filling_subjects(browser, subject):
    browser.element('#subjectsInput').type('co')
    browser.element('.subjects-auto-complete__option').click()

# выбор Hobbies
@allure.step("Заполняем Hobbies={hobbies}")
def filling_hobbies(browser, hobbies):
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

# добавление Picture
@allure.step("Заполняем Picture={filename}")
def filling_picture(browser, filename):
 browser.element('#uploadPicture').send_keys(os.path.abspath(filename))

# заполнение поля Current Address
@allure.step("Заполняем Address={address}")
def filling_address(browser, address):
    browser.element('[id="currentAddress"]').type(address)

# заполнение State and City: выбор State, затем City
@allure.step("Выбираем State={state}")
def filling_state(browser, state):
    browser.element('[id="state"]').click()

@allure.step("Выбираем City={city}")
def filling_city(browser, city):
  browser.element('div[class*="option"]').click()
  browser.element('[id="city"]').click()
  browser.element('div[class*="option"]').click()

 # отправка формы
@allure.step("Отправляем форму")
def filling_submit(browser):
    browser.element('[id="submit"]').click()

 # проверка формы "Thanks for submitting the form"
@allure.step("Проверяем форму")
def filling_check(browser):
  browser.element('[class="modal-content"]').should(have.text('Thanks for submitting the form'))
  browser.element('.table').should(have.text('Anna Kostina'))
  browser.element('.table').should(have.text('111name@example.com'))
  browser.element('.table').should(have.text('Female'))
  browser.element('.table').should(have.text('8788888888'))
  browser.element('.table').should(have.text('30 July,2025'))
  browser.element('.table').should(have.text('Computer Science'))
  browser.element('.table').should(have.text('Reading, Music'))
  browser.element('.table').should(have.text('test.jpg'))
  browser.element('.table').should(have.text('Moscow'))
  browser.element('.table').should(have.text('NCR Delhi'))
