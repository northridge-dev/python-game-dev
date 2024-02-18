# Tic-Tac-Toe

Create a program that allows a player to play a game of
Tic-Tac-Toe against an artificial intelligence.

## An artificial intelligence (!?!)

Yep! You'll be writing code that can make reasonable decisions
when playing an adversarial game. It won't be _very_ intelligent,
but it will play better than someone randomly picking moves and,
if you're not careful, it might even defeat you!

How?

You'll give it some reasonably good rules to follow. For example:

- If a winning move is available, the AI should choose it.
- If you can win on your next turn, the AI should try to block you.
- If the AI cannot win or block, it should try to take a high-value square.

Maybe you can think of other rule-based strategies to make your AI a stronger
tic-tac-toe player.

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

## Picking a good data structure

Implementing a rule-based AI depends on choosing a good data structure, a way of
representing the game board that makes it (relatively) easy to to assess the
state of the game and make decisions about what move to make.

For example, you _could_ represent the game board as a flat list with 9
elements where each element corresponds to a square on the board. It might look
something like this:

```python
board = ['X', 'O', 'X', 'O', 'X', 'O', ' ', ' ', 'X']
```

You could fairly easily use such a representation to "print" the game board:

```python
X | O | X
---------
O | X | O
---------
  |   | X
```

It's easy for a human to look at the board and determine that 'X' has won. But
how would you write code that could take as input that list and determine that
'X' has won? Would a different data structure make such a calculation easier?

Or here's another example. You or I could look at this board and conclude that,
if 'X' doesn't take the bottom-left square, 'O' will have a chance to win on the
next move:

```python
O | X | X
---------
O |   | X
---------
  |   | O
```

But it's not easy to get your AI to "see" the same thing. Whatever solution you
find, it will need to be flexible enough to handle, for example, a mirrored
board:

````python

X | X | O
---------
X |   | O
---------
O |   |


or a rotated board:

```python
O | O |
---------
X |   |
---------
X | X | O
````

Likewise, the logic that finds this vulnerability if the AI plays 'X' should
work equally well if the AI plays 'O'.
