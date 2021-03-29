from time import sleep

from page.basepage import BasePage


class Setting(BasePage):
    def logout(self,x,y):
        '''
        無法定位“退出登錄”元素
        在原生頁面上進行元素點擊操作
        :return:
        '''
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.current_url)
        # self.step("../data/settingpage.yaml", "logout")
        sleep(2)
        self.touch_tap(x,y)
        self.touch_tap(x, y)
        from page.login import Login
        return Login(self.driver)
