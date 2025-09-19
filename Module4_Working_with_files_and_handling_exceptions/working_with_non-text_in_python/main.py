with open("raw_data_1.bin", "wb") as fh:
    fh.write(b"Hello again!")

s = b"Venus"
print(s[3])



byte_str = "Don't turn your back on me".encode()
print(f"\n.encode(): {byte_str}")



# Convert numbers to byte strings
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(f"\nbyte_numbers: {byte_numbers}")
print(f"bytes(): {bytes(5)}")
print(f"hex(): {hex(numbers[2])}\n")

for num in numbers:
    print(hex(num))



# String encoding (ASCII, UTF-8, CP1251)
string = "Abracadabra..... b00000m*****"
string_2 = "Абракадабра..... бууууум*****"

print(f"\nord(): {ord(string[0])}")
print(f"chr(): {chr(65)}")

utf_8 = string.encode()
utf_8_2 = string_2.encode()
print(f"UTF-8: {utf_8}")
print(f"UTF-8: {utf_8_2}")

utf_16 = string.encode("utf-16")
utf_16_2 = string_2.encode("utf-16")
print(f"UTF-16: {utf_16}")
print(f"UTF-16: {utf_16_2}")

cp_1251 = string.encode("cp1251")
cp_1251_2 = string_2.encode("cp1251")
print(f"CP-1251: {cp_1251}")
print(f"CP-1251: {cp_1251_2}")

string_from_utf_16 = utf_16.decode("utf-16")
print(string == utf_16)
print(string == string_from_utf_16, "\n")



print(b"PUSH IT TO THE LIMIT!!!!".decode("utf-16"))



with open("test_file_1_1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)



# Byte array
byte_array = bytearray(b"Kill Bill")
byte_array[0] = ord("B")
byte_array[5] = ord("K")
print(f"\n{byte_array}")



byte_array = bytearray(b"My Voodoo Child")
byte_array.append(ord("!"))
print(F"\n{byte_array}")



byte_array = bytearray(b"IIIIIIT'S JOHNYYYY!!!!!!")
string = byte_array.decode("utf-8")
print(f"\n{string}: {type(string)}")



# Comparing rows
text = "Python - it's future!"
print(f"\n{text.casefold()}")



german_word = 'straße'
search_word = 'STRASSE' 

lower_comparison = german_word.lower() == search_word.lower()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Comparison with lower(): {lower_comparison}")
print(f"Comparison with casefold(): {casefold_comparison}")

