# Libraries

# Libraries are collections of functions (pre-built code) that do a job for you
# We can import these libraries to make our own code easier to understand, less complex and faster to write.

from random import randint # can import code within the library. instead of import random as rand, then rand.randint()

print(randint(1, 100))

import math

num_float = 23.22
print(math.ceil(num_float)) # rounds up to next integer
print(math.floor(num_float)) # rounds down
print(math.pi)

