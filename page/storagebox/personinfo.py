from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.storagebox.editpage import EditPage


class PersonInfo(BasePage):
    edit_ele = (MobileBy.XPATH,'//button[@class="van-button van-button--primary van-button--large van-button--plain van-button--block"]')
    def goto_editpage(self):
        # print(f"在個人信息頁面打印url1:{self.driver.current_url}")
        # print(f"在個人信息頁面打印上下文1:{self.driver.current_context}")
        # print(f"在個人信息頁面打印上下文2:{self.driver.current_context}")
        # print(f"在個人信息頁面打印窗口句柄:{self.driver.window_handles}")
        # print(f"在個人信息頁面打印當前窗口句柄1:{self.driver.current_window_handle}")
        self.driver.switch_to_window(self.driver.window_handles[-1])
        # print(f"在個人信息頁面打印窗口句柄:{self.driver.window_handles}")
        # print(f"在個人信息頁面打印當前窗口句柄2:{self.driver.current_window_handle}")
        # print(f"在個人信息頁面打印上下文3:{self.driver.current_context}")
        # print(f"在個人信息頁面打印url2:{self.driver.current_url}")
        self.find_and_click(self.edit_ele)
        return EditPage(self.driver)