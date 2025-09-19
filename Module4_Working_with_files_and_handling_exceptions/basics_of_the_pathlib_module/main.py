from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")

print("Name:", p.name)
print("Suffix:", p.suffix)
print("Parent:", p.parent)



from pathlib import Path

p = Path("example.txt")
p.write_text("IT'S JOHNY!")

print(f"\n{p.read_text()}")
print(f"Exists: {p.exists()}")



# Creating Paths
from pathlib import Path

path_unix = Path("/usr/bin/python3")
path_windonw = Path("C:/Users/Username/Documents/file.txt")



from pathlib import Path

base_path = Path("/usr/bin")
full_path = base_path / "subdir" / "script.py"

print(f"\n{full_path}")



# Relative and Absolute Paths
from pathlib import Path

relative_path = Path("basics_of_the_pathlib_module/main.py")
absolute_path = relative_path.absolute()

current_working_directory = Path(r"C:\Users\ohala\VSCodeProjects\GoIT")
relative_path = absolute_path.relative_to(current_working_directory)
print(f"\n{absolute_path}")
print(relative_path)



# Manipulating path components
from pathlib import Path

original_path = Path("basics_of_the_pathlib_module/main.py")
new_path = original_path.with_name("updated_main.py")

print(f"\nOld filename: {original_path}")
print(f"Updated filename: {new_path}")




from pathlib import Path

original_path = Path("GOIT/example.txt")
new_path = original_path.with_suffix(".md")

print(f"\nNew filename: {new_path}")



# from pathlib import Path

# original_path = Path("example.txt")
# new_path = original_path.with_name("update_example.txt")
# original_path.rename(new_path)

# print(f"\nUpdated filename: {new_path}")



# Read and write files
from pathlib import Path

file_path = Path("example.txt")
file_path.write_text("IT'S JOHNY AGAIN!!!!!", encoding="utf-8")
text = file_path.read_text(encoding="utf-8")

print(f"\n{text}")



from pathlib import Path

with open("byte_file.bin", "wb") as file:
    file.write(b"It's a byte string")

file_path = Path("byte_file.bin")
data = b"It's an updated byte string!"
file_path.write_bytes(data)
binary_text = file_path.read_bytes()

print(f"Data from byte_file.bin: {binary_text}\n")



# Working with directories
from pathlib import Path

directory = Path("./")

print("Elements From This Directory:")
for path in directory.iterdir():
    print(path)



from pathlib import Path

directory = Path("/GOIT/new_folder")
directory.mkdir(parents=True, exist_ok=True)
directory.rmdir()



from pathlib import Path

path = Path("./example.txt")

print("\n")
if path.exists():
    print(f"{path} exist!")

if path.is_dir():
    print(f"{path} is directory!")

if path.is_file():
    print(f"{path} is file!")



# Move and copy files
# import shutil
# from pathlib import Path

# source = Path("example.txt")
# destination = Path("/Module4_Working_with_files_and_handling_exceptions/basics_of_the_pathlib_module/example.txt")

# shutil.copy2(source, destination)



# import shutil
# from pathlib import Path

# source = Path("example.txt")
# destination = Path("/Module4_Working_with_files_and_handling_exceptions/basics_of_the_pathlib_module/example.txt")

# shutil.move(source, destination)



from pathlib import Path

file_path = Path("./example.txt")
size = file_path.stat().st_size

print(f"\nSize of {file_path}: {size} byte")



from pathlib import Path
import time

file_path = Path("./example.txt")
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"\nCreation time of {file_path}: {time.ctime(creation_time)}")
print(f"Modification time of {file_path}: {time.ctime(modification_time)}")



from pathlib import Path

file_path = Path("./test_file_1_3.txt")

if file_path.exists():
    file_path.unlink()
    print(f"File {file_path} was deleted")
else:
    print(f"File {file_path} doesn't exist")



from pathlib import Path

file_path = Path("./test_file_1_5.txt")
file_path.unlink(missing_ok=True)