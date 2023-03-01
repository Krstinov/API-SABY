import auth

print("Выберите сервер подключения 1-Боевой, 2-FIX")
serv = input()
if serv == "1": fix = ""
elif serv == "2": fix = "fix-"
else:
    print ("Не был выбран сервер, пытаюсь подключиться к тестовой среде")
    fix = "fix-"
server_auth = "https://" + fix +"online.sbis.ru/auth/service/"
server_requests =  "https://" + fix +"online.sbis.ru/service/?srv=1"
print("Введите логин:")
login = input()
print("Введите пароль:")
password = input()
X_SBISSessionID = auth.auth(login, password, server_auth)

if X_SBISSessionID is not None:
    print("Идентификатор авторизации: " + X_SBISSessionID)