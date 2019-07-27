# Snowman Defender
Save the snowpeople from the robot hoards by collecting each one without touching the robots. Use your WASD keys to collect the snowpeople, but watch out for the robots! This game is timed and tracks your score. Good luck!

## Demo
![Demo](snowman_pygame/snowman_game_demo.gif)

## Features
* Accumulate points by collecting randomly generated snowman sprites.
* Avoid randomly generated robot sprites that reduce the displayed score. 
* A "Game Over: Click to Play Again" screen that is triggered by 4 conditions.
* A countdown timer set to 60 seconds.
* Win condition: A score of 20 before the timer runs out.
* Lose Conditions: A score of -5 or 30 sprite collisions before reaching 20 points or the timer reaches 0.

## Built Using
* Python for the game engine
* Pygame for graphics rendering

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing, or entertainment purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install the following software/modules: 

``pip``

``Pygame``

``Python 2 or Python 3``

``snowman_pygame``

### Installing

Make sure you have `pip` installed on your local machine. [Python 3](https://www.python.org/downloads/) ships with pip, check if you have pip installed using ``python -m pip --version`` on the CLI. Otherwise, to install pip, see the [documentation](https://pip.pypa.io/en/stable/installing/). 
 
 ```
 python -m pip install -e https://github.com/ZATGit/Snowman-Defender-Pygame
 ```
 
 or
 
 ```
cd path/to/chosen/folder
git clone https://github.com/ZATGit/Snowman-Defender-Pygame
```
Alternatively, you can download a `.exe` [file](https://github.com/ZATGit/Snowman-Defender-Pygame/blob/master/snowman_pygame/dist/snowman_brick_collector/snowman_brick_collector.exe)

Don't forget to activate your virtual environment if you use one!

### Deployment

```
cd path/to/chosen/folder/snowman_pygame/snowman_pygame
python snowman_brick_collector
```

### License

This project is licensed under the MIT License - see the ``LICENSE.md`` file for details.

### Author

Zach Trembly



    
    
  
  
  
  
