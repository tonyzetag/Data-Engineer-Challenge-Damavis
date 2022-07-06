import numpy as np

class Board:
    
    def __init__(self, n, m):
        assert n == int(n), "n must be int"
        assert m == int(m), "m must be int"
        assert n >= 1 and n <=10, "1 ≤ n ≤ 10"
        assert m >= 1 and m <=10, "1 ≤ m ≤ 10"

        self.n = n
        self.m = m
        
    def to_array(self):
        return np.array([self.n, self.m], dtype=np.int8)  
    
    def Snake(self, *args):
        self.snake = self.Inner_Snake(*args, board=self.to_array())
        
    def Depth(self, n):
        self.depth = self.Inner_Depth(n)
        
    def start(self):
        # All Paths in Board
        paths_in_board = set((n,m) for n in range(self.n) for m in range(self.m))
        
        # Paths ocupated by Snake
        paths_ocupated = [(n[0], n[1]) for n in self.snake.args]
        
        snakes = []
        snakes.append(paths_ocupated)
        mov = np.array([[1,0], [-1,0], [0,1], [0,-1]])
        
        for n in range(self.depth.n):
            new_snakes = []
            for snake in snakes:
                # Adjacents
                path_new = set((element[0], element[1]) for element in snake[0] + mov)

                # Inside the board
                path_new = set.intersection(path_new, paths_in_board)

                # Not ocupated (update tail before)
                path_new = set.difference(path_new, set((element[0], element[1]) for element in snake[:-1]))
                
                # New snakes
                for new in path_new:
                    new_snake = snake.copy()
                    new_snake.pop()
                    new_snake.insert(0, new)
                    new_snakes.append(new_snake)  
                    
            snakes = new_snakes.copy()
        
        print(f"numberOfAvailableDifferentPaths({(self.n, self.m)}, {self.snake.args}, {self.depth.n}) = {len(snakes)}")
    
    class Inner_Snake:

        def __init__(self, *args, board):
            self.args = [*args]
            
            # 3 ≤ snake.length ≤ 7
            assert len(args) >= 3 and len(args) <= 7, "3 ≤ snake.length ≤ 7"

            # snake[i].length = 2
            for idx, coor in enumerate(args):
                # snake[i].length = 2
                assert len(coor) == 2, "snake[i].length = 2"

                # horizontally or vertically adjacent
                if idx < len(args) - 1:
                    assert abs(args[idx][0] - args[idx+1][0]) in [0,1], "Snake body must be horizontally adjacent" # H
                    assert abs(args[idx][1] - args[idx+1][1]) in [0,1], "Snake body must be vertically adjacent" # V
                    assert abs(args[idx][0] - args[idx+1][0] + args[idx][1] - args[idx+1][1]) == 1, "Snake body must be adjacent"
                
                # 0 ≤ snake[i][j] < board[j].
                assert (coor[0] < board[0] and 
                        coor[1] < board[1] and
                        coor[0] >= 0 and
                        coor[1] >= 0), "Snake have to stay inside the board, limit exceed"
                
    class Inner_Depth:
        
        def __init__(self, n):
            assert n == int(n), "n must be int"
            assert 0 <= n <= 20, "Path must be 0 <= n <= 20"
            
            self.n = n