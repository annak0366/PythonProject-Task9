from playwright.sync_api import Page
class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.__subscribe_text = self.page.locator('h2')
        self.__email_input = self.page.locator('[id="susbscribe_email"]')
        self.__subscribe_button = self.page.locator('[id="subscribe"]')
        self.__successful_msg = self.page.locator('[id="success-subscribe"]')
        self.__first_product = self.page.locator('[id="product-1"]')
        self.__second_product = self.page.locator('[id="product-2"]')
        self.__1st_product_price = self.page.locator("tr[id='product-1'] td[class='cart_price'] p")
        self.__2nd_product_price = self.page.locator("tr[id='product-2'] td[class='cart_price'] p")
        self.__1st_pr_quantity = self.page.locator("tr[id='product-1'] button")
        self.__2nd_pr_quantity = self.page.locator("tr[id='product-2'] button")
        self.__1st_total_price = self.page.locator("tr[id='product-1'] p[class='cart_total_price']")
        self.__2nd_total_price = self.page.locator("tr[id='product-2'] p[class='cart_total_price']")
        self.__checkout_btn = self.page.locator(".btn-default.check_out")
        self.__breadcrumpb = self.page.locator("ol.breadcrumb li.active")
        self.__login_regist_btn = self.page.locator('a[href="/login"] u')
        self.__adress_checkout = self.page.locator("ul[id='address_delivery'] li:nth-child(4)")
        self.__first_product_name = self.page.locator('h4 a[href="/product_details/1"]')
        self.__second_product_name = self.page.locator('h4 a[href="/product_details/2"]')
        self.__delete1_btn = self.page.locator('a[data-product-id="1"]')
        self.__delete2_btn = self.page.locator('a[data-product-id="2"]')
        self.__empty_cart_text = self.page.locator('p[class="text-center"] b')

    def get_footer_text(self):
        return self.__subscribe_text.inner_text()

    def fill_subscribe_data(self, email):
        self.__email_input.fill(email)
        self.__subscribe_button.click()

    def is_successful_msg_visible(self) -> bool:
        return self.__successful_msg.is_visible()

    def get_successful_msg(self):
        return self.__successful_msg.inner_text()

    def verifying_products_added(self) -> bool:
        return self.__first_product.is_visible() and self.__second_product.is_visible()

    def get_1st_product_price(self):
        return self.__1st_product_price.inner_text()

    def get_2nd_product_price(self):
        return self.__2nd_product_price.inner_text()

    def get_1st_pr_quantity(self):
        return self.__1st_pr_quantity.inner_text()

    def get_2nd_pr_quantity(self):
        return self.__2nd_pr_quantity.inner_text()

    def get_1st_total_price(self):
        return self.__1st_total_price.inner_text()

    def get_2nd_total_price(self):
        return self.__2nd_total_price.inner_text()

    def click_checkout_btn(self):
        self.__checkout_btn.click()

    def get_breadcrumbs(self):
        return self.__breadcrumpb.inner_text()

    def click_login_register_btn(self):
        self.__login_regist_btn.click()

    def delete_products_from_cart(self):
        self.__delete1_btn.click()
        self.__delete2_btn.click()

    def get_empty_cart_text(self):
        return self.__empty_cart_text.inner_text()