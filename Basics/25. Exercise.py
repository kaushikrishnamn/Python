picture = [
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0]
]


def print_picture(pic, pixel_character):
    for image in pic:
        for pixel in image:
            if pixel:
                print(pixel_character, end="")
            else:
                print(" ", end="")
        print("")


print_picture(picture, "$")
print_picture(picture, "*")
