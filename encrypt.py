import os
from pathlib import Path

# Read file
with open("input_text.txt") as f:
    plain_text = f.read()

# Set key
KEY_DEFAULT = 10
key = os.getenv("KEY", KEY_DEFAULT)

# Prepare outputs
encrypted = ""
output_folder = "data/outputs/"
Path(output_folder).mkdir(parents=True, exist_ok=True)

for c in plain_text:

    if c.isupper():  # check if it's an uppercase character

        c_index = ord(c) - ord('A')

        # shift the current character by key positions
        c_shifted = (c_index + key) % 26 + ord('A')

        c_new = chr(c_shifted)

        encrypted += c_new

    elif c.islower():  # check if its a lowercase character

        # subtract the unicode of 'a' to get index in [0-25) range
        c_index = ord(c) - ord('a')

        c_shifted = (c_index + key) % 26 + ord('a')

        c_new = chr(c_shifted)

        encrypted += c_new

    elif c.isdigit():

        # if it's a number,shift its actual value
        c_new = (int(c) + key) % 10

        encrypted += str(c_new)

    else:

        # if its neither alphabetical nor a number, just leave it like that
        encrypted += c

    # Write file
    with open(output_folder+"/output_text.txt", "w+") as f:
        f.write(encrypted)
