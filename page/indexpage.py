from time import sleep
from page.basepage import BasePage
from page.storagebox.personinfopage import PersonInfo
from page.workbench import WorkBench

class Index(BasePage):
    def message(self):
        '''
        消息相关
        '''
        pass

    def goto_workbench(self,x,y):
        '''
        进入到工作台
        '''
        sleep(10)
        # 通過相對位置定位進入工作台
        self.touch_tap(x,y)
        self.touch_tap(x, y)
        return WorkBench(self.driver)



    def goto_questionare(self):
        '''
        进入健康申報，此頁面是原生
        '''
        # 通過相對位置定位,先进入工作台，再点击消息打开健康申报表页面
        self.step("../data/index.yaml","index")
        from page.questionare import Questionare
        return Questionare(self.driver)

    def goto_person_info(self,x,y):
        '''
        打開個人頁面
        '''
        sleep(10)
        # 通過相對位置定位進入“我的”
        self.touch_tap(x, y)
        return PersonInfo(self.driver)

