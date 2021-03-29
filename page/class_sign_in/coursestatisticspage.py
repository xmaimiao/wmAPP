from page.basepage import BasePage
from page.class_sign_in.studentstatisticspage import StudentStatistics


class CourseStatistics(BasePage):

    def switch_to_window(self):
        '''
        切換到新窗口，科目-全體學生簽到統計頁面
        :return:
        '''
        self.driver.switch_to_window(self.driver.window_handles[-1])
        return self

    def stu_actual_attendance(self,staffNo):
        '''
        獲取學生實簽次數
        :return:
        # '''
        self.set_implicitly_wait(5)
        self._params["staffNo"] = staffNo
        return int(self.step("../data/class_sign_in/coursestatisticspage.yaml", "stu_actual_attendance"))

    def goto_student_statistics(self,staffNo):
        '''
        進入該科目-學生簽到統計頁面
        :return:
        '''
        self._params["staffNo"] = staffNo
        try:
            self.step("../data/class_sign_in/coursestatisticspage.yaml", "goto_student_statistics")
        except Exception as e:
            self.touch_move(1/2,1/2,9/10,1/10)
            self.step("../data/class_sign_in/coursestatisticspage.yaml", "goto_student_statistics")
        return StudentStatistics(self.driver)


