"""
Class to represent a zendo structure. Specifications can be found here:
https://www.looneylabs.com/sites/default/files/literature/Zendo%20Rules%20Book%201.pdf
"""

class Structure:
    """
    Pieces: 27 pyramids, 27 wedges, 27 blocks (9 per color). Possible colors are: red, blue, yellow.
    """

    def __init__(
        self,
        num_red_pyramids: int = 0,
        num_red_wedges: int = 0,
        num_red_blocks: int = 0,
        num_blue_pyramids: int = 0,
        num_blue_wedges: int = 0,
        num_blue_blocks: int = 0,
        num_yellow_pyramids: int = 0,
        num_yellow_wedges: int = 0,
        num_yellow_blocks: int = 0,
    ) -> None:

        self._num_red_pyramids = num_red_pyramids
        self._num_red_wedges = num_red_wedges
        self._num_red_blocks = num_red_blocks

        self._num_blue_pyramids = num_blue_pyramids
        self._num_blue_wedges = num_blue_wedges
        self._num_blue_blocks = num_blue_blocks

        self._num_yellow_pyramids = num_yellow_pyramids
        self._num_yellow_wedges = num_yellow_wedges
        self._num_yellow_blocks = num_yellow_blocks

        self._num_red = self._num_red_pyramids + self._num_red_wedges + self._num_red_blocks
        self._num_blue = self._num_blue_pyramids + self._num_blue_wedges + self._num_blue_blocks
        self._num_yellow = self._num_yellow_pyramids + self._num_yellow_wedges + self._num_yellow_blocks

        self._num_pyramids = self._num_red_pyramids + self._num_blue_pyramids + self._num_yellow_pyramids
        self._num_wedges = self._num_red_wedges + self._num_blue_wedges + self._num_yellow_wedges
        self._num_blocks = self._num_red_blocks + self._num_blue_blocks + self._num_yellow_blocks
    
    @property
    def num_red_pyramids(self):
        return self._num_red_pyramids

    @property
    def num_red_wedges(self):
        return self._num_red_wedges

    @property
    def num_red_blocks(self):
        return self._num_red_blocks

    @property
    def num_blue_pyramids(self):
        return self._num_blue_pyramids

    @property
    def num_blue_wedges(self):
        return self._num_blue_wedges

    @property
    def num_blue_blocks(self):
        return self._num_blue_blocks

    @property
    def num_yellow_pyramids(self):
        return self._num_yellow_pyramids

    @property
    def num_yellow_wedges(self):
        return self._num_yellow_wedges

    @property
    def num_yellow_blocks(self):
        return self._num_yellow_blocks

    @property
    def num_red(self):
        return self._num_red

    @property
    def num_blue(self):
        return self._num_blue

    @property
    def num_yellow(self):
        return self._num_yellow

    @property
    def num_pyramids(self):
        return self._num_pyramids

    @property
    def num_wedges(self):
        return self._num_wedges

    @property
    def num_blocks(self):
        return self._num_blocks
