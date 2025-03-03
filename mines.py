from random import randint

class Board:
    def __init__(self, width: int, height: int, multiplier = 1.19):
        self.width = width
        self.height = height
        self.multiplier = multiplier
        
        self.tiles = width * height

    def random_tile(self):
        tile = (randint(1, self.height), randint(1, self.width))
        return tile
    
    def random_unique_tile(self, compare: list):
        tile = self.random_tile()
        while tile in compare:
            tile = self.random_tile()
        return tile

    def bet(self, mines_count: int, bet_amount: float, tiles: int):
        mine_positions = []
        revealed_tiles = []

        for i in range(mines_count):
            mine_positions.append(self.random_unique_tile(mine_positions))

        for i in range(tiles):
            tile_pick = self.random_unique_tile(revealed_tiles)
            
            if tile_pick in mine_positions:
                return 0
            
            revealed_tiles.append(tile_pick)

        payout = bet_amount + self.multiplier ** tiles

        return payout