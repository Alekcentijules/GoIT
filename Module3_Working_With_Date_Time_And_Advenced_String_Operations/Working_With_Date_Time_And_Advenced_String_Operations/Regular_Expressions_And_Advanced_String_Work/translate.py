intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "*******This is string magic*******"
print(f"\nstr.translate(): {str.translate(trantab)}")
print(f"trantab 1: {trantab}")



intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is a story of Ma Baker..."
print(f"\nstr.translate(): {str.translate(trantab)}")
print(f"trantab 2: {trantab}")



symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
map_ = {}

for s, c in zip(symbols, code):
    map_[ord(s)] = c
    map_[ord(s.lower())] = c
result = "34 DF 56 AC".translate(map_)
print(f"\nord: {result}")
print(map_)



morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello Mars!"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(f"\ntable_morze_dict: {result}")
print(table_morze_dict)

