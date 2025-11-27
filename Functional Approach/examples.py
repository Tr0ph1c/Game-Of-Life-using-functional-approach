# I wrote this file in a way so that you can scroll along while reading
# and conveniently select the block of code associated with the
# specific example you want to try and run it to see the result.

# ===================================================================

# The Blinker
# The most common 2 period oscillator
# https://conwaylife.appspot.com/pattern/blinker

#  0 1 0         0 0 0
#  0 1 0  ---->  1 1 1
#  0 1 0         0 0 0

# initial pattern
# {(1,0), (1,1), (1,2)}

# expected output
# {(0,1), (1,1), (2,1)}

import GOL

print(GOL.step({(1,0), (1,1), (1,2)}))

# ===================================================================

# The Block
# Most common still structure
# https://conwaylife.appspot.com/pattern/block

#  0 0 0 0         0 0 0 0
#  0 1 1 0  ---->  0 1 1 0
#  0 1 1 0         0 1 1 0
#  0 0 0 0         0 0 0 0

# initial pattern
# {(1,1), (2,1), (1,2), (2,2)}

# expected output
# {(1,1), (2,1), (1,2), (2,2)}

import GOL

print(GOL.step({(1,1), (2,1), (1,2), (2,2)}))

# ===================================================================

# The Glider
# Most common "spaceship"
# https://conwaylife.appspot.com/pattern/glider

#  0 1 0 0         0 0 0 0
#  0 0 1 0  ---->  1 0 1 0
#  1 1 1 0         0 1 1 0
#  0 0 0 0         0 1 0 0

# initial pattern
# {(1,0), (2,1), (0,2), (1,2), (2,2)}

# expected output
# {(0,1), (1,2), (2,1), (2,2), (1,3)}

import GOL

print(GOL.step({(1,0), (2,1), (0,2), (1,2), (2,2)}))