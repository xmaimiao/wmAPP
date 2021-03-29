from time import sleep
from page.basepage import BasePage
from page.class_sign_in.coursestatisticspage import CourseStatistics


class Statistics(BasePage):

    def goto_course_statistics_scoll(self,course_code,x1,x2,y1,y2):
        '''
        切換到新窗口，滾動一次，查找科目
        '''

        self.driver.switch_to.context(self.driver.contexts[0])
        self.touch_move(x1,x2,y1,y2)
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self._params["course_code"] = course_code
        self.step("../data/class_sign_in/statisticspage.yaml", "goto_course_statistics_scoll")
        return CourseStatistics(self.driver)

    def goto_course_statistics(self,course_code):
        '''
        切換到新窗口，不滾動查找科目
        '''
        self.driver.switch_to_window(self.driver.window_handles[-1])
        # app file:///data/user/0/cn.doocom.WeMustDEV/cache/modules/S-WM-CLASS-TIMETABLE-OA/www/statistics-course-list.html
        self._params["course_code"] = course_code
        self.step("../data/class_sign_in/statisticspage.yaml", "goto_course_statistics")
        return CourseStatistics(self.driver)

    def search_courses(self,value):
        '''
        查找科目  ，輸入科目名稱、編號
        '''
        self._params["value"] = value
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return self.step("../data/class_sign_in/statisticspage.yaml","search_courses")
