import requests

# GitHub 리포지토리 정보
repository_owner = 'your username'
repository_name = 'your repository'
repository_branch = 'your branch'  
access_token = 'your access token'  

# 파일 정보
extra_problems = []
file_extensions = [".c", ".cpp", ".py"]

def get_folder_file_list(folder_path):
    api_url = f'https://api.github.com/repos/{repository_owner}/{repository_name}/contents/{folder_path}?ref={repository_branch}'
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(api_url, headers=headers)
    data = response.json()
    file_list = []
    for item in data:
        if 'type' in item and item['type'] == 'file' and any(item['name'].endswith(ext) for ext in file_extensions):
            file_name, _ = item['name'].split(".")
            file_list.append(int(file_name))
    
    return file_list

def main():
    with open('solved_number_list.txt', 'r') as solved_number_file:
        problem_numbers = list(map(int, solved_number_file.read().split()))
    
    problem_numbers += extra_problems
    problem_numbers.sort()
    print(len(problem_numbers))
    
    uploaded_files = []
    not_uploaded = []
    
    for i in range(1000, 30000, 1000):
        print(f"check range: {i:05d}~{i+999:05d}")
        folder_name = f"{i:05d}~{i + 999:05d}"
        for j in range(i, i + 1000, 100):
            sub_folder_name = f"{j:05d}~{j + 99:05d}"
            folder_path = f"백준/{folder_name}/{sub_folder_name}"
            uploaded_files += get_folder_file_list(folder_path)
        
    print(len(uploaded_files), len(problem_numbers))

    not_uploaded = list(set(problem_numbers) - set(uploaded_files))
    not_uploaded.sort()
    print(not_uploaded)

    with open('not_uploaded.txt', 'w') as not_uploaded_file:
        not_uploaded_file.write(f"Number of problems not uploaded: {len(not_uploaded)}\n")
        count = 0
        for problem_number in not_uploaded:
            if count != 0 and problem_number // 1000 != (not_uploaded[count - 1]) // 1000:
                not_uploaded_file.write('\n')
            if count % 10 == 0:
                not_uploaded_file.write('\n')
            not_uploaded_file.write(f"{problem_number:05d} ")
            count += 1
            
if __name__ == "__main__":
    main()
