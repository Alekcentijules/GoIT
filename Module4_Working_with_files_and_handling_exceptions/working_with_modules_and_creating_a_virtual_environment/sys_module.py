import sys


print(sys.modules["sys"])
print(sys.modules["sys"], "\n")

print(sys.modules.keys(), "\n")

print(sys.builtin_module_names, "\n\n")  

for arg in sys.argv:
    print(arg)