# Tic-Tac-Toe

Create a program that allows a player to play a game of
Tic-Tac-Toe against an artificial intelligence.

## An artificial intelligence (!?!)

Yep! You'll be writing code that can make reasonable decisions
when playing an adversarial game. It won't be _very_ intelligent
and it won't be very flexible -- it won't be able to play anything
but Tic-Tac-Toe -- but it will play better than someone randomly
picking moves and, if you're not careful, it might even beat you!

How?

You'll give it some reasonably good rules to follow. For example:

- If the computer can win with a move, it should do it.
- If you can win on your next turn, the computer should try to block you.
- If it cannot win or block, it should try to take a high-value square.

Maybe you can think of other rule-based strategies you can "teach" it.

## Setup

Before you can worry about the AI, you need to create the game itself.

You'll need to write code to:

- store the state of the game
- display the game board
- allow a player to choose a square to claim
  - handle invalid choices: a square that's
    already taken or a square that doesn't exist
- check if the game is over (win or draw), display
  the result, and end the game

You might even want to start by writing code that allows a player to play
another against himself or another human player.
