from random import randint
from scipy.special import binom

class Board:
    def __init__(self, width = 5, height = 5, multiplier_rule = 0.97):
        self.width = width
        self.height = height

        self.multiplier = multiplier_rule
        
        self.tiles = width * height

    def random_tile(self) -> tuple:
        tile = (randint(1, self.height), randint(1, self.width))
        return tile
    
    def random_unique_tile(self, compare: list) -> tuple:
        tile = self.random_tile()
        while tile in compare:
            tile = self.random_tile()
        return tile
    
    def calculate_payout(self, n: int, m: int) -> float:
        k = self.multiplier
        tiles_choose_picks = binom(self.tiles, n)
        safe_choose_picks = binom(self.tiles - m, n)

        pay = k * (tiles_choose_picks / safe_choose_picks)

        return pay


    def bet(self, mines_count: int, bet_amount: float, tiles: int, total_balance = 0) -> float:
        mine_positions = []
        revealed_tiles = []

        for i in range(mines_count):
            mine_positions.append(self.random_unique_tile(mine_positions))

        for i in range(tiles):
            tile_pick = self.random_unique_tile(revealed_tiles)
            
            if tile_pick in mine_positions:
                return total_balance - bet_amount
            
            revealed_tiles.append(tile_pick)

        return total_balance + self.calculate_payout(tiles, mines_count) * bet_amount - bet_amount