import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    # check file input ouput
    check_command_line_arg()

    # open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # open shirt
    shirtfile = Image.open("shirt.png")

    # get the size of the shirt
    size = shirtfile.size
    # resize
    muppet = ImageOps.fit(imagefile, size)
    # past
    muppet.paste(shirtfile, shirtfile)
    # create ouput
    muppet.save(sys.argv[2])

def check_command_line_arg():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line agruments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")

    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and ouput have different extensions")

def check_extension(file):
    if file in ['.jpg', '.jepg', '.png']:
        return True
    return False

if __name__ == "__main__":
    main()
