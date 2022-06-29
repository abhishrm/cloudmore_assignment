import logging
from behave import *
from src.steps.common.common_utility import *
from src.steps.API.users_endpoint import UsersEndpoint
import random
import os

_module = os.path.basename(__file__)


@When('user tries to create a user "{name}" with all the fields by using API endpoint as "{which_type_of_endpoint}"')
@When('user tries to creates multiple user "{name}" with all the fields by using API endpoint as "{which_type_of_endpoint}"')
@When('user tries to create a user "{name}" with all the fields but with field "{field}" "{missing}" by using API endpoint as "{which_type_of_endpoint}"')
@When('user tries to create a user "{name}" with all the fields but with field "{field}" as "{missing}" by using API endpoint as "{which_type_of_endpoint}"')
@When('user tries to create a user "{name}" with all the fields but with field "{field}" with "{missing}" by using API endpoint as "{which_type_of_endpoint}"')
def step_impl(context, name,which_type_of_endpoint, field=None, missing=None):
    """
    Keyword implemantion to create user using POST endpoint for createWithArray/createWithList
    :param context:
    :param name:name of the user
    :param which_type_of_endpoint: createWithArray or createWithList
    :param field: payload key parameter
    :param missing: string
    :return:
    """
    try:
        if not hasattr(context, 'users_output_list'):
            context.users_output_list = {}

        if not hasattr(context, 'username'):
            context.username = {}

        if not hasattr(context, 'users_input'):
            context.users_input = {}

        user_mgmt = UsersMgmtFunctions(context)
        users_info_data = []

        if ',' in name:
            all_users = name.split(",")
            users_info_data = [ user_mgmt.populate_users_json()['data']['attributes'] for i in range(len(all_users)) ]


        else:
            users_info = user_mgmt.populate_users_json()
            context.users_input[name] = users_info

            if field is not None and missing is not None:

                if field == 'all_the_fields' and missing == 'missing':

                    users_info['data']['attributes'] ={}
                elif field == 'as' and missing == 'wrong_parameters':
                    users_info['data']['attributes'] ={random_string_generator():random_string_generator() , random_string_generator(): random_string_generator(), random_string_generator():random_string_generator()}
                elif field and missing == 'empty string':

                    users_info['data']['attributes'][field] = ''

                elif field and missing == 'trailing spaces':

                    users_info['data']['attributes'][field] =     users_info['data']['attributes'][field] +  '        '

                elif field and missing == 'leading spaces':

                    users_info['data']['attributes'][field] = '     '  +  users_info['data']['attributes'][field]


                else:

                    del users_info['data']['attributes'][field]
            else:
                context.username[name] = users_info['data']['attributes']['username']


            users_info_data.append(users_info['data']['attributes'])


        users_response = context.users_obj.create_user(users_info_data, which_type_of_endpoint)
        context.users_output_list[name] = users_response

    except Exception as e:
        context.logger.error('user creation failed using endpoint:{0}'.format(str(e)))
        raise


@Then('user gets "{status_code}" and can verify user details in response json of user "{name}"')
@Then('user gets "{status_code}" and can verify user details in response json of user "{name}"')
def step_impl(context, status_code,name):
    """
    Keyword implemenation to verify POST call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """
    users_mgmt = UsersMgmtFunctions(context)
    try:

        if int(status_code) != context.users_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.users_output_list[name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise



@When('user tries to get user "{name}" by its name')
@When('user tries to get user "{name}" by "{invalid_user_name}"')
def step_impl(context, name, invalid_user_name = None):
    """
    Keyword implementation to get user using GET endpoint of the user.
    :param context:
    :param name:
    :param invalid_user_name:
    :return:
    """
    try:
        if not hasattr(context, 'get_users_output_list'):
            context.get_users_output_list = {}

        users_mgmt = UsersMgmtFunctions(context)

        if invalid_user_name is not None:
            name_of_the_user = random_string_generator()

        else:

            name_of_the_user = context.username[name]



        users_response = context.users_obj.get_user(name_of_the_user)
        context.get_users_output_list[name] = users_response


    except Exception as e:
        context.logger.error('user creation failed using endpoint:{0}'.format(str(e)))
        raise


@Then('user gets "{status_code}" and can verify user details in response json of user "{name}" under get response')
def step_impl(context, status_code,name):
    """
    Keyword implemenation to verify GET call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """
    users_mgmt = UsersMgmtFunctions(context)
    try:

        if int(status_code) != context.get_users_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.get_users_output_list[name][0]))

        if status_code ==200:
            users_mgmt.compare_users_json(context.users_input[name]['data']['attributes'],
                                      context.get_users_output_list[name][1])



        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise

@When('user tries to update user "{name}"')
@When('user tries to update user "{name}" with "{parameter_type}" parameters')
def step_impl(context,name, parameter_type= None):
    """
    Keyword implemenation to edit user info using PUT endpoint of the user.
    :param context:
    :param name:
    :param parameter_type:
    :return:
    """
    try:

        if not hasattr(context, 'update_users_output_list'):
            context.update_users_output_list = {}

        if not hasattr(context, 'users_input'):
            context.users_input = {}

        name_of_the_user = context.username[name]

        user_mgmt = UsersMgmtFunctions(context)
        users_info = user_mgmt.populate_users_json()

        context.users_input[name] = users_info

        if parameter_type is not None:
            if parameter_type == 'no_payload':
                users_info['data']['attributes']= {}
            else:
                users_info['data']['attributes'] ={random_string_generator() : random_string_generator()}

        users_response = context.users_obj.update_user(name_of_the_user, users_info['data']['attributes'])
        context.update_users_output_list[name] = users_response

    except Exception as e:
        context.logger.error('user creation failed using endpoint:{0}'.format(str(e)))
        raise

@Then('user gets "{status_code}" and can verify user details in response json of user "{name}" under patch response')
def step_impl(context, status_code,name):
    """
    Keyword implemenation to verify PUT call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """
    users_mgmt = UsersMgmtFunctions(context)
    try:

        if int(status_code) != context.update_users_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.update_users_output_list[name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise

@When('user tries to delete user "{name}"')
def step_impl(context,name):
    """
    Keyword implemenation to delete user info using DELETE endpoint of the user.
    :param context:
    :param name:
    :return:
    """
    try:
        if not hasattr(context, 'delete_users_output_list'):
            context.delete_users_output_list = {}

        if name == 'invalid_user':
            name_of_the_user = random_string_generator()

        else:

            name_of_the_user = context.username[name]


        users_response = context.users_obj.delete_user(name_of_the_user)

        context.delete_users_output_list[name] = users_response

    except Exception as e:
        context.logger.error('user creation failed using endpoint:{0}'.format(str(e)))
        raise

@Then('user gets "{status_code}" and can verify user details in response json of user "{name}" under delete response')
def step_impl(context, status_code,name=None):
    """
    Keyword implemenation to verify DELETE call status codes
    :param context:
    :param status_code:return code from the endpoint call
    :param name:name of the user created
    :return:
    """
    users_mgmt = UsersMgmtFunctions(context)
    try:

        if int(status_code) != context.delete_users_output_list[name][0]:
            raise Exception("Status code is not as per expectation, expected: {0}, got: {1}".format
                                (status_code, context.delete_users_output_list[name][0]))

        context.logger.info('#############Successfully Verified status code ################## ')

    except Exception as e:
        context.logger.error("user status code/details match failed using endpoint:{0}".format(str(e)))
        raise