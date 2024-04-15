import allure
from data.users import User
from pages.registration_page import RegistrationPage

@allure.tag('web')
@allure.title('Successful fill form')
def test_enter_data():
    registration_page = RegistrationPage()

    user = User(
        first_name='first name',
        last_name='last name',
        email='test@test.test',
        number='1234567890',
        gender='Female',
        month='March',
        year=1998,
        day=2,
        subjects='Computer Science',
        hobbies='Music',
        photo='Screenshot_1.png',
        address='Address',
        state='Haryana',
        city='Karnal'
    )

    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)
