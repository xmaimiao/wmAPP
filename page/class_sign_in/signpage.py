from time import sleep

from page.basepage import BasePage
from page.class_sign_in.statisticspage import Statistics


class SignPage(BasePage):
    def signpage_switch_to_context(self):
        '''
        打开上課签到應用，切换webview
        :return:
        '''
        self.driver.switch_to.context(self.driver.contexts[-1])
        # app file:///data/user/0/cn.doocom.WeMustDEV/cache/modules/S-WM-CLASS-TIMETABLE-OA/www/index.html
        return self

    def change_classroom(self):
        pass

    def roll_call(self):
        return self

    def statistics(self):
        return self

    def current_sign_present(self):
        '''
        獲取當前已簽到人數
        :return:
        '''
        return int(self.step("../data/class_sign_in/signpage.yaml","current_sign_present"))

    def current_sign_fullattendance(self):
        '''
        獲取當前應簽到人數
        :return:
        '''
        return int(self.step("../data/class_sign_in/signpage.yaml","current_sign_fullattendance"))

    def current_sign_absent(self):
        '''
        獲取當前未到（需補簽）人數
        :return:
        '''
        return int(self.step("../data/class_sign_in/signpage.yaml","current_sign_absent"))

    def goto_statistics(self):
        '''
        打開統計列表頁面
        :return:
        '''
        self.step("../data/class_sign_in/signpage.yaml", "goto_statistics")
        return Statistics(self.driver)

    def get_room_type(self):
        '''
        獲取課室類型
        :return:
        '''
        return self.step("../data/class_sign_in/signpage.yaml", "get_room_type")

    def goto_course_statistics(self):
        '''
        進入科目統計頁面
        :return:
        '''
        self.step("../data/class_sign_in/signpage.yaml", "goto_course_statistics")
        from page.class_sign_in.coursestatisticspage import CourseStatistics
        return CourseStatistics(self.driver)

    def goto_supplementarysign(self):
        '''
        進行補簽
        :return:
        '''
        self.step("../data/class_sign_in/signpage.yaml", "goto_supplementarysign")
        from page.class_sign_in.supplementarysignpage import Supplementarysign
        return Supplementarysign(self.driver)

    def get_suppl_current_sign_present(self):
        '''
        獲取補簽成功，已出席人數
        :return:
        '''
        self.driver.switch_to_window(self.driver.window_handles[0])
        return int(self.step("../data/class_sign_in/signpage.yaml", "get_suppl_current_sign_present"))

