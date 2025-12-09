# This implementation is very elegant and concise.
# Inspried by https://www.strangeleaflet.com/conways-game-of-life-a-functional-approach/
# A very good read. I recommend reading his explanation of the code, originally written in clojure.

def counter(iter, accum={}, index=0):
    if index == len(iter):
        return accum

    if iter[index] not in accum: accum[iter[index]] = 0
    
    accum[iter[index]] += 1
    return counter(iter, accum, index+1)

def neighbors(x, y):
    return [
        (x + dx, y + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == 0 and dy == 0)
    ]

def step(cells):
    counts = counter([
        cell
        for (x, y) in cells
        for cell in neighbors(x, y)
    ])

    return {
        (x,y)
        for ((x, y),n) in counts.items()
        if n == 3 or (n == 2 and (x,y) in cells)
    }