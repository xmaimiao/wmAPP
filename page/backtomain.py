from page.basepage import BasePage
from page.indexpage import Index


class BackToMain(BasePage):
    def backtomain(self):
        '''
        返回頁面，此頁面是webview頁面，與健康申報填寫頁面是同一個webview
        :return:
        '''
        self.step("../data/backtomain.yaml", "backtomain")
        # 切回原生頁面，進入首頁，進行觸屏操作
        self.driver.switch_to.context(self.driver.contexts[0])
        return Index(self.driver)