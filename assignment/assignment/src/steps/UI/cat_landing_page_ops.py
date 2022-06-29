from .cat_landing_page_locators import *
from src.steps.common import common_ui_utility
import logging
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
from src.steps.common.common_utility import read_config_file



class CatLandingPageOps(object):
    """
    This Class conatin all the methods to locate all the elements from the cloudmore landing page and search related methos
    """
    def __init__(self, context):
        self.context = context
        self.get_elem_obj = common_ui_utility.GetElement(self.context)

    def _type(self):
        return self.__class__.__name__


    def _verify_attributes_on_cloudmore_landing_page(self, attribute,click=None):
        if click is not None:
            return_value= self.get_elem_obj.get_element_once_visible(*elements_on_landing_page[attribute])
            return_value.click()
            time.sleep(2)
            return return_value
        else:
            return self.get_elem_obj.get_element_once_visible(*elements_on_landing_page[attribute])

    def _get_search_box_and_then_click_it(self,attribute):
        self.get_elem_obj.get_element_once_visible(*elements_related_to_search_box[attribute]).click()
        return True

    def _get_search_box_placeholder(self, attribute, search_text):
        ele = self.get_elem_obj.get_element_once_visible(*elements_related_to_search_box[attribute])

        ele.send_keys(search_text)
        ele.send_keys("\n")
        return True

    def _verify_search_result_page(self):
        self.get_elem_obj.get_element_once_visible(*elements_related_to_search_box['SEARCH_RESULT_TITLE'])
        return True

    def _next_page_icon(self):

        ##Read data from config file
        config = read_config_file(self.context.path_config_file)
###This is just a dry run to capture screenshot#####
        screenshot_local_directory = config['configuration_setting']['screenshot_local_directory']
        screenshot_file_name = config['configuration_setting']['screenshot_file_name']
        common_ui_utility.create_directory_function(screenshot_local_directory)
        captured_status = common_ui_utility.capture_screenshot(self.context, screenshot_file_name, screenshot_local_directory)

        time.sleep(10)
        if captured_status:
            self.context.logger.debug('screenshot captured with filename'.format(screenshot_file_name))
        else:
            self.context.logger.debug('Not able to capture screenshot captured with filename'.format(screenshot_file_name))

        ###This is call to make action class object so that we can carry out click on element
        actions = common_ui_utility.action_chain_method(self.context)

        ##This below variable is to keep track of how many times next page button appears on screen when user keep on clicking next page button icon
        no_of_times_next_page_icon_visible =0

        def common_function_to_capture():
            captured_status = common_ui_utility.capture_screenshot(self.context, screenshot_file_name,
                                                                   screenshot_local_directory)
            time.sleep(10)
            if captured_status:
                self.context.logger.debug('screenshot captured with filename'.format(screenshot_file_name))
            else:
                self.context.logger.debug(
                    'Not able to capture screenshot captured with filename'.format(screenshot_file_name))

        try:

            ###Here we need to keep on clicking the Next page button till the time user see next page button.
            #On every page next page clcik turn ,if user see Next button then we need to increase count value of  no_of_times_next_page_icon_visible
            #Once user do not see the next page button, then exception would get raise.
            #This help us to know how many pages are there with next page
            while True:
                ###The below thing is to scroll down so that next page button gets visible on the screen
                self.context.catalogue_driver.execute_script("window.scrollTo(900,1200);")
                element_located = self.get_elem_obj.get_element_once_visible(*elements_related_to_search_box['NEXT_PAGE_ICON'])

                actions.move_to_element(menu).click().perform()
                no_of_times_next_page_icon_visible += 1

                ###This below condition means that if there are more than 3 pages then we should not click anymore the next button
                ##Once this condition is fulfilled,we should take screenshot at page no 3 and should bail out with break statement
                if no_of_times_next_page_icon_visible == 3:
                    self.context.logger.debug('This means the no of pages with Next page button are more than 3,hence we should take screenshot now')
                    self.context.logger.debug('Calling screenshot capture function')
                    common_function_to_capture()
                    break


        except Exception as e:
            self.context.logger.debug('We could not find next page button')
            self.context.logger.debug('No of pages discovered so far :{} '.format(no_of_times_next_page_icon_visible))
            self.context.logger.debug('Exception raised is :{}'.format(str(e)))


        if no_of_times_next_page_icon_visible < 3:
            self.context.logger.debug(
                'This means the no of pages with Next page button are less than 3,hence we should navigate back and take screenshot after navigating back')
            self.context.catalogue_driver.back()
            self.context.logger.debug('Calling screenshot capture function')
            common_function_to_capture()

        return True



