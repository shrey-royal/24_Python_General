# file = open('somefile.txt', 'w')
# try:
#     file.write('this is some data')
# finally:
#     file.close()

"""
file operation modes:
1. 'r' -> open text file for reading text
2. 'w' -> open text file for writing text
3. 'a' -> open text file for appending text
3. '+' -> open text file for updating (both reading & writing)
"""
# ------------------------------------------------------------------
# reading data into file
# ------------------------------------------------------------------

# with open('somefile.txt', 'a') as file:
#     file.write("\nthis is another one")

# with open('somefile.txt', 'r') as f:
#     lines = f.readlines()

# print(lines)
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     contents = f.read()
#     print(contents)
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     [print(line) for line in f.readlines()]
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     [print(line.strip()) for line in f.readlines()]
# ------------------------------------------------------------------

# with open('somefile.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
        # print(line.strip())
# ------------------------------------------------------------------

# with open('somefile.txt') as f:
#     for line in f:
#         print(line.strip())
# ------------------------------------------------------------------

# with open('anime_dialogues.txt', encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# writing data into file
# ------------------------------------------------------------------

lines = ["Arin likes to eat", "Dhairya excel at SQL", "All GNR peoples loves to learn Python"]

# with open('gnr.txt', 'w') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')
# ------------------------------------------------------------------

# with open('gnr.txt', 'w') as f:
    # f.writelines(lines)
    # f.write('\n'.join(lines))
# ------------------------------------------------------------------

# added_text = ["", "This is appended text", "The End"]

# with open('gnr.txt', 'a') as f:
#     f.write('\n'.join(added_text))

# dialogue = "偶然だよ。それに裏が出ても、表が出るまで何度でも投げ続けようと思ってたから"

# with open('dialogue.txt', 'w', encoding='utf-8') as f:
#     f.write(dialogue)

# ------------------------------------------------------------------

# with open('docs/somefile.txt', 'x'):     # exclusive creation
#     pass

# ------------------------------------------------------------------

# check if file already exists
###############################
# from os.path import exists

# file_exists = exists('abcd.txt')
# print(file_exists)
###############################

# import os.path
# print(os.path.exists('gnr.pdf'))
###############################

# from os.path import exists as file_exists

# print(file_exists('somefile.txt'))
# ------------------------------------------------------------------

# we have another module called PATHLIB
from pathlib import Path

path = Path('somefile.txt')

print(path.is_file())