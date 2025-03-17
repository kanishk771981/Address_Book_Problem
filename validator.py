import re
from exceptions import UserFieldValidationEror

def validate_data(data_dict):
    """
        
    Validates the data in a dictionary based on specific rules for each field.

    Parameters:
    
    data_dict : dict
        The dictionary containing data to be validated.

    Returns:
    
    dict
        A dictionary with validated data.

    Raises:
    
    ValueError
        If any field does not meet the validation criteria.
    
    """
    validated_data = {}

    for key, value in data_dict.items():
        if key.endswith("first_name"):
            if re.fullmatch(r'^[A-Z][a-z]{2,}$', value):  
                validated_data[key] = value
            else:
                raise UserFieldValidationEror("Invalid first name. It must start with a capital letter and have at least 2 lowercase letters.")

        elif key.endswith("last_name"):
            if re.fullmatch(r'^[A-Z][a-z]{2,}$', value): 
                validated_data[key] = value
            else:
                raise UserFieldValidationEror("Invalid last name. It must start with a capital letter and have at least 2 lowercase letters.")

        elif key.endswith("phone_num"):
            if re.fullmatch(r'^\d{10}$', value): 
                validated_data[key] = value
            else:
                raise UserFieldValidationEror("Invalid phone number. It must be exactly 10 digits.")

        elif key.endswith("email"):
            if re.fullmatch(r'^[A-Za-z\d._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', value):  
                validated_data[key] = value
            else:
                raise UserFieldValidationEror("Invalid email format.")
        elif key.endswith("zip_code"):
            if re.fullmatch(r'^\d{6}$',value):
                validated_data[key] = value
            else:
                raise UserFieldValidationEror("Invalid phone number. It must be exactly 6 digits.")

        else:
            validated_data[key] = value  

    return validated_data


def validation_wrapper(func):
    """
     A decorator to handle data validation before executing a function.

    Parameters:
    
    func : function
        The function to be executed after validation.

    Returns:
    
    function
        A wrapped function that performs validation first."""
    def wrapper(data_dict):
        try:
            validated_data = validate_data(data_dict)
            return func(validated_data)
        except UserFieldValidationEror as e:
            print(f"Validation error: {e}")
            return None
    return wrapper

@validation_wrapper
def validate_user_data(data_dict):
    """
    Function to return validated user data.

    Parameters:
    
    data_dict : dict
        The dictionary containing user data.

    Returns:
    
    dict
        The validated data dictionary.
    """
    return data_dict
