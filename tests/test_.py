import pytest
from pytest import mark
from faker import Faker
from playwright.sync_api import Page, sync_playwright
from data.user_data import user_data
from pages import CartPage, CheckoutPage, DeletedAccountPage, HomePage, PaymentPage, DetailsPage, ProductsPage, \
    SignupLoginPage
from utils.tools import take_screenshot
fake = Faker()


@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def cart_page(page):
    return CartPage(page)
@pytest.fixture
def details_page(page):
    return DetailsPage(page)
@pytest.fixture
def pr_page(page):
    return ProductsPage(page)
@pytest.fixture
def signup_page(page):
    return SignupLoginPage(page)
@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
@pytest.fixture
def payment_page(page):
    return PaymentPage(page)
@pytest.fixture
def deleted_acc_page(page):
    return DeletedAccountPage(page)

@pytest.mark.parametrize("email", [fake.email()])
def test_10_verify_subscription_in_home_page(page: Page, email, home_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    page.evaluate("document.querySelector('footer').scrollIntoView()")
    assert home_page.get_footer_text() == "SUBSCRIPTION"
    home_page.fill_subscribe_data(email)
    assert home_page.is_successful_message_visible()
    assert home_page.get_successful_msg_text() == "You have been successfully subscribed!"
    take_screenshot(page, "subscription_home_page")

@pytest.mark.parametrize("email", [fake.email()])
def test_11_verify_subscription_in_cart_page(page: Page, email, home_page, cart_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.click_cart_btn()
    page.evaluate("document.querySelector('footer').scrollIntoView()")
    assert cart_page.get_footer_text() == "SUBSCRIPTION"
    cart_page.fill_subscribe_data(email)
    assert cart_page.is_successful_msg_visible()
    assert cart_page.get_successful_msg() == "You have been successfully subscribed!"
    take_screenshot(page, "ndkndwk")

def test_12_add_products_in_cart(page: Page, cart_page, home_page, pr_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.click_products_btn()
    first_price = pr_page.get_1st_product_price()
    second_price = pr_page.get_2nd_product_price()
    pr_page.add_first_product()
    pr_page.add_second_product()
    pr_page.click_view_cart_btn()
    assert cart_page.verifying_products_added()
    assert first_price == cart_page.get_1st_product_price() and second_price == cart_page.get_2nd_product_price()
    assert cart_page.get_1st_pr_quantity() == '1' and cart_page.get_2nd_pr_quantity() == '1'
    assert cart_page.get_1st_total_price() == first_price and cart_page.get_2nd_total_price() == second_price

def test_13_verify_product_quantity_in_cart(page: Page, details_page, home_page, cart_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.click_view_product_btn()
    details_page.is_product_detail_visible()
    details_page.change_quantity_to_4()
    details_page.click_add_to_cart()
    details_page.click_view_cart()
    assert cart_page.get_1st_pr_quantity() == '4'


@pytest.mark.parametrize("name, email, password, address, city, zipcode, phone_number, text",
                         [(fake.name(), fake.email(), fake.password(), fake.address(), fake.city(), fake.zipcode(),
                          fake.phone_number(), fake.text())])
def test_14_register_while_checkout(page: Page, name, email, password, address, city, zipcode, phone_number, text,
                                   home_page, cart_page, signup_page, checkout_page, payment_page, deleted_acc_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.add_products_to_cart()
    home_page.click_cart_btn()
    assert cart_page.get_breadcrumbs() == 'Shopping Cart'
    cart_page.click_checkout_btn()
    cart_page.click_login_register_btn()
    signup_page.fill_signup_form(name, email, password, address, city, zipcode, phone_number)
    assert signup_page.get_header() == 'ACCOUNT CREATED!'
    signup_page.click_continue_btn()
    assert home_page.get_loggined_user() == f' Logged in as {name}'
    home_page.click_cart_btn()
    cart_page.click_checkout_btn()
    assert checkout_page.check_address_details().replace('\n', ' ') == address.replace('\n', ' ')
    checkout_page.fill_description_field(text)
    card_number = fake.random_number(digits=8)
    cvc = fake.random_number(digits=3)
    random_month = f"{fake.random_int(min=1, max=12):02d}"
    random_year = fake.random_int(min=2010, max=2050)
    payment_page.enter_payment_details(name, str(card_number), str(cvc), str(random_month), str(random_year))
    assert payment_page.get_success_message() == 'Congratulations! Your order has been confirmed!'
    deleted_acc_page.click_delete_account_btn()
    assert deleted_acc_page.get_header_text() == 'ACCOUNT DELETED!'
    deleted_acc_page.click_continue_btn()


@pytest.mark.parametrize("name, email, password, address, city, zipcode, phone_number, text",
                         [(fake.name(), fake.email(), fake.password(), fake.address(), fake.city(),
                           fake.zipcode(), fake.phone_number(), fake.text())])
def test_15_register_before_checkout(page: Page, name, email, password, address, city, zipcode, phone_number, text,
                                  home_page, signup_page, cart_page, checkout_page, payment_page, deleted_acc_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.click_login_register_btn()
    signup_page.fill_signup_form(name, email, password, address, city, zipcode, phone_number)
    assert signup_page.get_header() == 'ACCOUNT CREATED!'
    signup_page.click_continue_btn()
    assert home_page.get_loggined_user() == f' Logged in as {name}'
    home_page.add_products_to_cart()
    home_page.click_cart_btn()
    assert cart_page.get_breadcrumbs() == 'Shopping Cart'
    cart_page.click_checkout_btn()
    assert checkout_page.check_address_details().replace('\n', ' ') == address.replace('\n', ' ')
    checkout_page.fill_description_field(text)
    card_number = fake.random_number(digits=8)
    cvc = fake.random_number(digits=3)
    random_month = f"{fake.random_int(min=1, max=12):02d}"
    random_year = fake.random_int(min=2010, max=2050)
    payment_page.enter_payment_details(name, str(card_number), str(cvc), str(random_month), str(random_year))
    assert payment_page.get_success_message() == 'Congratulations! Your order has been confirmed!'
    deleted_acc_page.click_delete_account_btn()
    assert deleted_acc_page.get_header_text() == 'ACCOUNT DELETED!'
    deleted_acc_page.click_continue_btn()

@pytest.mark.parametrize("text", [fake.text()])
def test_16_login_before_checkout(page: Page, text, home_page, signup_page, cart_page, checkout_page, payment_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.click_login_register_btn()
    signup_page.fill_login_data(user_data["email"], user_data["password"])
    assert home_page.get_loggined_user() == f' Logged in as {user_data["name"]}'
    home_page.add_products_to_cart()
    home_page.click_cart_btn()
    assert cart_page.get_breadcrumbs() == 'Shopping Cart'
    cart_page.click_checkout_btn()
    assert checkout_page.check_address_details().replace('\n', ' ') == user_data["address"].replace('\n', ' ')
    checkout_page.fill_description_field(text)
    card_number = fake.random_number(digits=8)
    cvc = fake.random_number(digits=3)
    random_month = fake.random_int(min=1, max=12)
    formatted_month = f"{random_month:02d}"
    random_year = fake.random_int(min=2010, max=2050)
    payment_page.enter_payment_details(user_data["name"], str(card_number), str(cvc), str(formatted_month), str(random_year))
    assert payment_page.get_success_message() == 'Congratulations! Your order has been confirmed!'

def test_17_remove_products_from_cart(page: Page, home_page, cart_page):
    page.goto("https://www.automationexercise.com")
    assert home_page.logo_is_visible()
    home_page.add_products_to_cart()
    home_page.click_cart_btn()
    assert cart_page.get_breadcrumbs() == 'Shopping Cart'
    cart_page.delete_products_from_cart()
    assert cart_page.get_empty_cart_text() == 'Cart is empty!'

def test_18_view_category_products(page: Page, home_page):
    page.goto("https://www.automationexercise.com")
    home_page.is_category_visible()
    home_page.click_women_category()
    assert home_page.get_category_text() == 'WOMEN - DRESS PRODUCTS'
    home_page.click_men_category()
    assert home_page.get_category_text() == 'MEN - TSHIRTS PRODUCTS'

def test_19_view_cart_brand_products(page: Page, home_page, pr_page):
    page.goto("https://www.automationexercise.com")
    home_page.click_products_btn()
    assert pr_page.is_brands_visible()
    pr_page.click_brand_name()
    assert pr_page.get_brand_header() == 'BRAND - POLO PRODUCTS' and pr_page.get_breadcrumpts() == 'Polo'
    pr_page.click_brand_name2()
    assert pr_page.get_brand_header() == 'BRAND - H&M PRODUCTS' and pr_page.get_breadcrumpts() == 'H&M'
