# Search in the strings
s = "Mr, Hey Mr!"

start = 0
end = 22

print(s.find("Mr", start, end))
print(s.find("Mr"))
print(s.find("Ser"))
print(s.rfind("Mr"))

print(s.index("Mr"))
print(s.rindex("Mr"))
# print(s.index("Ser"))



# Splitting and merging rows
text = "Hello Doc!"
result = text.split()
print(f"\ntext.split(): {result}")

text = "I'm your venus, I'm your fire!"
result = text.split(',')
print(f"text.split(\",\"): {result}")



list_of_potions = ["Bezoar Stone", "Moonstone", "Opal", "Ruby"]
result = " ".join(list_of_potions) + " Abracadabra TYDYSH'!!!"
print(f"\n\" \".join(list_of_potions): {result}")

elements = ["earth", "air", "fire", "water"]
result = ", ".join(elements)
print(f"\", \".join(elements): {result}")



clean = "             It's the space.......               ".strip() + "."
print(f"\n\" \".strip(): {clean}")



print("\n", 'RightHook'.removeprefix("Right"))
print('LeftHook, UPPERCUT!!!'.removeprefix("Hook"))

print("\n", 'RightHook'.removesuffix("Right"))
print('LeftHook, UPPERCUT!!!'.removesuffix("Hook"))
print('LeftHook, UPPERCUT!!!'.removesuffix("UPPERCUT!!!"))



url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split("?")
print(f"\n{query}")

obj_query = {}
for el in query.split("&"):
    key, value = el.split("=")
    obj_query.update({key: value.replace("+", " ")})
print(f"obj_query: {obj_query}")


