import requests
import os
import base64

# GitHub 리포지토리 정보
repository_owner = 'your username'
repository_name = 'your repository name'
repository_branch = 'your branch'  
access_token = 'your access token'  

# 파일 확장자 및 경로 정보
file_extensions = [".c", ".cpp", ".py"]
current_directory_path = os.path.dirname(os.path.abspath(__file__))
baekjoon_directory_path = os.path.dirname(current_directory_path)
not_upload_file = os.path.join(current_directory_path, "not_uploaded.txt")

def find_not_uploaded_numbers(file_path : str):
    not_uploaded_list = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith("N"):
                try:
                    num_list = [int(num) for num in line.strip().split()]
                except ValueError:
                    pass
                not_uploaded_list += num_list
    return not_uploaded_list

def upload_files_in_folders(numbers : list[int]):
    for number in numbers:
        folder_num = (number//1000)*1000
        folder_name = f"{folder_num:05d}~{folder_num + 999:05d}"
        
        sub_folder_num = folder_num + ((number - folder_num)//100)*100
        sub_folder_name = f"{sub_folder_num:05d}~{sub_folder_num + 99:05d}"
        
        problem_number = f"{number:05d}"
        
        local_folder_path = os.path.join(os.path.dirname(current_directory_path), folder_name, sub_folder_name)
        github_folder_path = f"백준/{folder_name}/{sub_folder_name}"
        
        upload_files(local_folder_path, problem_number, github_folder_path)

def upload_files(local_folder_path: str, 
                 problem_number: str, 
                 github_folder_path: str):
    
    for ext in file_extensions:
        file_name = f"{problem_number}{ext}"  
        full_file_path = os.path.join(local_folder_path, file_name)  
        
        if os.path.exists(full_file_path):
            with open(full_file_path, 'rb') as file:
                file_content = file.read()
            success, message = upload_file(github_folder_path, file_name, file_content)
            print(message)
            
        else:
            pass

def upload_file(folder_path :str, 
                file_name: str, 
                file_content: str) -> list:
    
    url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{folder_path}/{file_name}'

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    encoded_content = base64.b64encode(file_content).decode('utf-8')

    data = {
        'message': f'Add {file_name}',
        'content': encoded_content,
        'branch': repository_branch
    }

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        success = True
        message = f'Successfully uploaded {folder_path}/{file_name}.'
    else:
        success = False
        message = f'Failed to upload {folder_path}/{file_name}. Status code: {response.status_code}.'
        print(response.json())

    return success, message

def main():
    not_upload_list = find_not_uploaded_numbers(not_upload_file)

    upload_files_in_folders(not_upload_list)
    
if __name__ == "__main__":
    main()
