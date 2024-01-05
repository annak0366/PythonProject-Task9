from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.__first_product = self.page.locator("//div[@class='features_items']/div[2]")
        self.__add_to_cart_btn1 = self.page.locator("//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div["
                                                    "1]//div[2]//div[1]//a[1]")
        self.__continue_btn = self.page.locator(".btn-success")
        self.__second_product = self.page.locator("//div/div[2]/div/div[3]")
        self.__add_to_cart_btn2 = self.page.locator("//div[3]//div[1]//div[1]//div[2]//div[1]//a[1]")
        self.__view_cart_btn = self.page.locator("//u[normalize-space()='View Cart']")
        self.__1st_product_price = self.page.locator('//div/div[2]/div/div[1]/div[2]/div/h2')
        self.__2nd_product_price = self.page.locator('//div[3]//div[1]//div[1]//div[2]//div[1]//h2[1]')
        self.__product_brands = self.page.locator('div[class="brands_products"]')
        self.__brand_name = self.page.locator('a[href="/brand_products/Polo"]')
        self.__brand_header = self.page.locator('h2[class="title text-center"]')
        self.__brand_breadcrumps = self.page.locator('li[class="active"]')
        self.__brand_name2 = self.page.locator('a[href="/brand_products/H&M"]')

    def add_first_product(self):
        self.__first_product.hover()
        self.__add_to_cart_btn1.click()
        self.__continue_btn.click()

    def add_second_product(self):
        self.__second_product.hover()
        self.__add_to_cart_btn2.click()

    def click_view_cart_btn(self):
        self.__view_cart_btn.click()

    def get_1st_product_price(self):
        return self.__1st_product_price.inner_text()

    def get_2nd_product_price(self):
        return self.__2nd_product_price.inner_text()

    def is_brands_visible(self):
        return self.__product_brands.is_visible()

    def click_brand_name(self):
        self.__brand_name.click()

    def get_brand_header(self):
        return self.__brand_header.inner_text()

    def get_breadcrumpts(self):
        return self.__brand_breadcrumps.inner_text()

    def click_brand_name2(self):
        self.__brand_name2.click()