print("Let's play Battleship!!")

player1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_board(board):
    for i in range(10):
        stri = "|"
        print("-----------------------------------------")
        for j in range(10):
            stri += " " + str(board[i][j]) + " |"
        print(stri)
    print("-----------------------------------------")


class boat:

    def __init__(self, lives, name):
        self.lives = lives
        self.name = name

    def define_id(self):
        if self.name == 'cruiser':
            self.id = 1

        elif self.name == 'destroyer':
            self.id = 2

        elif self.name == 'aircraft':
            self.id = 3

        elif self.name == 'submarine':
            self.id = 4

        elif self.name == 'frigate':
            self.id = 5

    def place_boat(self, playa):
        x = int(input(f"the 'x' placement for your {self.name}: "))
        y = int(input(f"the 'y' placement for your {self.name}: "))

        dir = input("In which direction do you want it: 'up', 'down', 'left', 'right': ")

        if dir == 'up':
            playa[x][y] = self.id
            for i in range(self.lives):
                playa[x - i][y] = self.id

        elif dir == 'down':
            playa[x][y] = self.id
            for i in range(self.lives):
                playa[x + i][y] = self.id

        elif dir == 'left':
            playa[x][y] = self.id
            for i in range(self.lives):
                playa[x][y - i] = self.id

        elif dir == 'right':
            playa[x][y] = self.id
            for i in range(self.lives):
                playa[x][y + i] = self.id
