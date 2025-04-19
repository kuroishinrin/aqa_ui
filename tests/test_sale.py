
def test_sale_page_title(sale_page):
    text_data = 'Sale'
    sale_page.open_page()
    sale_page.check_page_title(text_data)