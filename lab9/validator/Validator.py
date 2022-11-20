import jsonschema.exceptions
from jsonschema import validate

class Validator:
    def validate(data, scheme):
        try:
            validate(instance=data, schema=scheme)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True
