from pages.login_page import LoginPage

def test_successful_login(page):
    x = LoginPage(page)
    x.navigate()
    x.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in page.url

def test_locked_out_user_login(page):
    x = LoginPage(page)
    x.navigate()
    x.login("locked_out_user", "secret_sauce")
    
    assert x.error_msg()