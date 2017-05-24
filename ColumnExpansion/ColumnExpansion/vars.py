class vars(object):
    """Variables for the Application"""

    version="1.0"

    def __new__(cls):
        return super(vars, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(vars, self).__init__(*args, **kwargs)

