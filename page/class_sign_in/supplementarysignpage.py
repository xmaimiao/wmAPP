from time import sleep

from page.basepage import BasePage
from page.class_sign_in.signpage import SignPage


class Supplementarysign(BasePage):
    def supplementarysign(self,remark):
        self._params["remark"] = remark
        self.driver.switch_to_window(self.driver.window_handles[-1])
        try:
            self.step("../data/class_sign_in/supplementarysignpage.yaml", "supplementarysign")
            return SignPage(self.driver)
        except Exception as e:
            print("暫無數據")
            raise e