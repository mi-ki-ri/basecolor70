from math import floor
import numpy as np
from PIL import Image


HEIGHT = 240
WIDTH = 320

BASE_COLOR = [233, 185, 64]
ASSERT_COLOR = [69, 114, 46]
ACCENT_COLOR = [100, 164, 60]

stacks = []

stacks.append(np.full((HEIGHT, floor(WIDTH*75/100), 3), BASE_COLOR))
stacks.append(np.full((HEIGHT, floor(WIDTH*25/100), 3), ASSERT_COLOR))
stacks.append(np.full((HEIGHT, floor(WIDTH*5/100), 3), ACCENT_COLOR))

stack = np.hstack(stacks)

fromarr = Image.fromarray(stack.astype(np.uint8)).save("./dist_flow3.png")
