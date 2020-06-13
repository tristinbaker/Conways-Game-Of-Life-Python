# Conway's Game Of Life in Python
Implementation of Conway's Game of Life in Python

I started out writing this implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in order to further my knowledge of how Python works, but I mainly just wanted to write Conway's Game of Life again. I wrote it once in C++ during college, but I forgot most of that development, so this was me having another try at it without any assistance from my professor.

This uses [pygame](https://www.pygame.org/news) for the graphics, mainly [pygame.Rect](https://www.pygame.org/docs/ref/rect.html). The grid is made up of a 2D array of pygame.Rect. A "live" cell will be displayed by being drawn filled in, where a "dead" cell is drawn just as the border. 

The initial grid is set up by external files with a specific 2D array pre-built. These files have specific grids drawn to make the Game of Life behave in a specific way, such as the [Glider](https://www.conwaylife.com/wiki/Glider).

## Future Plans
I would like to implement buttons to switch between Game of Life behaviors. In addition, I would like to implement a feature in which clicking on the grid will generate a glider where the user clicked. These two features will give the user a more interactive experience, as right now it is not user-friendly.
