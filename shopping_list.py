# TODO: Press either Option + C on MacOS or Alt + C on Windows on a new line.
class ShoppingList:
    """
     A class to represent a list items to buy.  
    """

    def __init__(self):  # Constructor
        """
        Initializes the list of items to buy.
        """
        self.items = []
    def add_item(self, item):   # Method
        """
        Adds an item to the list.
        """
        self.items.append(item)