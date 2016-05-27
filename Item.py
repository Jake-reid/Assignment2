"""
Created a class to use for items in items for hire
"""

class Items:
    """
    initialization
    """
    def __init__(self, item=[]):
        self.Name = item[0]
        self.Desc = item[1]
        self.Pric = str(item[2])
        self.Avai = item[3]
    #Handles the display of a * if the item is already hired
    def is_available(self):
        if self.Avai == "out":
            return "*"
        else:
            return""
   # Printing format of items
    def __str__(self):
        return "{}: {:<50} = {}{}".format(self.Name, self.Desc, self.Pric, self.is_available())

