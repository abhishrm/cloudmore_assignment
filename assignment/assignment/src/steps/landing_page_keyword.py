from behave import *
import src.steps.UI.cat_landing_page_ops as cat_landing_page
from src.steps.common.common_ui_utility import *
import re
_module = os.path.basename(__file__)

@when('user has navigated to the cloudmore landing page')
def step_impl(context):
    """
    This keyword is to make sure that user has navigated to "https://web.cloudmore.com/" page
    :param context:
    :return:
    """


    landing_page = cat_landing_page.CatLandingPageOps(context)


@then('user can verify the "{attribute}" on landing page')
def step_impl(context, attribute):
    """
    This keyword is to verify the various icons on main landing page when user has navigated to "https://web.cloudmore.com/" page
    :param context:
    :param attribute: The logo which user wants to verify
    :return:
    """


    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_attributes_on_cloudmore_landing_page(attribute), 'Verifcatiom of :{} to landing page failed'.format(attribute)

@when('user clicks the "{attribute}" on landing page')
def step_impl(context, attribute):
    """
    Keyword implemenation to click the various icon on cloudmore main landing page
    :param context:
    :param attribute:icon need to be clicked
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_attributes_on_cloudmore_landing_page(attribute,click=True), 'Click to the :{} failed on landing page'.format(attribute)


@when('user finds the "{attribute}" on cloudmore landing page and then click it')
def step_impl(context, attribute):
    """
    keyword implementation to look for search box on cloudmore landing page
    :param context:
    :param attribute:searchbox on landimg page
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._get_search_box_and_then_click_it(attribute), 'Search and click to : {} failed '.format(attribute)

@then('user can find the main "{attribute}" and can search using keyword "{search_text}"')
def step_impl(context, attribute, search_text):
    """
    Kyyword implemenation to figure out main search box and then search string in that
    :param context:
    :param attribute:Name of the searchbox need to be located
    :param search_text: string which user wants to search in the searchbox
    :return:
    """

    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._get_search_box_placeholder(attribute, search_text), 'Not able to locate and search string :{}'.format(search_text)


@then('verify that navigation happened to search result page')
def step_impl(context):
    """
    Keyword implemenation to verify the navigation occured after some text was searched in search box.
    :param context:
    :return:
    """
    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._verify_search_result_page(), 'Navigation failed to the search result page'

@then('verify that user can capture screenshot and search results has less than 3 pages, screenshot should be taken from latest result page and in case if search results has more that 3 pages than take screenshot from 3rd page')
def step_impl(context):
    """
    Keyword implemenation to figure out number of pages available after search result
    :param context:
    :return:
    """
    #mouse_object = MouseOperation()
    landing_page = cat_landing_page.CatLandingPageOps(context)

    assert landing_page._next_page_icon(),'Not able to capture screenshot as per condition'




