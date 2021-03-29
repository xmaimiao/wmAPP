from page.basepage import BasePage
from page.indexpage import Index

class Login(BasePage):
    '''
    登錄，此頁面是webview
    '''

    def switch_to_context(self):
        '''
        进入登錄頁，此頁面是webview，且正確的登錄窗口是-2
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.switch_to_window(self.driver.window_handles[-2])
        return self

    def username(self,user):
        self._params["user"] = user
        self.step("../data/login.yaml","username")
        return self

    def password(self,psd):
        self._params["psd"] = psd
        self.step("../data/login.yaml", "password")
        return self

    def click_save(self,x,y):
        '''
        點擊確認，進入首頁，確認元素無效，切回原生，頁面點擊
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[0])
        self.touch_tap(x,y)
        return Index(self.driver)
