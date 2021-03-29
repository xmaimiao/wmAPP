from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class EditPage(BasePage):
    email_ele = (MobileBy.XPATH,'//input[@class="van-field__control van-field__control--right" and @name="email"]')
    contactPhoneNo_ele = (MobileBy.XPATH,'//input[@class="van-field__control van-field__control--right" and @name="contactPhoneNo"]')
    save_ele = (MobileBy.XPATH,'//button[@class="van-button van-button--primary van-button--large van-button--block"]')

    def mailbox(self,mail):
        self.find_and_sendkeys(self.email_ele,mail)
        return self


    def contact_number(self,phone):
        self.find_and_sendkeys(self.contactPhoneNo_ele, phone)
        return self

    def click_save(self):
        self.find_and_click(self.save_ele)
        from page.storagebox.storageboxpage import StorageBoxPage
        return StorageBoxPage(self.driver)