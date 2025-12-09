# Game of Life - Functional Approach

Imperative and purely functional implementations of Conway's Game of Life.

## Overview

The imperative code was written freestyle after a quick read of the game's rules and a little bit of research.
The functional approach is directly inspired by [this article](https://www.strangeleaflet.com/conways-game-of-life-a-functional-approach/) which is very well documented.

### Simple gist of the game

1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors survives to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## The imperative approach

Written in the file `Imperative GOL.py`.  Just open the script with python to start it. `python "Imperative GOL.py"`
- Grid where you can click to toggle cells
- Step by step simulation with customizable tick rate
- Count of local neighbors displayed on each cell
- Pause/resume with spacebar

## The purely functional approach

Inside the folder `Functional Approach` you will find `GOL.py` which, _in only two pure functions_, encapsulates all the implementation needed to simulate the game!
`examples.py` includes examples of common GOL patterns and samples of code that you can run on the fly to verify the correctness of the program.
This implementation has multiple optimizations over the prior one including:
- Only storing "alive" cells
- Using a set of tuples instead of a 2D array
