import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed(), "There is no button to add item"
