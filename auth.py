import requests


def auth(log, password,server_auth):

    login = log
    password = password
    request_auth = saby_auth(login, password)
    return run_command(request_auth, server_auth)


def saby_auth(login, password):
    auth = {
        "jsonrpc": "2.0",
        "method": "СБИС.Аутентифицировать",
        "params": {
            "Параметр": {
                "Логин": login,
                "Пароль": password
            }
        },
        "id": 0
    }
    return auth


def run_command(request, service):
    headers = {"Content-Type": "application/json-rpc;charset=utf-8"}
    request_command = requests.post(service, json=request, headers=headers)
    if request_command.status_code == 200:
        request_json = request_command.json()
        return request_json["result"]
    else:
        print("Не получилось авторизоваться, код выполнения запроса: " + str(request_command.status_code) + "\n " + str(request_command.json()["error"]['message']))
        return None