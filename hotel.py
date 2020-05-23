from room import Room
class Hotel:

    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms_list = []

    def get_hotel_name(self):
        return self.hotel_name
    
    def add_room(self, room_name, items):
        self.rooms_list.append(Room(room_name, items))

    def get_all_rooms(self):
        return self.rooms_list

    def get_rooms_with_budget(self, budget):
        rooms_under_budget = []
        for room in self.rooms_list:
            if room.get_total_price() <= budget:
                rooms_under_budget.append(room)
        return rooms_under_budget
    
    def remove_room(self, name):
        for room in self.rooms_list:
            if room.get_room_name() == name:
                self.rooms_list.remove(room)
    

        


    