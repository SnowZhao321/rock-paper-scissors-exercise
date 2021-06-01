# rock-paper-scissors-exercise
This repo contains a basic command-line game of rock-paper-scissors.

## Installation
Clone or download this repo onto your local computer.
Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):
```sh
cd rock-paper-scissors-exercise 
```

## Setup
First, please install python version 3.8 in a conda environment. And create and activate a new project-specific Anaconda virtual environment:
  ```
  conda create -n my-game-env python=3.8 # (first time only)
  
  conda activate my-game-env
  ```
Second, chenck the python version and module 
  ```
  python --version
  
  pip list 
  ```
Third, Install the required packages:
```sh
pip install -r requirements.txt
```

## Configuring Environment Variables

Add a new ".env" file to the root directory of this repo, and place contents like the following inside:
```
PLAYER_NAME="player 1"
```

## Usage
From within the virtual environment, run the Python script from the command-line:
  ```sh
  python game.py 
  ```
