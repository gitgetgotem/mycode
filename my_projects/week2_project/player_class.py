class Player:
    def __init__(self, inventory, rooms):
        self.inventory = inventory
        self.currentRoom = 'Hall'
        self.options = []
        self.health = []
        self.ability = []

    def showStatus(self, rooms):
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print('You are in the ' + self.currentRoom)
        # print what the player is carrying
        print('Inventory:', self.inventory)
        # check if there's an item in the room, if so print it
        if "item" in rooms[self.currentRoom]:
            print('You see a ' + rooms[self.currentRoom]['item'])
        print("---------------------------")
