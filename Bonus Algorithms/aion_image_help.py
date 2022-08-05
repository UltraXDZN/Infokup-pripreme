def round_end(value, round_digits):
    return format(round(value, round_digits), "." + str(round_digits) + "f")


name = input()

# Full Image Size
FullWidth = int(input())
FullHeight = int(input())

# Image Position
imageX = int(input())
imageY = int(input())

# Image Size
imageSizeX = int(input())
imageSizeY = int(input())

# Rows n Cols
rows = int(input())

for x in range(rows):
    print()
    print(f"Frame {x + 1}:")
    print(f"U: {round_end(x * imageSizeX / FullWidth, 6)}\tV: {round_end(1 * imageSizeY / FullHeight, 6)}")
    print(f"U: {round_end((x + 1) * imageSizeX / FullWidth, 6)}\tV: {round_end((1 + 1) * imageSizeY / FullHeight, 6)}")
