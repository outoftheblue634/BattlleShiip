
def print_board(board):
    for i in range(10):
        build_str = f"{i} |"
        print(" -----------------------------------------")
        for j in range(10):
            build_str += " " + str(board[i][j]) + " |"
        print(build_str)
    print(" -----------------------------------------")
    print("  --0   1   2   3   4   5   6   7   8   9--")

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

    def place(self, playa):

        while True:
            x = int(input(f"the 'x' placement for your {self.name} (0, 9): "))
            y = int(input(f"the 'y' placement for your {self.name} (0, 9): "))

            direction = input("In what direction do you want it: 'up', 'down', 'left', 'right': ")
            if self.out_of_bound(x, y, direction):
                print(f'This {self.name} is out of bound, please choose another place.')

            else:
                break

        if direction == 'up':
            playa[x][y] = self.id
            for i in range(self.health):
                playa[x - i][y] = self.id

        elif direction == 'down':
            playa[x][y] = self.id
            for i in range(self.health):
                playa[x + i][y] = self.id

        elif direction == 'left':
            playa[x][y] = self.id
            for i in range(self.health):
                playa[x][y - i] = self.id

        elif direction == 'right':
            playa[x][y] = self.id
            for i in range(self.health):
                playa[x][y + i] = self.id
