def pickUpItem(self, rooms):
        """try to pick up an item"""
        if 'item' in rooms[self.currentRoom]:
            requiredStrength = rooms[self.currentRoom]['item'].get('strength', 0)
            if self.stats[0] >= requiredStrength:
                self.inventory.append(rooms[self.currentRoom]['item']['name'])
                del rooms[self.currentRoom]['item']
                print("You picked up the item.")
            else:
                print("You are not strong enough to pick up the item.")
        else:
            print("There is no item to pick up in this room.")
