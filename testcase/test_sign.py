import pytest
import yaml
from page.app import App

with open("../data/test_sign.yaml",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    fulldatas = datas["fullattendance"]
    presentdatas = datas["present"]
    absentdatas = datas["absent"]
    get_room_type_datas = datas["get_room_type"]
    student_actual_attendance_datas = datas["student_actual_attendance"]
    student_supplementarysign_num_datas = datas["student_supplementarysign_num"]
    student_the_supplementarysign_text_datas = datas["student_the_supplementarysign_text"]
    student_the_supplementarysign_num_datas = datas["student_the_supplementarysign_num"]
    supplementarysign_datas = datas["supplementarysign"]
    test_statistics_search_datas = datas["test_statistics_search"]

class TestSign:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()
        # pass

    def setup(self):
        '''
        正常打開APP應用進入工作台
        :return:
        '''
        # self.signin = self.app.start().\
        #     goto_index().\
        #     goto_workbench().\
        #     goto_class_sign_in(self._x,self._y)
        '''
        臨時入口測試，不重新打開APP，從工作台開始
        '''
        self.start = self.app.start()

    def teardown(self):
        self.app.close()

    @pytest.mark.parametrize("data", [fulldatas])
    def test_fullattendance(self,data):
        '''
        獲取應簽到人數
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]).\
            signpage_switch_to_context().\
            current_sign_fullattendance()
        assert data["expect"] == result

        # result = self.start.goto_index().\
        #     goto_workbench(174,978).\
        #     goto_class_sign_in().\
        #     signpage_switch_to_context().\
        #     current_sign_fullattendance()
        # assert data["expect"] == result

    @pytest.mark.parametrize("data", [presentdatas])
    def test_present(self,data):
        '''
        获取已签到人数
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context().\
            current_sign_present()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [absentdatas])
    def test_absent(self,data):
        '''
        获取未到人数
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            current_sign_absent()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [get_room_type_datas])
    def test_get_room_type(self,data):
        '''
        獲取課程教室，網課-》網課，雲課堂-》雲課堂
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            get_room_type()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [student_actual_attendance_datas])
    def test_student_actual_attendance(self,data):
        '''
        檢查該科目學生實際簽到次數
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            goto_course_statistics().\
            switch_to_window().\
            stu_actual_attendance(data["staffNo"])
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [student_supplementarysign_num_datas])
    def test_student_supplementarysign_num(self,data):
        '''
        獲取該科目、該學生簽到統計頁面的補簽數量
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            goto_course_statistics().\
            switch_to_window(). \
            goto_student_statistics(data["staffNo"]).\
            switch_to_window().\
            get_supplementarysign_num()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [student_the_supplementarysign_text_datas])
    def test_student_the_supplementarysign_text(self,data):
        '''
        驗證該學生第N條記錄的補簽toast
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            goto_course_statistics(). \
            switch_to_window(). \
            goto_student_statistics(data["staffNo"]). \
            switch_to_window().\
            get_the_supplementarysign_text(data["supplementarysign_num"])
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [student_the_supplementarysign_num_datas])
    def test_student_the_supplementarysign_num(self,data):
        '''
        驗證該學生當前頁面補簽數量
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            goto_course_statistics(). \
            switch_to_window(). \
            goto_student_statistics(data["staffNo"]). \
            switch_to_window(). \
            get_supplementarysign_num()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [supplementarysign_datas])
    def test_supplementarysign(self,data):
        '''
        驗證從APP補簽成功
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context().\
            goto_supplementarysign().\
            supplementarysign(data["remark"]). \
            signpage_switch_to_context(). \
            get_suppl_current_sign_present()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", [test_statistics_search_datas])
    def test_statistics_search(self,data):
        '''
        檢查簽到統計頁面查詢功能
        '''
        result = self.start. \
            goto_index(). \
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context().\
            goto_statistics().\
            search_courses(data["value"])
        assert data["expect"] == result






