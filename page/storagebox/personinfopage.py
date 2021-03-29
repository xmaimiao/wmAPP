from time import sleep

from page.basepage import BasePage
from page.settingpage import Setting


class PersonInfo(BasePage):
    def goto_setting(self,x,y):
        '''
        非原生頁面，切換上下文
        無法定位設置元素，原生頁面坐標點擊
        :return:
        '''
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # self.step("../data/personinfopage.yaml","goto_setting")
        sleep(2)
        self.touch_tap(x,y)
        return Setting(self.driver)
