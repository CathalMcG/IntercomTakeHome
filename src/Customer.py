class Customer(object):
    """
    Customer

    A customer has a user_id, a name, and a location.
    """

    def __init__(self, user_id, name, location):
        """ A Customer has an id, a name, and a location """
        self._user_id = user_id
        self._name = name
        self._location = location

    """ user_id is a unique id for each customer """
    @property
    def user_id(self):
        return self._user_id
    
    """ name is the customer's full name """
    @property
    def name(self):
        return self._name

    """ location is the customer's location """
    @property
    def location(self):
        return self._location