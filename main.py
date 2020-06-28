from hotel import Hotel
hotel_list = []
def create_hotel():
    print("Existing Hotel List")
    print("==========================================================")
    hotel_names = []
    for hotel in hotel_list:
        hotel_names.append(hotel.get_hotel_name())
        print(hotel.get_hotel_name())
    print("===========================================================")
    hotel_name = input("Enter Hotel Name \n")    
    if hotel_name in hotel_names:
        print("Hotel already exists")
    else:
        hotel_list.append(Hotel(hotel_name))

def add_hotel_room():
    print("Existing Hotel List")
    print("==========================================================")
    hotel_names = []
    for hotel in hotel_list:
        hotel_names.append(hotel.get_hotel_name())
        print(hotel.get_hotel_name())
    print("===========================================================")
    hotel_name = input("Enter Hotel Name where the room is to be added \n")
    if hotel_names.count(hotel_name) == 0:
        print("===========================================================")
        print("Hotel Name Invalid!")
        print("===========================================================")
        return    
    try:
        for hotel in hotel_list:
           if hotel.get_hotel_name() == hotel_name:
                room_names =[]
                for room in hotel.get_all_rooms():
                    room_names.append(room.get_room_number())
                print("Room Numbers already there : {}".format(room_names))
        room_number = int(input("Enter Room Number \n"))    
        if room_number in room_names:
            print ("room already exists")
        else:
            items = dict()
            while True:
                item_name = input("Enter Item Name : \n")
                try:
                    item_price = float(input("Enter Item Price (in $): \n"))
                    items[item_name] = item_price
                except ValueError:
                    print("Enter Valid Price")
                
                user_choice = input("Add another item? (Y/N)  ")
                if user_choice == 'N' or user_choice == 'n':
                    break
            print("Adding")
            for hotel in hotel_list:

                if hotel.get_hotel_name() == hotel_name:
                    print("Added")
                    hotel.add_room(room_number, items)
    except ValueError:
        print("Room Number cannot be a string")


    
def print_all_rooms():
    print("Existing Hotel List")
    print("==========================================================")
    for hotel in hotel_list:
        print(hotel.get_hotel_name())
    print("===========================================================")
    hotel_name = input("Select Hotel Name \n")
    
    for hotel in hotel_list:
        if hotel.get_hotel_name() == hotel_name:
            
            print("Rooms List")
            print("===========================================================")
            for room in hotel.get_all_rooms():
                print("Room Number : {}".format(room.get_room_number()))
                print("Room Item List")
                for item, price in room.get_item_list().items():
                    print("{} : ${}".format(item,price))
            print("===========================================================")

def print_rooms_under_budget():
    try:
        budget = float(input("Enter estimate budget (in $) \n"))
        
        rooms_count = 0
        print("===========================================================")
        print("Hotels under your budget")
        print("===========================================================")
        for hotel in hotel_list:
            rooms = hotel.get_rooms_with_budget(budget)
            if len(rooms)>0:
                print("Hotel {}".format(hotel.get_hotel_name()))
                for room in rooms:
                    rooms_count = rooms_count+1
                    print("Room Number : {}".format(room.get_room_number()))
                    print("Total Price : ${}".format(room.get_total_price()))
                print("===========================================================")    

        if rooms_count == 0:
            print("No rooms under specified budget")
        print("===========================================================")
    except ValueError:
        print("Enter valid price")


while True:
    print("1. Add Hotel")
    print("2. Add Room")
    print("3. Print Rooms")
    print("4. Rooms under budget")
    print("5. Exit")

    try:
        choice = int(input("Enter the desired choice \n"))
        if choice == 1:
            create_hotel()
        elif choice == 2:
            if len(hotel_list)>0:
                add_hotel_room()
            else:
                print("No Hotel present")
        elif choice == 3:
            if len(hotel_list)>0:
                print_all_rooms()
            else:
                print("No Hotel present")
        elif choice == 4:
            if len(hotel_list)>0:
                print_rooms_under_budget()
            else:
                print("No Hotel present")
        elif choice == 5:
            print("Byee")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter valid choice please")    
        






