from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.__address_checkout = self.page.locator("ul[id='address_delivery'] li:nth-child(4)")
        self.__first_product_name = self.page.locator('h4 a[href="/product_details/1"]')
        self.__second_product_name = self.page.locator('h4 a[href="/product_details/2"]')
        self.__description_input = self.page.locator('textarea[class="form-control"]')
        self.__place_order = self.page.locator('a[href="/payment"]')

    def check_address_details(self):
        return self.__address_checkout.inner_text()

    def fill_description_field(self, text):
        self.__description_input.fill(text)
        self.__place_order.click()