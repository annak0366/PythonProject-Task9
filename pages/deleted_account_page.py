from playwright.sync_api import Page

class DeletedAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.__continue_btn_deleted_account = self.page.locator('a[data-qa="continue-button"]')
        self.__deleted_account_header = self.page.locator('h2[data-qa="account-deleted"] b')

    def click_delete_account_btn(self):
        self.__delete_account_btn.click()

    def get_header_text(self):
        return self.__deleted_account_header.inner_text()

    def click_continue_btn(self):
        self.__continue_btn_deleted_account.click()