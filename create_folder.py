START = 30000
END = 40000

import os

current_directory_path = os.path.dirname(os.path.abspath(__file__))


for i in range(START, END, 1000):
    root_folder_name = f"{i:05d}~{i + 999:05d}"
    root_folder_path = os.path.join(current_directory_path, root_folder_name)
    os.makedirs(root_folder_path, exist_ok=True)
    for j in range(i, i+1000, 100):
        sub_folder_name = f"{j:05d}~{j+99:05d}"
        sub_folder_path = os.path.join(root_folder_path, sub_folder_name)
        os.makedirs(sub_folder_path, exist_ok=True)
        for k in range(j, j+100):
            file_name = f"{k:05d}.txt" 
            file_path = os.path.join(sub_folder_path, file_name)
            with open(file_path, 'a'):
                pass
            
        
