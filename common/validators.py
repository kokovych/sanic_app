import re
from jsonschema import validate, FormatChecker
from jsonschema.exceptions import ValidationError


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


def get_validation_error_msg(err):
    err_msg = err.message
    err_type = err.path[0]
    err_msg = re.sub("'.*?'", '', err_msg, 1)
    return {
        err_type: err_msg.strip().replace('\'', '')
    }


def create_user_validation(data):
    try:
        validate(instance=data, schema=USER_CREATION, format_checker=draft7_format_checker)
    except ValidationError as err:
        err_data = get_validation_error_msg(err)
        return err_data
