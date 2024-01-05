from playwright.sync_api import Page

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.__name_on_card = self.page.locator('input[data-qa="name-on-card"]')
        self.__card_number = self.page.locator('input[data-qa="card-number"]')
        self.__cvc = self.page.locator('input[data-qa="cvc"]')
        self.__expiration_month = self.page.locator('input[data-qa="expiry-month"]')
        self.__expiration_year = self.page.locator('input[data-qa="expiry-year"]')
        self.__pay_btn = self.page.locator('#submit')
        self.__succsess_message = self.page.locator('div[class="col-sm-9 col-sm-offset-1"] p')

    def enter_payment_details(self, name, card_number, cvc, month, year):
        self.__name_on_card.fill(name)
        self.__card_number.fill(card_number)
        self.__cvc.fill(cvc)
        self.__expiration_month.fill(month)
        self.__expiration_year.fill(year)
        self.__pay_btn.click()

    def get_success_message(self):
        return self.__succsess_message.inner_text()