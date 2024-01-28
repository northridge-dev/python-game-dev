# Hangman

Create your own two-player version of the classic word game Hangman.

```text


 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|

                                      +---+
                                      |   |
                                      O   |
                                     /|\  |
                                     / \  |
                                       =====

```

## Specifications

Your program should:

- Allow one player to enter a secret word for the other player to guess.
- Prompt the player to guess one letter at a time until the player has
  guessed the secret word or run out of guesses.
- After each guess, your program should display the state of the game:
  - the secret word with any correctly guessed letters filled in
  - a list of letters guessed so far
  - the number of guesses remaining
  - ASCII art appropriate to the number of missed guesses
- Display an appropriate message when the player wins or loses.
- When a game has ended, ask the players if they want to play again.
  If so, start a new game. If not, exit the program.

## Plan ahead

Before you write any code, outline the steps your program will take to play the game
or -- even better -- create a flowchart. You may find it helpful to convert this outline
or flowchart into pseudocode.

You'll need to submit this outline or flowchart before you start coding.

Consider the following:

- What state (data) does your program need to keep track of? What data types will you use?
- What steps get repeated? What control structures will you use to repeat them? How will
  your program know when to stop repeating?
- What are the decision points in your program -- steps when your program has choose between
  different actions it could take? How will it decide which code path to follow?

## Craftsmanship

For this project, let's focus on two good programming practices:

- **Descriptive variable names**. Use variable names that describe the data they hold.
  For example, `secret_word` is a better variable name than `word` and a much better
  variable name than `w`.
- **Comments**. Use precise comments to explain your code when it's helpful, but avoid
  comments where the code explains itself. Function-level comments are generally
  useful and a good place to start.

## Submitting your work

## Bonus challenges

Here are a few ideas for extending your program. Have a better idea? Go for it!

- Add a single-player mode. Your game will select a secret word for the player to guess. A player  
  should be unlikely to encounter the same secret word twice, even after playing many games.
- In two player-mode, keep score. After each game, display the number of games won by each player.
- In single-player mode, track a user's win-loss record and current win streak. Display win-loss and
  streak stats after each game.
- Add a difficulty setting. In harder settings, the program should choose longer or harder or less
  common words.
- Allow a user to choose a category from a list of categories. The program should select a word appropriate
  to the category.
