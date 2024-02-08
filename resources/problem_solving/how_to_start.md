# How to Get Started When You're Not Sure What You're Doing

The challenges, problem sets, and projects in this course are meant to be difficult.
We grow and learn by stretching.

Stretching is often uncomfortable. When you're swimming out of your depth, it's only
natural to panic. Don't panic.

Instead, try this:

## Decompose the problem

A difficult problem is _complex_: it may look like one giant, hairy problem, but it's
probably a bunch of smaller problems all tangled together. If you can tease them apart,
each of those smaller problems will be more manageable. If any are still too complex,
see if you can break them apart, too.

Some problems will be easier to decompose than others. If you're having trouble, here
are some questions that might help:

1. **What are the inputs?** Put another way: what information do you need to get started?
   For example, if you're writing a program to calculate the area of a rectangle, you'll
   need its length and width as inputs. If you're creating a game like Pong, the inputs
   might be the user's keystrokes.

2. **What would an answer (the output of your program) look like?** Sometimes it's easy to
   describe. If you're writing a program to calculate the area of a rectangle, the output
   will be a number. But what if you're building a game like Pong? The "output" will a
   dynamic display and set of user controls that follow the game's rules.

3. **What are the steps -- calculations, transformations, etc. -- needed to turn those
   inputs into that output?** Turning the length and width into an area is pretty
   straightforward. For Pong, it would probably help to think about game elements
   separately -- the ball, the paddles, the score, etc. -- and then about how they
   interact.

4. **What record keeping is necessary?** What information do you need to track? Calculating
   the area of a rectangle is simple enough that you probably don't need to do any
   record keeping. That's not typical. Often it's necessary to store the results of one
   step to reuse in the next or a later step. Or in the case of Pong, you'd need to keep
   track of the score, the position and trajectory of the ball, and the position of each
   paddle.

Still stuck? Try working through a concrete example. Get out a piece of paper and write
it out. Pay attention

## Simplify the problem and find a strategy

Chances are not every version of the problem is equally difficult. Why not start with the
simplest version you can think of. The harder versions can wait.

Suppose, for example, that you're trying to find the number of days between two dates. Start
by solving the problem when the two dates are in the same month.

It helps to start with a concrete example or two. As you work through those concrete examples,
look for patterns that you can generalize into a strategy that will work for similar cases.

## Write pseudocode

## Implement your strategy in code

Now that you have a plan, you can start writing the code. Think about the tools you have in
your Python toolbox and how you can use them to implement your plan.

Can't find the tool you need? There's a good chance that your pseudocode can help you formulate a
precise question. The more precise your question, the more likely a classmate, a Google search, or
Bard / ChatGPT will yield a helpful answer.

## Test your code

You don't have to wait until your function can handle all possible inputs and edge cases before
giving it a whirl. Testing your code now will help you validate your strategy and catch any errors
in your code.

One of two things will happen:

1. You'll get an error message. Don't be discouraged. Take time to read and try to understand the error
   message. It's the Python interpreter's way of helping you. Look at the error type and the line number
   to try to figure out what went wrong and where. Maybe you have a typo or your syntax is a little off.
   If you don't know how to fix it, now's the time to look at past examples, look up some documentation,
   or ask!
2. You'll be prompted to enter a day, month, and year. Pick values that help you test a case you think
   your code should be able to handle. Did you get the result you expected? If so, _awesome_! But you're
   not done. Try a few more cases to be more confident that your code is working the way you expect. What
   if you didn't get the result you expected? Try stepping through your code line-by-line, looking for
   where your logic is flawed. Fix it, rinse, and repeat.

## Extend your strategy and deal with complications

Next, see if you can extend your strategy to deal with more complicated versions of the problem.
Apply what you learned from the simpler version to harder versions.

For example, if you can find the number of days between two dates when they're in the same month,
try to find the number of days between two dates when they're in adjacent months.

### Handle corner cases: days after Christmas

Once you have a function that handles the common cases, it's time to rework or extend your logic to handle "corner cases".
