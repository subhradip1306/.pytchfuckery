# Python Programs I made during my first semester at IISER-K
---

### A brief idea of what each program does:
1. **GOATED Func Approximator**
   - Graphs any function you want it to (R→R)
   - Will ask for the limits of the domain of the function
   - Will ask for *frequency*
      * Frequency is a term which is inversely proportional to smoothness and accuracy of the graphs
      * If the frequency is set to, let's say... 0.1, the program computes the function for x that occur at intervals of 0.1
   - Will then ask you to input a function, which you'll have to type out in python syntax with or without using the math module
2. **Kaprekar**
   - Outputs Kaprekar constants
   - <a href=https://kaprekar.sourceforge.net/output/sample.php> Know more about kaprekar contants </a>
3. **Goated Prime checker**
   - Outputs prime numbers between 1 and n where n is a number we input
4. **Golden Spiral**
   - Traces out the golden spiral till the distance and upto the accuracy that we input
5. **one-one checker**
   - For any function we input (with domain Z), checks whether the function is one-one or not
   - Has it's limitations of course, since it can't actually compute for the infinite number of elements in Z
     * What it does instead is stop right when there are two identical f(x)'s for two different x's within the domain when computing the range
     * So all it can really tell you is if the function is many-one *yet*
6. **Take me to Kaprekar**
   - Any 4 digit number with at least two distinct digits (leading 0's allowed), when put through <a href=https://en.m.wikipedia.org/wiki/Kaprekar%27s_routine> the kaprekar routine </a>
   - This program computes the highest number of iterations needed until the answer becomes 6174

