from selenium.webdriver.common.by import By

email_field_loc = (By.XPATH, '//input[@id="email"]')
pass_field_loc = (By.XPATH, '//input[@id="pass"]')
button_sign_in_loc = (By.XPATH, '//button[@id="send2"]')
error_message_loc = (By.XPATH,'//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')