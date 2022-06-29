import logging
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, \
    ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


_module = os.path.basename(__file__)


def initialise_webdriver(context, get_url, chrome_exe_location):
    """
    This function initialise the webdriver
    :param context: behave context var
    :param get_url: url of the browser
    :param chrome_exe_location:location of chrome exe
    :return:
    """
    driver = None
    try:
        driver = webdriver.Chrome(executable_path = chrome_exe_location)
        driver.maximize_window()
        driver.implicitly_wait(50)  # seconds
        driver.get(get_url)
        return driver
    except Exception as e:

        context.logger.error('Error in initialising the webdriver : {}'.format(str(e)))
        assert False, "Initialization failed"

def create_directory_function(screenshot_local_directory):
    return os.makedirs(screenshot_local_directory, exist_ok=True)


def capture_screenshot(context,file_name,_screenshot_local_directory):
    """

    :param context:  Session Object
    :param file_name:  File name of the .png file
    :param _screenshot_local_directory: Screenshot local directory path
           Need to be present beforehand
    @return: _status : True if screenshot captured else False
    """
    _status = False
    try:
        # Relative path to save screenshot
        full_path = os.path.join(_screenshot_local_directory,file_name)
        context.logger.info(f'Trying to save screen shot at path : {full_path}')
        _status = context.catalogue_driver.save_screenshot(full_path)
    except Exception as e:
        if not context.catalogue_driver:
            context.logger.info("Not able to find the driver object"
                                               "to capture screen shot. "
                                               "Expected at session object context.catalogue_driver")

        context.logger.info("Failed to capture the screenshot")

    return _status


def action_chain_method(context):
    action_object = ActionChains(context.catalogue_driver)
    return action_object

class GetElement:

    def __init__(self, context):
        self.context = context

    def get_element_once_visible(self, locator, locator_val, timeout=15,
                                 pollFrequency=0.5):
        try:
            wait = WebDriverWait(self.context.catalogue_driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            if locator.upper() == 'ID':
                return wait.until(EC.visibility_of_element_located((By.ID, locator_val)))
            elif locator.upper() == 'NAME':
                return wait.until(EC.visibility_of_element_located((By.NAME, locator_val)))
            elif locator.upper() == 'TAG_NAME':
                return wait.until(EC.visibility_of_element_located((By.TAG_NAME, locator_val)))
            elif locator.upper() == 'CSS_SELECTOR':
                return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator_val)))
            elif locator.upper() == 'XPATH':
                return wait.until(EC.visibility_of_element_located((By.XPATH, locator_val)))
            elif locator.upper() == 'CLASS_NAME':
                return wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator_val)))
            elif locator.upper() == 'LINK_TEXT':
                return wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locator_val)))
            elif locator.upper() == 'PARTIAL_LINK_TEXT':
                return wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, locator_val)))
            else:
                raise Exception('Locator {} provided is not supported'.format(locator.upper()))
        except Exception as e:
            context.logger.info.error('Element not appeared on web page')

