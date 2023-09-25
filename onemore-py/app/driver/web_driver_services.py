from flask import request, make_response
from flask_restful import Resource
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.test_case.testcase_models import TestCase, TestCaseSchema
from app.utils.session_validation import is_valid_user
from server import db
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import app.utils.custom_logger as cl
import logging
import time
import os


class OneMoreExecutor():
    log = cl.customLogger(logging.DEBUG)
    driver = None
    var_dict = None

    def __init__(self):
        return OneMoreExecutor

    def open_application(self, test_suite):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(test_suite['application'])
        self.driver = browser
        self.execute_test_suite(self, test_suite['id'])

    def execute_test_suite(self, testsuite_id):
        testcase_list = self.get_all_test_case(test_suite=testsuite_id)
        for testcase in testcase_list:
            self.execute_test_case(self, testcase)

    def execute_test_case(self, testcase):
        testcase_details = testcase.test_case_details
        if testcase_details['selector_group'] != None:
            testcase_selector_group = testcase_details['selector_group']
            element = None
            if testcase_selector_group['id_selector']['is_selected']:
                element = self.waitForElement(self, testcase_selector_group['id_selector']['selector'], 'id')
            if testcase_selector_group['xpath_selector']['is_selected']:
                element = self.waitForElement(self, testcase_selector_group['xpath_selector']['selector'], 'xpth')
            if testcase_selector_group['css_selector']['is_selected']:
                element = self.waitForElement(self, testcase_selector_group['css_selector']['selector'], 'css')
            if element != None:
                if testcase.test_case_type == 'ENTER_VALUE':
                    self.sendKeys(self, data=testcase_details['action']['eneter_value']['value'])
                elif testcase.test_case_type == 'CLICK':
                    element.click()
                elif testcase.test_case_type == 'READ_VALUE':
                    self.var_dict[testcase_details['action']['read']['var_name']] = self.getText(self, element=element)
                elif testcase.test_case_type == 'VALIDATE':
                    

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(self, locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and locatorType: " + locatorType)
        return element

    def get_all_test_case(test_suite):
        result = db.session.query(TestCase).filter(
            TestCase.test_suite == test_suite).all()
        db.session.close()
        schema = TestCaseSchema(many=True)
        return result

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatorType + "not correct/supported")
        return False

    def click(self, element=None):
        try:
            element.click()
            self.log.info("Clicked on element")
        except:
            self.log.error("cannot click on element")
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def clearKeys(self, locator="", locatorType="id", element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Clear data of element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("cannot clear data of the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator +
                               " and locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " and locatorType: " + locatorType)
            else:
                self.log.error("Element is not displayed with locator: " + locator +
                               " and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is not displayed with locator: " + locator +
                           " and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator="", locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((ByType, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url

        return currentURL

    def pageBack(self):
        '''
        page back the browser
        '''
        self.driver.execute_script("window.history.go(-1)")

    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error("Failed to get " + attribute + " in element with locator: " +
                           locator + " and locatorType: " + locatorType)
            print_stack()
            attribute_value = None
        return attribute_value

    def refresh(self):
        self.driver.get(self.driver.current_url)
