import logging
import requests


class UsersEndpoint(object):

    def __init__(self, context):
        self.context = context
        self.main_url = 'https://petstore.swagger.io/v2/user'

        self.standalone_user_endpoint_url = self.main_url + '/user'
        self.create_with_array_url = self.main_url + '/createWithArray'
        self.create_users_list_url = self.main_url + '/createWithList'
        self.modify_users_url = self.main_url + '/<user_name>'
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.context.logger.handlers.pop()


    def _type(self):
        return self.__class__.__name__

    def get_logger(self):
        return logging.getLogger(self.context.logger_name + '.' + self._type())

    def create_user(self, json, which_type_of_endpoint):
        """
        This method is user to call user POST endpoint.
        :param json:
        :param which_type_of_endpoint:createWithArray/createWithList/user
        :return: tuple of respone status code and response text
        """

        if which_type_of_endpoint == 'createWithArray':
            create_user_url = self.create_with_array_url
        elif which_type_of_endpoint == 'createWithList':
            create_user_url = self.create_users_list_url
        elif which_type_of_endpoint == 'standalone_user_endpoint':
            create_user_url = self.standalone_user_endpoint_url

        response = requests.post(create_user_url, headers=self.headers, json=json)
        self.context.logger.info('created user status code : %s' % response.status_code)
        self.context.logger.info('create user : %s' % response.text)
        return response.status_code, response.json()

    def get_user(self, user_name):
        """
        This method is user to call user GET endpoint.
        :param user_name: user_name
        :return: tuple of returned user metadata and status code
        """
        get_url = self.modify_users_url.replace("<user_name>", user_name)
        response = requests.get(get_url,  headers=self.headers)
        self.context.logger.info('get user status code: %s' % response.status_code)
        self.context.logger.info('get a user : %s' % response.text)
        return response.status_code, response.json()

    def update_user(self, user_name, json):
        """
        This method is user to call user PUT endpoint.
        :param user_name: user_name to be updated
        :param json: input json for user
        :return: tuple of returned user metadata and status code
        """
        get_url = self.modify_users_url.replace("<user_name>", user_name)
        response = requests.put(get_url, headers=self.headers, json=json)
        self.context.logger.info('updated user status code : %s' % response.status_code)
        self.context.logger.info('updated user : %s' % response.text)
        return response.status_code, response.json()

    def delete_user(self, user_name):
        """
        This method is user to call user DELETE endpoint.
        :param user_name: user to be deleted
        :return: tuple of returned user status code and string
        """
        get_url = self.modify_users_url.replace("<user_name>", user_name)
        response = requests.delete(get_url, headers=self.headers)
        self.context.logger.info('delete user status code : %s' % response.status_code)
        self.context.logger.info('delete user text : %s' % response.text)
        return response.status_code,'deleted'


