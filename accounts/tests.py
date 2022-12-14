from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:/Users/hiroc/Downloads/chromedriver_win32/chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        #　ログインページを開く
        self.selenium.get('http://localhost:8000/' + str(reverse_lazy('account_login')))

        #　ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('<rossipythonia@gmail.com>')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('<naka1202>')
        self.selenium.find_element_by_name('btn').click()

        #ページタイトルの検証
        self.assertEquals('日記一覧|PrivateDiary', self.selenium.title)