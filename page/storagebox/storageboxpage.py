from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from page.basepage import BasePage
from page.storagebox.personinfo import PersonInfo


class StorageBoxPage(BasePage):

    perinfo_ele = (MobileBy.XPATH,'//button[@class="van-button van-button--primary van-button--normal van-button--block"]')
    text_ele = (MobileBy.XPATH, "//*[contains(@text,'添加成功')]")

    def complete_personinfo(self):
        self.webdriver_wait_click(self.perinfo_ele)
        self.find_and_click(self.perinfo_ele)
        return PersonInfo(self.driver)

    def toast(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])
        toast = self.find(self.text_ele).text
        return toast

    # def goto_apply(self):
    #     return ApplyPage(self.driver)

    def setting(self):
        return self

    def set_goto_apply(self):
        return ApplyPage(self.driver)

    def set_personinfo(self):
        pass

    def set_help(self):
        pass

    def set_history(self):
        pass

    def set_unlock(self):
        pass