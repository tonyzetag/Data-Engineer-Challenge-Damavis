from game.board import Board

# Se ha usado estilo CamelCase para ser fiel al documento, pero PEP8 recomienda "lowercase, with words separated by underscores"
def numberOfAvailableDifferentPaths(board, snake, depth):
    """ Inputs
    - board = list(int, int)
    - snake = list(list(int, int))
    - depth = int
    Considerations
    - board have to be board.length = 2, 1 <= board[i] <= 10
    - snake have to be 3 <= snake.length <= 7, snake[i].length = 2, 0 <= snake[i][j] < board[j]
    - depth have to be 1 <= n <= 20.
    """
    game = Board(*board)
    game.Snake(*snake)
    game.Depth(depth)
    return game.start()

def main():
    print("Test 1 - ".center(50, '-'))
    numberOfAvailableDifferentPaths(
        board = [4, 3],
        snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]],
        depth = 3
    )

    print("Test 2 - ".center(50, '-'))
    numberOfAvailableDifferentPaths(
        board = [2, 3],
        snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]],
        depth = 10
    )

    print("Test 3 - ".center(50, '-'))
    numberOfAvailableDifferentPaths(
        board = [10, 10],
        snake = [[5, 5], [5, 4], [4, 4], [4, 5]],
        depth = 4
    )

main()
