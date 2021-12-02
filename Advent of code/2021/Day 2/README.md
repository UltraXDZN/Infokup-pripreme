### Day Two:

## Dive! - parts One and Two

I've approached this assignment by firstly creating an empty variables for `x` and `y` which represent default values for
`horizontal position` and `depth` variables.
```python
x, y = 0, 0 # Definition of x, y variables' default values
```
After that I've took an input outside of the loop to store the first value.
```python
a, b = map(str, input().split()) # First input of the expression
```
When the first value is stored, the program enters *infinite* loop. It runs until the user doesn't stop program by
entering empty input. In the loop, the program checks for every entered *expression* if it is `forward`, `up` or 
`down` and its adding values based on it.
```python
while True:
    x += [0, int(b)][a == "forward"] # Increment of "horizontal" variable
    y += [0, int(b) * [-1, 1][a == "down"]][a == "up" or a == "down"] # Increases or decreases depth based on "up" or "down"
    try:
        a, b = map(str, input().split()) # New input of the expression
    except ValueError: # If input is "" it gives an error which is handled and causes the program to break from the loop.
        break
```

At the end, program will just print the values of `x` and `y`.
```python
print(x * y) # Prints multiplication of "horizontal" and "depth" values
```

#### Second Part
The only differences between the first and second part are `aim` variable and how variables `y` and `aim` are calculated.
```python
x, y, aim = 0, 0, 0     # Definition of x, y and aim variables' default values
```
```python
    ...
    y += [0, int(b) * aim][a == "forward"] # Calculating Depth value based on formula x * aim 
    aim += [0, int(b) * [-1, 1][a == "down"]][a == "up" or a == "down"] # Increases or decreases aim based on "up" or "down"
    ...
```