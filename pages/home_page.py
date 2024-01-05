from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.__logo = self.page.locator('div[class="logo pull-left"]')
        self.__subscribe_text = self.page.locator('//*[@id="footer"]//h2')
        self.__email_input = self.page.locator('[id="susbscribe_email"]')
        self.__subscribe_btn = self.page.locator('button[id="subscribe"]')
        self.__successful_message = self.page.locator('[id="success-subscribe"]')
        self.__cart_btn = self.page.locator('a[href="/view_cart"] > i.fa.fa-shopping-cart')
        self.__products_btn = self.page.locator('a[href="/products"]')
        self.__contact_btn = self.page.locator('a[href="/contact_us"]')
        self.__view_product_btn = self.page.locator("a[href='/product_details/1']")
        self.__login_register_btn = self.page.locator('a[href="/login"]')
        self.__add__first_product = self.page.locator('//a[@data-product-id="1"]').nth(0)
        self.__add_second_product = self.page.locator('a[data-product-id="2"]').nth(0)
        self.__continue_btn = self.page.locator("//button[@class='btn btn-success close-modal btn-block']")
        self.__loggedin_user = self.page.locator('li:nth-child(10) a')
        self.__category_panel = self.page.locator('div[id="accordian"]')
        self.__women_category = self.page.locator('a[href="#Women"]')
        self.__women_subcategory = self.page.locator('a[href="/category_products/1"]')
        self.__category_text = self.page.locator(".title.text-center")
        self.__men_category = self.page.locator('a[href="#Men"]')
        self.__men_subcategory = self.page.locator('a[href="/category_products/3"]')

    def logo_is_visible(self):
        return self.__logo.is_visible()

    def get_footer_text(self):
        return self.__subscribe_text.inner_text()

    def fill_subscribe_data(self, email) -> None:
        self.__email_input.fill(email)
        self.__subscribe_btn.click()

    def is_successful_message_visible(self) -> bool:
        return self.__successful_message.is_visible()

    def get_successful_msg_text(self):
        return self.__successful_message.inner_text()

    def click_cart_btn(self):
        self.__cart_btn.click()

    def click_products_btn(self):
        self.__products_btn.click()

    def click_view_product_btn(self):
        self.__view_product_btn.click()

    def add_products_to_cart(self):
        self.__add__first_product.click()
        self.__continue_btn.click()
        self.__add_second_product.click()
        self.__continue_btn.click()

    def click_login_register_btn(self):
        self.__login_register_btn.click()

    def get_loggined_user(self):
        return self.__loggedin_user.inner_text()

    def is_category_visible(self):
        return self.__category_panel.is_visible()

    def click_women_category(self):
        self.__women_category.click()
        self.__women_subcategory.click()

    def get_category_text(self):
        return self.__category_text.inner_text()

    def click_men_category(self):
        self.__men_category.click()
        self.__men_subcategory.click()