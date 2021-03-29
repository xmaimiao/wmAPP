from page.app import App
import pytest

class TestBox:
    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.index = self.app.start().goto_index()

    def teardown(self):
        # self.app.back(5)
        self.app.close()

    def test_personinfor(self):
        '''
        应用的坐标根据账号不同有变化，要实时更新
        :return:
        '''
        email = "76@qq.com"
        phone = "85857569"
        x=95
        y=807
        result = self.index.goto_workbench(x,y).goto_storagebox().\
            complete_personinfo().goto_editpage().\
            mailbox(email).contact_number(phone).\
            click_save().toast()
        assert "保存成功" in result

# if __name__ == '__main__':
#     pytest.main()
