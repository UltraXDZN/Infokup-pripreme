sat = int(input())
minute = int(input())
vrijeme_putovanja = int(input())

if (sat == 6):
    vrijeme_putovanja -= 60 - minute
elif (minute > 30):
    vrijeme_putovanja += minute - 30

temp_minute = 0
minute += vrijeme_putovanja
if (minute >= 60):
    temp_minute = minute - 60
    minute = temp_minute
    sat += 1


print(vrijeme_putovanja)

print(sat, minute)
