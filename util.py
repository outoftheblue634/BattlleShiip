import pickle
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def print_board(board):
    for i in range(10):
        build_str = f"{i} |"
        print(" -----------------------------------------")
        for j in range(10):
            build_str += " " + str(board[i][j]) + " |"
        print(build_str)
    print(" -----------------------------------------")
    print("  --0   1   2   3   4   5   6   7   8   9--")


def create_boat():
    cruiser = Boat('cruiser')
    destroyer = Boat('destroyer')
    aircraft = Boat('aircraft')
    submarine = Boat('submarine')
    recon = Boat('recon')

    boat_name_dict = {0: cruiser, 1: destroyer, 2: aircraft, 3: submarine, 4: recon}
    return boat_name_dict


def place_boats(tab, num_of_boat):
    print_board(tab)
    boat_name_dict = create_boat()
    for i in range(num_of_boat):
        boat_name_dict[i].place(tab)
        print_board(tab)

    return boat_name_dict


def valid_shot(x, y):
    if x > 9 or x < 0:
        return False
    elif y > 9 or y < 0:
        return False
    else:
        return True


def take_a_shot(tab):
    print_board(tab)
    while True:
        x_shot = int(input("Where do you want to shoot (x): "))
        y_shot = int(input("Where do you want to shoot (y): "))
        if valid_shot(x_shot, y_shot):
            print(f'You shot at ({x_shot}, {y_shot})')
            break
        else:
            print('invalid shot')

    return pickle.dumps(x_shot, y_shot)


def receive_a_shot(received, tabb, boat_name_dict):
    unpickled = pickle.loads(received)
    x_received = unpickled[0]
    y_received = unpickled[1]

    if tabb[x_received, y_received] == 0:
        s.send(pickle.dumps("Missed!"))

    elif tabb[x_received, y_received] == 'X':
        s.send(pickle.dumps("Already shot there"))
    else:
        boat_name_dict[tabb[x_received, y_received]].got_hit()
        s.send(pickle.dumps("Hit!"))


def tab_adjust(mes, tabw, x, y):
    if pickle.loads(mes) == "Missed!":
        tabw[x][y] = 'W'
    elif pickle.loads(mes) == "Already shot there":
        pass
    elif pickle.loads(mes) == "Hit!":
        tabw[x][y] = 'X'

def lose_a_life(player_lives):
    player_lives -= 1
    if player_lives == 0:
        return True
    else:
        return False



class Boat:

    def __init__(self, name):
        self.name = name

        if self.name == 'cruiser':
            self.id = 1
            self.health = 5

        elif self.name == 'destroyer':
            self.id = 2
            self.health = 3

        elif self.name == 'aircraft':
            self.id = 3
            self.health = 6
            self.name = 'aircraft carrier'

        elif self.name == 'submarine':
            self.id = 4
            self.health = 3

        elif self.name == 'recon':
            self.id = 5
            self.health = 2
            self.name = 'recon boat'

        self.current_health = self.health

    def out_of_bound(self, x, y, direction):
        if direction == 'up':
            if x - self.health < 0:
                return True
        elif direction == 'down':
            if x + self.health > 9:
                return True
        elif direction == 'left':
            if y - self.health < 0:
                return True
        elif direction == 'right':
            if y + self.health > 9:
                return True
        else:
            return False

    def place(self, player):

        while True:
            x = int(input(f"the 'x' placement for your {self.name} (0, 9): "))
            y = int(input(f"the 'y' placement for your {self.name} (0, 9): "))

            direction = input("In what direction do you want it: 'up', 'down', 'left', 'right': ")
            if self.out_of_bound(x, y, direction):
                print(f'This {self.name} is out of bound, please choose another place.')

            else:
                break

        if direction == 'up':
            player[x][y] = self.id
            for i in range(self.health):
                player[x - i][y] = self.id

        elif direction == 'down':
            player[x][y] = self.id
            for i in range(self.health):
                player[x + i][y] = self.id

        elif direction == 'left':
            player[x][y] = self.id
            for i in range(self.health):
                player[x][y - i] = self.id

        elif direction == 'right':
            player[x][y] = self.id
            for i in range(self.health):
                player[x][y + i] = self.id

    def is_dead(self):
        if self.current_health == 0:
            return True
        else:
            return False

    def got_hit(self):
        self.current_health -= 1
