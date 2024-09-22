import requests

response = requests.get('http://localhost:8000/mean', json=[1, 2.0, 3.0])

if response.status_code == 200:
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Ошибка при разборе JSON, возможно, сервер вернул некорректный ответ.")
else:
    print(f"Ошибка {response.status_code}: {response.text}")