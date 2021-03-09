from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from SetpTest_5.Zhibo_Test.Web.SeleniumPO.page.add_peoplepage import AddPeoplePage
from SetpTest_5.Zhibo_Test.Web.SeleniumPO.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_addpeopel_page(self):
        # 点击添加“添加成员”按钮
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        # 跳转到“添加成员”详细界面
        return AddPeoplePage(self.driver)
