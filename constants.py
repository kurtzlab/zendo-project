# colors
RED = "RED"
BLUE = "BLUE"
YELLOW = "YELLOW"

# quantities
EXACTLY = "EXACTLY"
AT_LEAST = "AT_LEAST"
MAX_QTY = 9

# shapes
PYRAMIDS = "PYRAMIDS"
WEDGES = "WEDGES"
BLOCKS = "BLOCKS"

PRIORITY_QUEUE_OF_ALL_POSSIBLE_RULES = [
    f"{qty} {i} {color}" for qty in [EXACTLY, AT_LEAST] for i in range(MAX_QTY + 1) for color in [RED, BLUE, YELLOW]
] + [
    f"{qty} {i} {shape}" for qty in [EXACTLY, AT_LEAST] for i in range(MAX_QTY + 1) for shape in [PYRAMIDS, WEDGES, BLOCKS]
] + [
    f"{qty} {i} {color} {shape}" for qty in [EXACTLY, AT_LEAST] for i in range(MAX_QTY + 1) for color in [RED, BLUE, YELLOW] for shape in [PYRAMIDS, WEDGES, BLOCKS]
]
