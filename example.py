from mines import Board

main = Board() # Create board with default settings

balance = 3_000 # Initial balance
bet_amount = 100
tiles = 12 # Number of tiles the "user" clicks
mines = 1 # Number of mines on the board

print(f"Balance before bet: {balance}")
balance = main.bet(mines, bet_amount, tiles, balance)
print(f"Balance after bet: {balance}")


if False: # Change to True for advanced board demonstration
    print()

    advanced_board = Board(6, 4, 1.01) # Creates a 6x4 board that adds 1% to winnings

    balance = 3_000

    print(f"Balance before bet: {balance}")
    balance = advanced_board.bet(mines, bet_amount, tiles, balance)
    print(f"Balance after bet: {balance}")