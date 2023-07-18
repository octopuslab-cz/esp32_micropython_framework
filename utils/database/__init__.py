# (c) OctopusLAB 2016-23 - MIT
"""
octopusLAB - database class
"""

__version__ = "1.0.1"



class Database():
    def __init__(self):
        pass

    def write(self, *args, **kwargs):
        raise NotImplementedError("Using abstract class")
