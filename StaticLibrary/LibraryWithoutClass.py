import base64


def encode_as_base64(string):
    """
    Encode string as base64.
    """
    return base64.b64encode(string.encode())


def decode_from_base64(string):
    """
    Decode string from base64.
    """
    return base64.b64decode(string).decode()


def return_length(string):
    """
    Return length of the given string
    :param string:
    :return: len(string)
    """
    return len(string)


def return_reverse(string):
    """
    Return reversed string
    :param string:
    :return: reversed string
    """
    return string[::-1]

