from pages.login_page import LoginPage
from pages.inventory_page import InvPage

def test_successful_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in page.url

def test_locked_out_user_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")
    
    assert login.error_msg_visible()

def test_add_to_cart(page):
    login = LoginPage(page)
    inv= InvPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    inv.addtocart()
    assert inv.cart_badge_count() == "1"