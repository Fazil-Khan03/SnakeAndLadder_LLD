import time
class User:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.pos = x

class Board:

    def __init__(self) -> None:
        self.cells = []
        self.snakes = {}
        self.ladders = {}
        self.user1 = None
        self.user2 = None

    def add_cells(self):
        for i in range(1,20):
            self.cells.append(i)
          
    def add_snakes(self, snakes):
        self.snakes = snakes
     
    def add_ladder(self, ladders):
        self.ladders = ladders

    def add_user(self, user_obj):
        self.user = user_obj

    def roll_dice(self, user):
        import random
        choice = random.choice([1,2,3,4,5,6])
        print("Choice For ", user.name," is :",choice)
        if choice + user.pos > 20 :
            return
        user.pos += choice  
        if user.pos in self.snakes:    
            user.pos = self.snakes[user.pos]
            print(user.name, "is bitten by snake and new position is: ",user.pos)
            print()
            return
        if user.pos in self.ladders:
            user.pos = self.ladders[user.pos]
            print(user.name, "got ladder and new position is : ", user.pos)
        print()    

class PlayGame:
    
    def create_board(self):
        board_obj = Board()
        board_obj.add_cells()
        snakes = {5:3,3:1,19:10,14:12,19:1}
        board_obj.add_snakes(snakes)
        ladders = {2:8,9:15,4:18,3:8,10:20}
        board_obj.add_ladder(ladders)
        board_obj.user1, board_obj.user2 = self.create_users()
        return board_obj

    def create_users(self):
        user1 = User("fazil", 1, 1)
        user2 = User('Manish', 1, 1)
        return user1, user2

pg = PlayGame()
board_obj = pg.create_board()

while True:
    board_obj.roll_dice(board_obj.user1)
    if board_obj.user1.pos == 20:
        print('User ', board_obj.user1.name," has won the game")
        break
    board_obj.roll_dice(board_obj.user2)
    if board_obj.user2.pos == 20:
        print('User ', board_obj.user2.name," has won the game")
        break
