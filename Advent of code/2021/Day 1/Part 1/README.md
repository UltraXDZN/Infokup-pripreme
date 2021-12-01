#Day one:
##Sonar Sweep - Part One


In this assignment, it was required to create an infinite loop that is running until the end of user input.
For that, I've also created an empty list (array) and outside input that is collected before entering the main loop.
The following code can be seen here as:
```python
inputs = []
a = input()
while a != "":
    inputs.append(int(a))
    a = input()
```
After input is done, it was needed to write the actual logic of the program. 

I approached this by creating a new integer and assigning its value to 0, then creating another loop and looping over all elements in an array and checking whether the current
element is greater than the element before. That code can be seen as:
```python
c = 0
for i in range(len(inputs)):
    if inputs[i] > inputs[i - 1]:
        c += 1
```
After that, all that is left to do is to print out the c variable.
```python
print(c)
```
