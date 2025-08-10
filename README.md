# Mines Game Simulator
The Board class aims to accurately simulate a mines game board, and is based on that found at [SPRIBE](https://spribe.co/games/mines). See example.py for a quick demonstration of the features. 
# Requirements
`pip install -r requirements.txt`
# Parameters:
`def __init__(self, width  =  5, height  =  5, multiplier_rule  =  0.97)`

`width` and `height`: Dimensions of the board, typically 5x5
`multiplier_rule`: Constant that winnings are multiplied by as a house advantage. SPRIBE pays 97% of winnings that are calculated as follows:

$`P(n, m, k, t)= k \frac{\binom{t}{n}}{\binom{t-m}{n}}`$

Where n is the number of correct tile clicks, m is the number of mines on the board, k is the constant, and t is the total number of tiles `width * length`. This is multiplied by the bet amount and returned to the player.
# Betting
`def bet(self, mines_count: int, bet_amount: float, tiles: int, total_balance  =  0)`

Returns the total balance after a bet by simulating a round. If the round is lost, the balance minus the bet is returned, and if won, the bet is subtracted from the total balance and the winnings are added. 

`mines_count`: Amount of mines on the board. This is selected by the user for each bet and more mines lead to a better payout for a successful round. 
`bet_amount`: Amount of money bet
`tiles`: The number of simulated tile clicks, the pattern is randomized and irrelevant to the outcome
`total_balance`: Balance when starting the bet. Includes the bet itself, so if this is 3,000 and the bet is 100, a loss will return 2,900. 
