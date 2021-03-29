import yaml

from page.app import App
import pytest

def get_params(name):
    with open("../data/test_login.yaml", encoding="utf-8") as f:
        datas = yaml.load(f)[name]
        data = datas.values()
        return data

class TestLogin:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start()

    @pytest.mark.parametrize("user,psd,login_x,login_y,work_x,work_y",[get_params("login")])
    def test_goin_and_questionare(self,user,psd,login_x,login_y,work_x,work_y):
        '''
        1.登錄页面输入账号
        2.完善健康申報表
        3.返回到首頁
        4.進入工作台
        :return:
        '''
        self.main.goto_login().\
            switch_to_context().\
            username(user).\
            password(psd).click_save(login_x,login_y).\
            goto_questionare().question().\
            backtomain().goto_workbench()

    def test_questionare(self):
        '''
        1.已登录，无须进入登录页面
        2.完善健康申報表
        3.返回到首頁
        4.進入工作台
        :return:
        '''
        self.main.goto_index().\
            goto_questionare().\
            question().\
            backtomain().goto_workbench()


    @pytest.mark.parametrize("user,psd,login_x,login_y,work_x,work_y",[get_params("login")])
    def test_lgoin(self,user,psd,login_x,login_y,work_x,work_y):
        '''
        登錄，無需填寫申報，打開工作臺
        :return:
        '''
        self.main.goto_login(). \
            switch_to_context(). \
            username(user). \
            password(psd).\
            click_save(login_x,login_y).\
            goto_workbench(work_x,work_y)

