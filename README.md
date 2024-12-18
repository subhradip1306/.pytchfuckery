# Python Programs I made during my first semester of BS-MS
---

### A brief idea of what each program does:
1. **GOATED Func Approximator**
   * Graphs any function you want it to (R→R)
   * Will ask for the limits of the domain of the function
   * Will ask for *frequency*
      - Frequency is a term which is inversely proportional to smoothness and accuracy of the graphs
      - If the frequency is set to, let's say... 0.1, the program computes the function for x that occur at intervals of 0.1
   * Will then ask you to input a function, which you'll have to type out in python syntax with or without using the math module
2. **Kaprekar**
   * Outputs Kaprekar constants
   * <a href=https://kaprekar.sourceforge.net/output/sample.php> Know more about kaprekar contants </a>
3. **Goated Prime checker**
   * Outputs prime numbers between 1 and n where n is a number we input
4. **Golden Spiral**
   * Traces out the golden spiral till the distance and upto the accuracy that we input
5. **one-one checker**
   * For any function we input (with domain Z), checks whether the function is one-one or not
   * Has it's limitations of course, since it can't actually compute for the infinite number of elements in Z
     - What it does instead is stop right when there are two identical f(x)'s for two different x's within the domain when computing the range
     - So all it can really tell you is if the function is many-one *yet*
6. **Take me to Kaprekar**
   * Any 4 digit number with at least two distinct digits (leading 0's allowed), when put through <a href=https://en.m.wikipedia.org/wiki/Kaprekar%27s_routine> the kaprekar routine </a>, will eventually give you 6174
   * This program computes the highest number of iterations needed until the answer becomes 6174
7. **Power**
   * Outputs the power set of any set we input.
8. **SORT Balls**
   * Sorts any random string 0s and 1s with all 0s on one end and all 1s on the other end
   * Outputs the minimum number of swaps to do so
9. **FLIP**
   * A CLI game where we're given a 3x3 grid of 0's and 1's, with the goal of flipping all the elements to 1
   * You can choose any element of your choice to flip however there's a catch...
   * <a href=https://www.jaapsch.net/puzzles/lomath.htm> Some math related to this game and more </a>
