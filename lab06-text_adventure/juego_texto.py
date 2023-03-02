
class Room:
    """
    Esta clase representa la habitación del juego
    """
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west



def main():

    room_list = []

    room_1 = Room("Habitaion pequeña", None, 2, 4, None)
    room_list.append(room_1)
    room_2 = Room("Salón principal", 5, None, None, 1)
    room_list.append(room_2)
    room_3 = Room("Cocina", None, 2, None, 4)
    room_list.append(room_3)
    room_4 = Room("Recepcion superior", 5, 0, 3, 1)
    room_list.append(room_4)
    room_0 = Room("Recepcion inferior", 4, None, 2, 5)
    room_list.append(room_0)
    room_5 = Room("Habitacion principal", 1, None, 0, None)
    room_list.append(room_5)
    room_6 = Room("Balcon", None, 4, None, None)
    room_list.append(room_6)

    current_room = 0

    done = False

    while(done == True) :
        print(room_list[current_room].description)
        print("\n")
        movimiento = input("¿Que quieres hacer?")
        print(movimiento)

        if(movimiento == "N" or movimiento == "n" or movimiento =="North" or movimiento == "north" or movimiento == "NoRtH"):
            next_room = room_list[current_room].north
            if(movimiento == "None"):
                print("No puedes ir a la nada")
                current_room = next_room


main()





