from playwright.sync_api import Page

class DetailsPage:
    def __init__(self, page: Page):
        self.page = page
        self.__product_detail = self.page.locator('div[class="product-information"]')
        self.__quantity_box = self.page.locator('input[id="quantity"]')
        self.__add_to_cart_btn = self.page.locator("button[type='button']")
        self.__view_cart_btn = self.page.locator('a[href="/view_cart"] u')

    def change_quantity_to_4(self):
        self.__quantity_box.wait_for_selector_state('visible')
        self.__quantity_box.fill('4')

    def click_add_to_cart(self):
        self.__add_to_cart_btn.click()

    def click_view_cart(self):
        self.__view_cart_btn.click()

    def is_product_detail_visible(self):
        return self.__product_detail.is_visible()