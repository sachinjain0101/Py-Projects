class Hello(object):
    """description of class"""

    def __new__(cls):
        return super(Hello, cls).__new__()

    def __init__(self, *args, **kwargs):
        return super(Hello, self).__init__(*args, **kwargs)


