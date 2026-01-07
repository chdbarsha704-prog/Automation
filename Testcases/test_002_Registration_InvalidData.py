from Base.InitiateDriver import startBrowser,closeBrowser

def test_Validate_Invalid_Data_Registration():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='firstname']").send_keys('12345')
    driver.find_element('xpath',"//input[@name='lastname']").send_keys('0000')
    closeBrowser()
