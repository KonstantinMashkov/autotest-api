import httpx

# print("GET")
# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# print(response.request.headers)
# print(response.json())

# print("POST")
# data = {
#     "title": "test_new",
#     "completed": False,
#     "userId": 1 
# }
# response2 = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
# print(response2.status_code)
# print(response2.request.headers)
# print(response2.json())

# print("POST")
# data2 = {"username": "test_user", "password": "123456"}
# response3 = httpx.post("https://httpbin.org/post", data=data2)
# print(response3.status_code)
# print(response3.request.headers)
# print(response3.json()) 


# print("GET")
# headers = {"Authorization": "Bearer my_secret_token"}
# response4 = httpx.get("https://httpbin.org/get", headers=headers)
# print(response4.request.headers)
# print(response4.json())


# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)    
# print(response.json()) 

# files = {"file": ("example_file.txt", open("example_file.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
# print(response.json())  



# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
# print(response1.json())  # Данные первой задачи
# print(response2.json())  # Данные второй задачи


# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = client.get("https://httpbin.org/get")
# print(response.json())  # Заголовки включены в ответ
# client.close()


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
    
    
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")