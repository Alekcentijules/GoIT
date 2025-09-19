import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("The Path not exist!\n")
else:
    path = sys.argv[1]
    print(f"Send path: {path}\n\n")

print(f"Python version: {sys.version}\n")
print(f"Platform: {sys.platform}\n")
print(f"Module search paths: {sys.path}\n\n")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Size of list: {sys.getsizeof(my_list)} bytes\n")
print(f"Modules dict: {sys.modules}")