from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."

def test_add_product_in_busket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_busket()
    page.solve_quiz_and_get_code()
    page.checking_message_about_successful_addition_of_the_product_to_the_store()
