from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import  random

class BasePage:
    TIMEOUT = 10
    alertWait = 3

    def __init__(self, driver):
        self.driver = driver

    def is_element_presented_by_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element is not None

    def get_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def insert_text_into_textfield_with_id(self, id, text):
       try:
        element = self.driver.find_element_by_id(id)
        element.send_keys(text)
       except:
        element = self.driver.find_element_by_xpath(id)
        element.send_keys(text)

    def click_button_with_id(self, id):
        element = self.driver.find_element_by_id(id)
        element.click()

    def navigate_to_page_with_url(self, url):
        self.driver.get(url)

    def wait_until_page_with_url_loaded(self, url):
        try:
            page_loaded = EC.url_to_be(url)
            WebDriverWait(self.driver, self.TIMEOUT).until(page_loaded)
        except TimeoutError:
            print("Timed out waiting for page with url - %s to load" % url)
        finally:
            print("Page with url - %s loaded" % url)

    def wait_until_receiving_journals_page_with_url_loaded(self, url):
        try:
            page_loaded = EC.url_to_be(url)
            WebDriverWait(self.driver, self.TIMEOUT).until(page_loaded)
        except TimeoutError:
            print("Timed out waiting for page with url - %s to load" % url)
        finally:
            print("Page with url - %s loaded" % url)

    def select_element_from_drop_down(self, id, text):
        select_element = Select(self.driver.find_element_by_id(id))
        select_element.select_by_value(text)

    def get_all_elements_from_dropdown(self, id):
        select_box = self.driver.find_element_by_id(id)
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        for element in options:
            return element.get_attribute("value") is not None

    def clear_text_filed(self, id):
        self.driver.find_element_by_id(id).clear()

    def are_values_match(self, id, text):
        actual_element = self.driver.find_element_by_id(id).text
        expected_element = text
        if expected_element == actual_element:
            return True
        else:
            print("Values are not matching")

    def alert_accept(self):
        try:
            WebDriverWait(self.driver, self.alertWait).until(EC.alert_is_present(),
                                                           'Timed out waiting for PA creation ' +
                                                           'confirmation popup to appear.')

            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")

    def alert_dismiss(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.dismiss()

    def alert_send_key(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.send_keys()

    def alert_text(self):
        alert_obj = self.driver.switch_to.alert
        alert_obj.text()

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def click_element_by_link_text(self, text):
        link = self.driver.find_element_by_link_text(text)
        link.click()

    def click_element_by_xpath(self, xpath):
        elements_xpath = self.driver.find_element_by_xpath(xpath)
        elements_xpath.click()

    def click_element_by_partial_link_text(self, link):
        partial_link = self.driver.find_element_by_partial_link_text(link)
        partial_link.click()

    def implicitly_wait_for_element(self, url, id):
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.find_element_by_id(id)

    def is_element_presented_by_xpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        return element is not None

    def close_last_tab(self):
        if (len(self.driver.window_handles) == 2):
            self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(window_name=self.driver.window_handles[0])

    def get_all_rows_from_page(self,xpath):
        elements= self.driver.find_elements_by_xpath(xpath)
        if(len(elements)>0):
         randomValue= random.randrange(1,len(elements))
        value= self.driver.find_element_by_xpath("(// div[ @class ='ui-grid-row ng-scope']//div[1]//div[1]/div)["+str(randomValue)+"]").text
        return value

    def insert_text_into_textfield_with_xpath(self, xpath, text):
        element = self.driver.find_element_by_xpath(xpath)
        element.send_keys(text)








