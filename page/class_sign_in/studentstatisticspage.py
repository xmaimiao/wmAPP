from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class StudentStatistics(BasePage):
    def switch_to_window(self):
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return self

    def get_supplementarysign_num(self):
        '''
        獲取該課程-該學生當前屏幕內所有補簽次數，若數據>12不適用
        :return:
        '''
        self.set_implicitly_wait(5)
        try:
            result = self.step("../data/class_sign_in/studentstatisticspage.yaml",
                         "get_supplementarysign_num")
            return result
        except Exception as e:
            print("暫無補簽數據")
            raise e

    def get_the_supplementarysign_text(self,supplementarysign_num):
        sleep(2)
        self._params["supplementarysign_num"] = supplementarysign_num
        return self.step("../data/class_sign_in/studentstatisticspage.yaml",
                  "get_last_supplementarysign_text")
