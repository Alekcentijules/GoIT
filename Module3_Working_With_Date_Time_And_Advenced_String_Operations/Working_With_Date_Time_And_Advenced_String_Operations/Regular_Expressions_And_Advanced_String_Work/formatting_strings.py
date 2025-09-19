for num in range(8):
    val = f"int: {num:d}; hex: {num:#x}; oct: {num:#o}; bin: {num:#b}"
    print(val)



price = 3.14
quantity = 7
total = f"Total: {price * quantity:.2f}"
print(f"\n{total}\n")



width = 7
for num in range(13):
    print(f"{num:^12} {num**2:^12} {num**3:^12}")



name = "Alice in Disnayland"
formatted = f"\n{name:>30}"
print(formatted)



completion = 0.789
formatted = f"\n:.1%: {completion:.1%}"
print(formatted)



proggress = 0.5
formatted = f"\n:.0%: {proggress:.0%}"
print(formatted)