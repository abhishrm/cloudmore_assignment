import string
import random
import secrets
import configparser

def random_string_generator():
    random_string_formed= ''.join(random.choices(string.ascii_uppercase +
                           string.digits, k=10))
    return random_string_formed


def read_config_file(path_config_file):
    try:

        config = configparser.ConfigParser()
        config.read(path_config_file)
        return config

    except Exception as e:
        assert False, "Failed to read config file :{}".format(e)

def random_string_only_char():
    return ''.join(secrets.choice(string.ascii_uppercase)
            for i in range(10)).lower()
class UsersMgmtFunctions(object):

    def __init__(self, context):
        self.context = context

    def populate_users_json(self,):
        """
        method to populate user input json
        :return: returns a dictionary containing user input json
        """

        try:


            users_info = {
                          "data": {
                            "attributes": {
            "id": 0,
            "username": "string"+random_string_only_char().lower(),
            "firstName": "string"+ random_string_only_char().lower(),
            "lastName": "string"+ random_string_only_char().lower(),
            "email": "string"+random_string_only_char().lower(),
            "password": "string"+random_string_only_char().lower(),
            "phone": "string"+ random_string_only_char().lower(),
            "userStatus": 0
}
                          }}
            return users_info
        except:
            raise

    def compare_users_json(self, input_users_info, output_users_info):
        """
        This methos is used to compare the input set during POST/PATCH input json against the GET endpoint json.
        :param input_users_info:
        :param output_users_info:
        :return:
        """
        try:

            keys = input_users_info.keys()

            for key in keys:
                if key == 'id':
                    continue
                if type(input_users_info[key]) == list and type(output_users_info[key]) == list:
                    input_users_info[key].sort()
                    output_users_info[key].sort()
                if input_users_info.get(key) != output_users_info.get(key):
                    raise Exception('Users info :{} does not match, expected:{} , got:{}'.format(
                        key, input_users_info.get(key), output_users_info.get(key)
                    ))
        except:
            raise