import os
import allure
from selene import browser, have

def test_student_registration_form():
 open_registration_forme()
 filling_name()
 filling_email()
 filling_gender()
 filling_mobile()
 filling_date()
 filling_subjects()
 filling_hobbies()
 filling_picture()
 filling_address()
 filling_state()
 filling_city()
 filling_submit()
 filling_check()



@allure.step("Открываем форму")
def open_registration_forme():
 browser.open('https://demoqa.com/automation-practice-form')

# заполнение Name: поля First Name и Last Name
@allure.step("Заполняем Name: поля First Name и Last Name")
def filling_name():
  browser.element('[id="firstName"]').type('Anna')
  browser.element('[id="lastName"]').type('Kostina')

# заполнение поля Email
@allure.step("Заполняем Email")
def filling_email():
  browser.element('[id="userEmail"]').type('111name@example.com')

# выбор Gender
@allure.step("Заполняем Gender")
def filling_gender():
  browser.element('label[for="gender-radio-2"]').click()

# заполнение поля Mobile
@allure.step("Заполняем Mobile")
def filling_mobile():
  browser.element('[id="userNumber"]').type('8788888888')

# выбор Date of Birth кликом из календаря
@allure.step("Заполняем Date of Birth")
def filling_date():
  browser.element('[id="dateOfBirthInput"]').click()
  browser.element('button[aria-label="Previous Month"]').click()
  browser.element('[aria-label="Choose Wednesday, July 30th, 2025"]').click()

# выбор Subjects
@allure.step("Заполняем Subjects")
def filling_subjects():
  browser.element('#subjectsInput').type('co')
  browser.element('.subjects-auto-complete__option').click()

# выбор Hobbies
@allure.step("Заполняем Hobbies")
def filling_hobbies():
  browser.element('label[for="hobbies-checkbox-2"]').click()
  browser.element('label[for="hobbies-checkbox-3"]').click()

# добавление Picture
@allure.step("Заполняем Picture")
def filling_picture():
  browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpg'))

# заполнение поля Current Address
@allure.step("Заполняем Address")
def filling_address():
  browser.element('[id="currentAddress"]').type('Moscow')

# заполнение State and City: выбор State, затем City
@allure.step("Выбираем State")
def filling_state():
  browser.element('[id="state"]').click()

@allure.step("Выбираем City")
def filling_city():
  browser.element('div[class*="option"]').click()
  browser.element('[id="city"]').click()
  browser.element('div[class*="option"]').click()

 # отправка формы
@allure.step("Отправляем форму")
def filling_submit():
  browser.element('[id="submit"]').click()

 # проверка формы "Thanks for submitting the form"
@allure.step("Проверяем форму")
def filling_check():
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