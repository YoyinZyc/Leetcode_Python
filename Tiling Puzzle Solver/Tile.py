class Tile(object):
    def __init__(self, tile, area, isBoard = False):
        self.tile = tile
        self.area = area
        self.d = dict()
        self.d_r = dict()
        # self.dup = dup
        if not isBoard:
            self.fh_tile = self.file_horizontal_tile()
            self.r_tile = self.rotate_tile(self.tile)
            self.fhr_tile = self.fhr_tile()
        else:
            self.create_board_map()

    def file_horizontal_tile(self):
        fh_tile_set = set()
        fh_tile_set.add(self.tile)
        fh_tile_set.add(self.flip_horizontal(self.tile))
        return tuple(fh_tile_set)

    def rotate_tile(self, tile):
        rotate_tile_set = set()
        rotate_tile_set.add(tile)
        rotate_tile_set.add(self.rotate_90(tile))
        rotate_tile_set.add(self.rotate_180(tile))
        rotate_tile_set.add(self.rotate_270(tile))
        return tuple(rotate_tile_set)
    def fhr_tile(self):
        fhr_tile_set = set()
        for v in self.fh_tile:
            l = self.rotate_tile(v)
            for t in l:
                fhr_tile_set.add(t)
        return tuple(fhr_tile_set)
    def flip_horizontal(self,tile):
        fh_tile = []
        for v in tile:
            fh_tile.insert(0,v)
        return tuple(fh_tile)
    def flip_vertical(self, tile):
        fv_tile = []
        tile_v = tuple(zip(*tile))

        for v in tile_v:
            fv_tile.insert(0,v)
        return tuple(zip(*fv_tile))

    def rotate_90(self, tile):
        return tuple(zip(*self.flip_horizontal(tile)))
    def rotate_180(self, tile):
        return self.flip_horizontal(self.flip_vertical(tile))
    def rotate_270(self,tile):
        return tuple(zip(*self.flip_vertical(tile)))
    def create_board_map(self):
        count = 0
        for i in range(len(self.tile)):
            for j in range(len(self.tile[0])):
                if self.tile[i][j] != ' ':
                    self.d[(i,j)] = count
                    self.d_r[count] = (i,j)
                    count+=1


