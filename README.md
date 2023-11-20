# github_upload
<br>백준 문제를 긁어서 solved_number_list.txt에 저장한 후 check_github_not_uploaded.py로 아직 안 올린 파일을 확인하고, upload.py로 파일을 업로드합니다.</br>
개인 액세스 토큰이 필요합니다. 다른 사람에게 보여주지 마시고 설정에서 발급 받으세요.

<br>
# 로컬 폴더 구조 (백준 폴더는 GitHub와 동일, 백준 정보는 로컬 폴더로 존재, 백준과 백준 정보 폴더는 부모 디렉토리가 같아야 합니다.)

## 백준
- 01000~01999
  - 01000~01099
    - 01000.c
    - 01010.py
  ...
- 29000~29999

## 백준 정보
- upload.py : 업로드 해줍니다.
- check_github_not_uploaded.py : 업로드 되지 않은 항목을 로컬 폴더에서 찾습니다.
- create_folder.py - 일정한 형태로 현재 디렉토리에 디렉토리를 생성합니다.
- not_uploaded.txt : 업로드 되지 않은 항목입니다.
- solved_number_list.txt - 푼 문제 수입니다.

</br>
