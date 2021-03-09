from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from SetpTest_5.Zhibo_Test.Web.SeleniumPO.page.main_page import MainPage


class TestAddpeople:

    def setup(self):
        # 实例化主页类
        self.main = MainPage()

    def test_addmember(self):
        username = 'name3'
        ausername = 'name23'
        account = '130003'
        phone = '13211111113'
        aphone = '0571-11111113'
        mail = '1219964093@qq.com'
        address = '江南大道'
        job = '部门经理'
        page = self.main.goto_addpeopel_page()
        # 一个测试用例中可以用多个assert断言，page是将都会用到的部分定义出来，然后通过page去调用其他的方法
        page.add_people_page(username, ausername, account, phone, aphone, mail, address, job)
        # 调用添加联系人page，需要传入添加联系人所需要的locator
        names = page.get_member()
        # 调用获取联系人page，
        print(names)
        assert username in names
        # 断言
