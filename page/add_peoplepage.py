from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from SetpTest_5.Zhibo_Test.Web.SeleniumPO.page.base_page import BasePage


class AddPeoplePage(BasePage):
    # 讲locator的value写成变量的形式
    def add_people_page(self, username, ausername, account, phone, aphone, mail, address, job):
        # 用户名
        self.find(By.ID, 'username').send_keys(username)
        # 别名
        self.find(By.ID, 'memberAdd_english_name').send_keys(ausername)
        # 账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 手机
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        # 座机
        self.find(By.ID, 'memberAdd_telephone').send_keys(aphone)
        # 邮箱
        self.find(By.ID, 'memberAdd_mail').send_keys(mail)
        # 地址
        self.find(By.ID, 'memberEdit_address').send_keys(address)
        # 职务
        self.find(By.ID, 'memberAdd_title').send_keys(job)
        # 保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_member(self):
        # 获取所有的联系人姓名
        # element_to_be_clickable后面传参要用元祖类型，加（）
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        # 显示等待（已经被封装过，直接调用wait_for_click方法）
        self.wait_for_click(10, locator)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        ele_lists = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # 获取联系人姓名列表，其结果展示为ele的形式
        names = []
        for ele in ele_lists:
            names.append(ele.get_attribute("title"))
            # 获取ele的title属性然后添加的names列表中
        return names
