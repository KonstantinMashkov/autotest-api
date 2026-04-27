import httpx
from tools.fakers import fake


# Аутентификация
login_payload = {
    "email": fake.email(),
    "password": fake.password(),
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f'Status: {login_response.status_code}, Login response: {login_response_data}')

create_files_headers = {
   "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

create_file_response = httpx.post(
    'http://localhost:8000/api/v1/files', 
    data={'filename': 'image.jpg', 'directory': 'test_upload_file'}, 
    files={'upload_file': open('testdata/files/image.jpg', 'rb')},
    headers=create_files_headers
    )

create_file_response_data = create_file_response.json()
print(f'{create_file_response.status_code}: Data: {create_file_response_data}')