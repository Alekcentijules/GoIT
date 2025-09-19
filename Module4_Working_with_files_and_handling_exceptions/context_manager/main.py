fh = open("test_file_2_1.txt", "w")
try:
    fh.write("Some text")
finally:
    fh.close()



with open("test_file_2_1.txt", "w") as fh:
    fh.write("Second some text...")



with open("test_file_1_5.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)