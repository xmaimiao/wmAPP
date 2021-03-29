from time import sleep
from page.basepage import BasePage
from page.class_sign_in.signpage import SignPage
from page.storagebox.storageboxpage import StorageBoxPage


class WorkBench(BasePage):

    def goto_storagebox(self,x,y):
        sleep(3)
        self.touch_tap(x, y)
        self.touch_tap(x, y)
        self.driver.switch_to.context(self.driver.contexts[-1])
        return StorageBoxPage(self.driver)

    def goto_class_sign_in(self,x,y):
        sleep(1)
        self.touch_tap(x, y)
        self.touch_tap(x, y)
        return SignPage(self.driver)

    # def goto_class_sign_in(self):
    # '''進入上課簽到應用，目前無法定位元素'''
    #     self.driver.switch_to.context(self.driver.contexts[-1])
    #     self.driver.switch_to_window(self.driver.window_handles[-3])
    #     print(self.driver.current_context)
    #     print(self.driver.contexts)
    #     print(self.driver.current_url)
    #     self.step("../data/app.yaml","goto_class_sign_in")
    #     return SignPage(self.driver)
