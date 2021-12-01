###Day one:

##Sonar Sweep - Part Two

Most of this code is the same as the code for the first part. The only different parts are the loops.

In the second part, I've done it with two for loops:

I've created new list (array) `new_inputs = []`  which will contain the sums of three. 
Then I've created first for loop that creates sums of three. The following code can be portrayed as:

```python
new_inputs = []

for i in range(len(inputs) - 2):
    b = (inputs[i] + inputs[i + 1] + inputs[i + 2])
    new_inputs.append(b)
```

The second loop is the same as the first part of the task, but the list (array) is now the one that works with new list.
Here can be shown the second for loop with different list (array):

```python
for i in range(len(new_inputs)):
    if new_inputs[i] > new_inputs[i - 1]:
        c += 1
```
