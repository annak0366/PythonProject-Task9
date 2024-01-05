from playwright.sync_api import Page

class SignupLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.__signup_name = self.page.locator('input[data-qa="signup-name"]')
        self.__signup_email = self.page.locator('input[data-qa="signup-email"]')
        self.__signup_btn = self.page.locator('button[data-qa="signup-button"]')
        self.__radio_btn = self.page.locator('#id_gender1')
        self.__password = self.page.locator('#password')
        self.__day_dropdown = self.page.locator('#days')
        self.__month_dropdown = self.page.locator('#months')
        self.__year_dropdown = self.page.locator('#years')
        self.__first_name = self.page.locator('#first_name')
        self.__last_name = self.page.locator('#last_name')
        self.__address = self.page.locator('#address1')
        self.__country = self.page.locator('#country')
        self.__state = self.page.locator('#state')
        self.__city = self.page.locator('#city')
        self.__zipcode = self.page.locator('#zipcode')
        self.__mobile_number = self.page.locator('#mobile_number')
        self.__create_account_btn = self.page.locator('button[data-qa="create-account"]')
        self.__successful_msg = self.page.locator('h2[data-qa="account-created"]')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')
        self.__login_email = self.page.locator('input[data-qa="login-email"]')
        self.__login_password = self.page.locator('input[data-qa="login-password"]')
        self.__login_btn = self.page.locator('button[data-qa="login-button"]')

    def fill_signup_form(self, name, email, password, address, city, zipcode, mobile_number):
        self.__signup_name.fill(name)
        self.__signup_email.fill(email)
        self.__signup_btn.click()
        self.__radio_btn.check(force=True)
        self.__password.fill(password)
        self.__day_dropdown.click()
        self.__day_dropdown.select_option('1')
        self.__month_dropdown.click()
        self.__month_dropdown.select_option('1')
        self.__year_dropdown.click()
        self.__year_dropdown.select_option('2000')
        self.__first_name.fill(name)
        self.__last_name.fill(name)
        self.__address.fill(address)
        self.__country.click()
        self.__country.select_option('Canada')
        self.__state.fill(city)
        self.__city.fill(city)
        self.__zipcode.fill(zipcode)
        self.__mobile_number.fill(mobile_number)
        self.__create_account_btn.click()

    def get_header(self):
        return self.__successful_msg.inner_text()

    def click_continue_btn(self):
        self.__continue_btn.click()

    def fill_login_data(self, email, password):
        self.__login_email.fill(email)
        self.__login_password.fill(password)
        self.__login_btn.click()