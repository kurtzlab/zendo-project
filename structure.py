"""
Class to represent a zendo structure. Specifications can be found here:
https://www.looneylabs.com/sites/default/files/literature/Zendo%20Rules%20Book%201.pdf
"""

class Structure:
    """
    Zendo structure representation
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
        """
        Shapes: pyramids, wedges, blocks. Possible colors are: red, blue, yellow.
        """

        self.num_red_pyramids = num_red_pyramids
        self.num_red_wedges = num_red_wedges
        self.num_red_blocks = num_red_blocks

        self.num_blue_pyramids = num_blue_pyramids
        self.num_blue_wedges = num_blue_wedges
        self.num_blue_blocks = num_blue_blocks

        self.num_yellow_pyramids = num_yellow_pyramids
        self.num_yellow_wedges = num_yellow_wedges
        self.num_yellow_blocks = num_yellow_blocks

        self.num_red = self.num_red_pyramids + self.num_red_wedges + self.num_red_blocks
        self.num_blue = self.num_blue_pyramids + self.num_blue_wedges + self.num_blue_blocks
        self.num_yellow = self.num_yellow_pyramids + self.num_yellow_wedges + self.num_yellow_blocks

        self.num_pyramids = self.num_red_pyramids + self.num_blue_pyramids + self.num_yellow_pyramids
        self.num_wedges = self.num_red_wedges + self.num_blue_wedges + self.num_yellow_wedges
        self.num_blocks = self.num_red_blocks + self.num_blue_blocks + self.num_yellow_blocks

    def __EQ__(self, other) -> bool:
        return self.num_red_pyramids == other.num_red_pyramids and \
            self.num_red_wedges == other.num_red_wedges and \
            self.num_red_blocks == other.num_red_blocks and \
            self.num_blue_pyramids == other.num_blue_pyramids and \
            self.num_blue_wedges == other.num_blue_wedges and \
            self.num_blue_blocks == other.num_blue_blocks and \
            self.num_yellow_pyramids == other.num_yellow_pyramids and \
            self.num_yellow_wedges == other.num_yellow_wedges and \
            self.num_yellow_blocks == other.num_yellow_blocks

    def __str__(self):
        return f"""
        num_red_pyramids: {self.num_red_pyramids}
        num_red_wedges: {self.num_red_wedges}
        num_red_blocks: {self.num_red_blocks}
        num_blue_pyramids: {self.num_blue_pyramids}
        num_blue_wedges: {self.num_blue_wedges}
        num_blue_blocks: {self.num_blue_blocks}
        num_yellow_pyramids: {self.num_yellow_pyramids}
        num_yellow_wedges: {self.num_yellow_wedges}
        num_yellow_blocks: {self.num_yellow_blocks}
        """
