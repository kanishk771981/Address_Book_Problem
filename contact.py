
class Contact:
    """
    A class to represent a contact with various attributes.

    Attributes:
    kwargs : dict
        A dictionary of attributes (e.g., fname, lname, address, city, state, zip_code, phone_num, email).

    Methods:
    __str__():
        Returns a string representation of the contact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Contact instance with dynamic attributes.

        Parameters:
        kwargs : dict
            Key-value pairs of attributes to set.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        """
        Returns a formatted string representing the contact's information.
        """
        return f"{getattr(self, 'fname', '')} {getattr(self, 'lname', '')}, {getattr(self, 'address', '')}, {getattr(self, 'city', '')}, {getattr(self, 'state', '')}, {getattr(self, 'zip_code', '')}, {getattr(self, 'phone_num', '')}, {getattr(self, 'email', '')}"