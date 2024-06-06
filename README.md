# Mini-game

This repository contains a simple random number game where the user competes against the computer. The game is implemented in Python, and the rules are straightforward: if the user's input matches the computer's randomly chosen value, the user wins. Otherwise, the user loses.

## Table of Contents

- [Introduction](#introduction)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Usage](#usage)



## Introduction

This game is a basic implementation that demonstrates the use of random number generation and conditional statements in Python. The goal of the game is to match the user's input with a randomly generated value by the computer.

## How to Play

1. The computer randomly selects a number between 0 and 5.
2. The user is prompted to enter a number between 0 and 5.
3. If the user's input matches the computer's randomly selected number, the user wins.
4. If the numbers do not match, the user loses.

## Installation

1. Clone this repository to your local machine:

    ```sh
    git clone https://github.com/your-username/simple-random-number-game.git
    ```

2. Navigate to the project directory:

    ```sh
    cd simple-random-number-game
    ```

3. Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).

## Usage

To play the game, create a file named `game.py` with the following content:

```python
import random as r 

n = r.randint(0, 5)
if n == 0:
    n = 's'
elif n == 1:
    n = 'p'
elif n == 2:
    n = 'c'

user_input = input("Enter input (s, p, c): ")
if user_input == n:
    print("tie")
elif (user_input == 's' and n == 'p') or (user_input == 'p' and n == 'c') or (user_input == 'c' and n == 's'):
    print("you win")
else:
    print("you fail")

just for fun.
