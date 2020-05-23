class Room:

    def __init__(self, room_number, items):
        self.room_number = room_number
        self.items = items
        prices = self.items.values()
        self.total_price = sum(prices)
        
    def get_total_price(self):
        return self.total_price
    
    def get_room_number(self):
        return self.room_number
    
    def get_item_list(self):
        return self.items
    
