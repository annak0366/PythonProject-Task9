# Назва файлу: __init__.py
from .cart_page import CartPage
from .checkout_page import CheckoutPage
from .deleted_account_page import DeletedAccountPage
from .home_page import HomePage
from .payment_page import PaymentPage
from .product_details_page import DetailsPage
from .products_page import ProductsPage
from .signup_login_page import SignupLoginPage

__all__ = [
    "CartPage",
    "CheckoutPage",
    "DeletedAccountPage",
    "HomePage",
    "PaymentPage",
    "DetailsPage",
    "ProductsPage",
    "SignupLoginPage",
]
