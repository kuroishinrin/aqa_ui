
def test_incorrect_login(login_page):
    text_input = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    login_page.open_page()
    login_page.fild_login_form('qweqwe@ewqe.com', 'qweqweqwe')
    login_page.check_error_alert(text_input)

def test_correct_login(login_page):
    text_input = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'
    login_page.open_page()
    login_page.fild_login_form('qweqwe@email.com', 'non-non-non')
    login_page.check_error_alert(text_input)


