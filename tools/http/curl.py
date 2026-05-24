import httpx
from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    Генерирует команду cURL из HTTP-запроса httpx.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    # Создаем список с основной командой cURL, включая метод и URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # Добавляем тело запроса, если оно есть (например, для POST, PUT)
    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    # Объединяем части с переносами строк, исключая завершающий `\`
    return " \\\n  ".join(result)


body = {
    "email": "user@example.com",
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=body)
print(make_curl_from_request(response.request))

def request_hook(request: httpx.Request):
    print(f"Запрос: {request.method} {request.url}")

client = httpx.Client(event_hooks={"request": [request_hook]})
response = client.get("https://example.com")