fh = open("test_file_1_1.txt", "w")
symbols_written = fh.write("Hello Doc!")
print(symbols_written)
fh.close()



fh = open("test_file_1_2.txt", "w+")
fh.write("I'm here, Mr Brown!")
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)

fh.close()



fh = open("test_file_1_3.txt", "w")
fh.write("Hello! It's I'm again.")
fh.close()

fh = open("test_file_1_3.txt", "r")
all_file = fh.read()
print(all_file)

fh.close()



fh = open("test_file_1_4.txt", "w")
fh.write("SAY HELLO TO MY LITTLE FRIEND!!!!*****")
fh.close()

fh = open("test_file_1_4.txt", "r")
while True:
    symbol = fh.read(2)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()



fh = open("test_file_1_5.txt", "w")
fh.write("first line\nsecond line\nthied line")
fh.close()

fh = open("test_file_1_5.txt", "r")
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.seek(0)
lines = fh.readlines()
print(lines)

fh.seek(0)
lines = [el.strip() for el in fh.readlines()]
print(lines)

position = fh.tell()
print(position)

fh.close()

