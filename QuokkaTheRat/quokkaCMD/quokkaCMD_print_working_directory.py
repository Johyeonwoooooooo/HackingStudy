import os


current_directory_path = os.path.dirname(os.path.abspath(__file__))
print(f"script executing path : {current_directory_path}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.system("dir")

os.system("pause")