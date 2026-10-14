class InvPage:
    def __init__(self, page):
        self.page = page
        self.cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def  addtocart(self):
         self.cart_button.click()

    def cart_badge_count(self):
        return self.cart_badge.inner_text()
