import os
import allure
from selene import have

def test_student_registration_form(setup_browser):
    browser = setup_browser
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
def open_registration_forme(_browser):
 _browser.open('https://demoqa.com/automation-practice-form')

# заполнение Name: поля First Name и Last Name
@allure.step("Заполняем Name: поля First Name={first_name} и Last Name={last_name}")
def filling_name(_browser, first_name, last_name):
    _browser.element('[id="firstName"]').type(first_name)
    _browser.element('[id="lastName"]').type(last_name)

# заполнение поля Email
@allure.step("Заполняем Email={email}")
def filling_email(_browser, email):
    _browser.element('[id="userEmail"]').type(email)

# выбор Gender
@allure.step("Заполняем Gender={gender}")
def filling_gender(_browser, gender):
    _browser.element('label[for="gender-radio-2"]').click()

# заполнение поля Mobile
@allure.step("Заполняем Mobile={mobile}")
def filling_mobile(_browser, mobile):
    _browser.element('[id="userNumber"]').type(mobile)

# выбор Date of Birth кликом из календаря
@allure.step("Заполняем Date of Birth={date}")
def filling_date(_browser, date):
  _browser.element('[id="dateOfBirthInput"]').click()
  _browser.element('button[aria-label="Previous Month"]').click()
  _browser.element('[aria-label="Choose Wednesday, July 30th, 2025"]').click()

@allure.step("Заполняем Subjects={subject}")
def filling_subjects(_browser, subject):
    _browser.element('#subjectsInput').type('co')
    _browser.element('.subjects-auto-complete__option').click()

# выбор Hobbies
@allure.step("Заполняем Hobbies={hobbies}")
def filling_hobbies(_browser, hobbies):
    _browser.element('label[for="hobbies-checkbox-2"]').click()
    _browser.element('label[for="hobbies-checkbox-3"]').click()

# добавление Picture
@allure.step("Заполняем Picture={filename}")
def filling_picture(_browser, filename):
 _browser.element('#uploadPicture').send_keys(os.path.abspath(filename))

# заполнение поля Current Address
@allure.step("Заполняем Address={address}")
def filling_address(_browser, address):
    _browser.element('[id="currentAddress"]').type(address)

# заполнение State and City: выбор State, затем City
@allure.step("Выбираем State={state}")
def filling_state(_browser, state):
    _browser.element('[id="state"]').click()

@allure.step("Выбираем City={city}")
def filling_city(_browser, city):
  _browser.element('div[class*="option"]').click()
  _browser.element('[id="city"]').click()
  _browser.element('div[class*="option"]').click()

 # отправка формы
@allure.step("Отправляем форму")
def filling_submit(_browser):
    _browser.element('[id="submit"]').click()

 # проверка формы "Thanks for submitting the form"
@allure.step("Проверяем форму")
def filling_check(_browser):
  _browser.element('[class="modal-content"]').should(have.text('Thanks for submitting the form'))
  _browser.element('.table').should(have.text('Anna Kostina'))
  _browser.element('.table').should(have.text('111name@example.com'))
  _browser.element('.table').should(have.text('Female'))
  _browser.element('.table').should(have.text('8788888888'))
  _browser.element('.table').should(have.text('30 July,2025'))
  _browser.element('.table').should(have.text('Computer Science'))
  _browser.element('.table').should(have.text('Reading, Music'))
  _browser.element('.table').should(have.text('test.jpg'))
  _browser.element('.table').should(have.text('Moscow'))
  _browser.element('.table').should(have.text('NCR Delhi'))
