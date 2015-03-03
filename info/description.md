We will emulate the stack process with Python. You are given a sequence of commands:

- "PUSH X" -- add **X** in the stack, where **X** is a digit.
- "POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero) and does nothing.
- "PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero).
The stack can only contain digits.

You should process all commands and sum all digits which were taken from the stack ("PEEK" or "POP").
Initial value of the sum is 0 (zero).

Let's look at an example, here’s the sequence of commands:<br>

    ["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

| Command | Stack | Sum 
|---------|-------|-----
| PUSH 3  | 3     | 0
| POP     |       | 0+3
| POP     |       | 3+0
| PUSH 4  | 4     | 3
| PEEK    | 4     | 3+4
| PUSH 9  | 4,9   | 7
| PUSH 0  | 4,9,0 | 7
| PEEK    | 4,9,0 | 7+0
| POP     | 4,9   | 7+0
| PUSH 1  | 4,9,1 | 7
| PEEK    | 4,9,1 | 7+1=**8**

In this mission the main goal to make your code as short as possible.
The shorter your code, the more points you earn.
Your score for this mission is dynamic and directly related to the length of your code.
For reference, scoring is based on the number of characters used.
