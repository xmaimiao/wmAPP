import pytest
import yaml

from page.app import App

with open("../data/test_sign_all.yaml",encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    get_room_type_datas = datas["test_get_room_type"]
    supplementarysign_datas = datas["test_supplementarysign"]

class TestSignAll:
    '''
    驗證多個賬號的課程類型
    '''
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        '''
        正常打開APP應用進入工作台
        :return:
        '''
        self.login = self.app.start().goto_login()

    def teardown(self):
        x=522
        y=986
        self.app.close().goto_person_info(520, 979). \
            goto_setting(293, 485). \
            logout(285, 263)

    @pytest.mark.parametrize("data", get_room_type_datas)
    def test_get_room_type(self,data):
        '''
        獲取課程教室，網課-》網課，雲課堂-》雲課堂
        '''
        result = self.login. \
            switch_to_context(). \
            username(data["username"]).password(data["password"]).click_save(286,444).\
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            get_room_type()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", supplementarysign_datas)
    def test_supplementarysign(self,data):
        '''
        驗證從APP補簽成功
        '''
        result = self.login. \
            switch_to_context(). \
            username(data["username"]).password(data["password"]).click_save(286,444).\
            goto_workbench(174, 978). \
            goto_class_sign_in(data["signin_x"], data["signin_y"]). \
            signpage_switch_to_context(). \
            goto_supplementarysign().\
            supplementarysign(data["remark"]). \
            signpage_switch_to_context(). \
            get_suppl_current_sign_present()
        assert data["expect"] == result
