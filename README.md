# miniature-planet
This is my take on Game of Life.
gol.py is the class file, cool_iterator.py is a function file. In it, a very special function resides.

## What is game of life?
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

## Requiriments
gol.py doesn't have any dependancies. But cool_iterator.py depends on the [blessed](https://pypi.org/project/blessed/) module.

## How does it work?
Read the upper section of gol.py for further information about the implemention.

## How to use it?
Import ```gol```, create a ```GameOfLife``` instance, and then use the ```.tick()``` method.

Or you can just import ```blessed``` and ```cool_iterator``` modules, and use the ```cool_iterator()``` function, 
which is a better way to visualize it.

Lastly, put a 2-dimensional list in it. Again, read gol.py file for more information.
