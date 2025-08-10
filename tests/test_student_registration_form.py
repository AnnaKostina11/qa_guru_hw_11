import os
import allure
from selene import browser, have

def test_student_registration_form(setup_browser):
    _browser = setup_browser
    _browser.driver.set_window_size(1920, 2000)
    open_registration_forme(_browser)
    filling_name(_browser, 'Anna', 'Kostina')
    filling_email(_browser, '111name@example.com')
    filling_gender(_browser, 'Female')
    filling_mobile(_browser, '8788888888')
    filling_date(_browser, '30 July,2025')
    filling_subjects(_browser, 'Computer Science')
    filling_hobbies(_browser, 'Reading, Music')
    filling_picture(_browser, 'tests/test.jpg')
    filling_address(_browser, 'Moscow')
    filling_state(_browser, 'NCR')
    filling_city(_browser, 'Delhi')
    filling_submit(_browser)
    filling_check(_browser)



@allure.step("Открываем форму")
def open_registration_forme(_browser):
 browser.open('https://demoqa.com/automation-practice-form')

# заполнение Name: поля First Name и Last Name
@allure.step("Заполняем Name: поля First Name={first_name} и Last Name={last_name}")
def filling_name(_browser, first_name, last_name):
    browser.element('[id="firstName"]').type(first_name)
    browser.element('[id="lastName"]').type(last_name)

# заполнение поля Email
@allure.step("Заполняем Email={email}")
def filling_email(_browser, email):
    browser.element('[id="userEmail"]').type(email)

# выбор Gender
@allure.step("Заполняем Gender={gender}")
def filling_gender(_browser, gender):
    browser.element('label[for="gender-radio-2"]').click()

# заполнение поля Mobile
@allure.step("Заполняем Mobile={mobile}")
def filling_mobile(_browser, mobile):
    browser.element('[id="userNumber"]').type(mobile)

# выбор Date of Birth кликом из календаря
@allure.step("Заполняем Date of Birth={date}")
def filling_date(_browser, date):
  browser.element('[id="dateOfBirthInput"]').click()
  browser.element('button[aria-label="Previous Month"]').click()
  browser.element('[aria-label="Choose Wednesday, July 30th, 2025"]').click()

@allure.step("Заполняем Subjects={subject}")
def filling_subjects(_browser, subject):
    browser.element('#subjectsInput').type('co')
    browser.element('.subjects-auto-complete__option').click()

# выбор Hobbies
@allure.step("Заполняем Hobbies={hobbies}")
def filling_hobbies(_browser, hobbies):
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

# добавление Picture
@allure.step("Заполняем Picture={filename}")
def filling_picture(_browser, filename):
 browser.element('#uploadPicture').send_keys(os.path.abspath(filename))

# заполнение поля Current Address
@allure.step("Заполняем Address={address}")
def filling_address(_browser, address):
    browser.element('[id="currentAddress"]').type(address)

# заполнение State and City: выбор State, затем City
@allure.step("Выбираем State={state}")
def filling_state(_browser, state):
    browser.element('[id="state"]').click()

@allure.step("Выбираем City={city}")
def filling_city(_browser, city):
  browser.element('div[class*="option"]').click()
  browser.element('[id="city"]').click()
  browser.element('div[class*="option"]').click()

 # отправка формы
@allure.step("Отправляем форму")
def filling_submit(_browser):
    browser.element('[id="submit"]').click()

 # проверка формы "Thanks for submitting the form"
@allure.step("Проверяем форму")
def filling_check(_browser):
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
