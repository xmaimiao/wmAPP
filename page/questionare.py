from page.backtomain import BackToMain
from page.basepage import BasePage


class Questionare(BasePage):
    def question(self):
        '''
        此頁面是webview，故要切換上下文，填寫健康申報表
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.step("../data/questionare.yaml", "question")
        return BackToMain(self.driver)

