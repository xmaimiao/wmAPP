from time import sleep

from appium import webdriver
from page.basepage import BasePage
from page.class_sign_in.signpage import SignPage
from page.login import Login
from page.indexpage import Index
from page.workbench import WorkBench


class App(BasePage):
    # dev
    _package = 'cn.doocom.WeMustDEV'
    _activity = 'io.dcloud.PandoraEntryActivity'
    # uat
    # _package = 'cn.doocom.WeMustUAT'
    # _activity = 'io.dcloud.PandoraEntryActivity'
    def start(self):
        '''
        启动APP
        :return:
        '''
        if self.driver == None:
            caps = dict()
            caps["platformName"] = 'Android'
            caps["deviceName"] = '127.0.0.1:7555'
            caps["platformVersion"] = '6.0.1'
            caps["appPackage"] = self._package
            caps["automationName"] = 'uiautomator2'
            caps["appActivity"] = self._activity
            caps["noReset"] = 'true'
            # 启动之前不关闭APP
            caps["dontStopAppOnReset"] = 'true'
            caps["skipDeviceInitializati"] = 'true'
            # 輸入中文增加的兩個設置參數
            # caps["unicodeKeyboard"] = 'true'
            # caps["resetKeyboard"] = 'true'
            caps["chromedriverExecutable"] = r'C:\Users\mai\AppData\Local\Programs\Appium\chromedriver2.20.exe'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.start_activity(self._package,self._activity)
        self.set_implicitly_wait(3)
        return self

    def stop(self):
        '''
        停止APP
        :return:
        '''
        self.driver.quit()

    def restart(self):
        '''
        重启APP
        '''
        self.driver.close()
        # 启动应用
        self.driver.launch_app()
        return self

    def close(self):
        '''
        關閉當前頁面
        '''
        self.driver.switch_to.context(self.driver.contexts[0])
        self.step("../data/app.yaml", "close")
        sleep(1)
        return self

    def goto_login(self):
        '''
        进入登錄頁
        '''
        return Login(self.driver)

    def goto_index(self):
        '''
        進入首頁
        '''
        return Index(self.driver)

    def goto_workbench(self):
        '''
        臨時入口，進入工作台
        '''
        return WorkBench(self.driver)

    def goto_class_sign_in(self,x,y):
        '''
        臨時入口，在工作台進入其他应用
        '''
        self.touch_tap(x, y)
        return SignPage(self.driver)

    # def goto_class_sign_in(self):
    #     '''
    #     臨時入口，在工作台進入其他应用
    #     :return:
    #     '''
    #     self.driver.switch_to.context(self.driver.contexts[-1])
    #     self.driver.switch_to_window(self.driver.window_handles[-3])
    #     print(self.driver.current_context)
    #     print(self.driver.contexts)
    #     print(self.driver.current_url)
    #     self.step("../data/app.yaml","goto_class_sign_in")
    #     return SignPage(self.driver)

    def goto_person_info(self,x,y):
        '''
       臨時入口，打開個人頁面
       '''
        # 通過相對位置定位進入工作台
        self.touch_tap(x, y)
        from page.storagebox.personinfopage import PersonInfo
        return PersonInfo(self.driver)


