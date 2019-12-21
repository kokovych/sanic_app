from jsonschema import validate
from jsonschema.exceptions import ValidationError


USER_CREATION = {
    "type" : "object",
    "properties" : {
        "email" : {"type" : "string"},
        "password" : {"type" : "string"},
     },
    "required": ["email", "password"],
}


def create_user_validation(data):
    print(data)
    try:
        validate(instance=data, schema=USER_CREATION)
    except ValidationError as err:
        print('ERROR!')
        print(err)
        return False
    return True
