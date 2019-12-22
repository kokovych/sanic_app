import re

from jsonschema import validate, FormatChecker
from jsonschema.exceptions import ValidationError
from passlib.hash import sha256_crypt

from src.db.model import get_user_by_email, get_user_fields

ERR_MSG_UNIQUE_EMAIL = "User with this email is already exist"

USER_CREATION = {
    "type": "object",
    "properties": {
        "email":
            {
                "format": "email"
            },
        "password":
            {
                "type": "string",
                "minLength": 8
            },
    },
    "required": [
        "email", "password"
    ],
}

draft7_format_checker = FormatChecker()


def generate_error_dict(error_type, error_msg):
    return {error_type: error_msg}


def get_validation_error_msg(err):
    err_msg = err.message
    err_type = err.path[0]
    err_msg = re.sub("'.*?'", '', err_msg, 1)
    return {
        err_type: err_msg.strip().replace('\'', '')
    }


def clean_user_data(data):
    correct_fields = get_user_fields()
    result = {}
    for attr_name in correct_fields:
        result[attr_name] = data.get(attr_name)
    # hash password:
    raw_password = result.get('password')
    if raw_password:
        result['password'] = sha256_crypt.hash(raw_password)
    return result


async def registration_valid_data(data, conn):
    try:
        validate(instance=data, schema=USER_CREATION, format_checker=draft7_format_checker)
    except ValidationError as err:
        err_data = get_validation_error_msg(err)
        return err_data
    email = data.get('email')
    user = await get_user_by_email(conn, email)
    if user:
        return generate_error_dict(error_type='email', error_msg=ERR_MSG_UNIQUE_EMAIL)
