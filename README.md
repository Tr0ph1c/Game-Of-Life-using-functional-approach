# Game of Life - Functional Approach

A Python implementation of Conway's Game of Life using a functional programming approach with pygame for visualization.

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It's a zero-player game that evolves based on its initial state, requiring no further input. The game consists of a grid of cells which, based on a few mathematical rules, can live, die, or multiply.

### Rules

1. Any live cell with fewer than two live neighbors dies (underpopulation)
2. Any live cell with two or three live neighbors survives to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

## Features

- Interactive grid where you can click to toggle cells
- Real-time simulation with customizable tick rate
- Visual display of neighbor counts for each cell
- Pause/resume functionality with spacebar
- Clean, minimal interface

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ahmniab/Game-Of-Life-using-functional-approach.git
cd Game-Of-Life-using-functional-approach
```


### 2. Install Dependencies

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Game

```bash
python "Imperative GOL.py"
```

### Controls

- **Mouse Click**: Toggle cell state (alive/dead)
- **Spacebar**: Start/pause simulation
- **Close Window**: Exit the game

### Customization

You can modify the following constants in the code to customize your experience:

```python
SIZE = 50        # Size of each cell in pixels
X_SIZE = 15      # Number of cells horizontally
Y_SIZE = 15      # Number of cells vertically
TICKRATE = .5    # Time between generations (in seconds)
```

### Colors

The color scheme can be customized by modifying these constants:

```python
COLOR_BG = (10, 10, 10)        # Background color
COLOR_ALIVE = (250, 250, 250)  # Living cells
COLOR_DEAD = (30, 30, 30)      # Dead cells
COLOR_GRID = (30, 30, 30)      # Grid lines
```

## How to Play

1. **Setup**: Click on cells to create your initial pattern
2. **Start**: Press spacebar to begin the simulation
3. **Observe**: Watch how your pattern evolves according to Conway's rules
4. **Pause**: Press spacebar again to pause and modify the pattern
5. **Experiment**: Try different initial configurations to see various behaviors

### Interesting Patterns to Try

- **Glider**: A pattern that moves across the grid
- **Blinker**: A simple oscillator that toggles between two states
- **Block**: A static pattern that doesn't change
- **Beacon**: A period-2 oscillator

## Project Structure

```
Game-Of-Life-using-functional-approach/
│
├── README.md              # This file
└── Imperative GOL.py      # Main game implementation
```

## Technical Details

- **Language**: Python 3
- **Graphics**: pygame library for rendering and event handling
- **Math**: numpy for efficient array operations
- **Architecture**: Functional approach with separation of concerns

## Dependencies

- **pygame**: For graphics, window management, and event handling
- **numpy**: For efficient array operations and neighbor calculations

## Troubleshooting

### Common Issues

1. **pygame not found**: Make sure pygame is installed with `pip install pygame`
2. **numpy not found**: Make sure numpy is installed with `pip install numpy`
3. **Python version**: Ensure you're using Python 3.6 or higher
4. **Virtual environment**: If dependencies aren't found, make sure your virtual environment is activated

### Performance

If the game runs slowly, try:

- Reducing the grid size (X_SIZE, Y_SIZE)
- Increasing the TICKRATE value
- Reducing the cell SIZE

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## Acknowledgments

- John Conway for creating the Game of Life
- The pygame community for the excellent graphics library
- NumPy developers for efficient array operations
