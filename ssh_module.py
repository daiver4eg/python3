import paramiko
import clear_data

#host = '192.168.88.1'


def mikrotik_request(host):
    wifi_key = ""
    user = 'test'
    secret = 'test'

    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    print("connecting...")
    client.connect(hostname=host, username=user, password=secret, port=port)
    # Выполнение команды
    print("receive data")
    stdin, stdout, stderr = client.exec_command('/interface wireless security-profiles print')
    # Читаем результат
    data = stdout.read() + stderr.read()
    client.close()
    bytestr = data
    print("start searching in data")
    #print("Пароль ВиФи содержит одна из строк ниже")
#ищем нужные нам строчки, отсекаем лишнее
    index = -1
    while True:
        index = bytestr.find(b'wpa2-pre-shared-key=', index + 1)
        # print(index)
        #print(bytestr[index + 16:index + 16 + 16])
        #wifi_key += str(bytestr[index + 16:index + 16 + 19]) + "\n"
        wifi_key += str(bytestr[index + 16:index + 16 + 19])
        if index == -1:
#Очистка строки!!!
            #print("end")
            #print(len(wifi_key))
            #print(type(wifi_key))
            print("До очистки", wifi_key)
            wifi_key = wifi_key.replace("'", "")
            wifi_key = wifi_key.replace('"', "_")
            print("После очистки", wifi_key)
            break


#добавляем в переменную index_list значения индексов начало-конец пароля
    index = 0
    index_list = []
    while True:
        index = wifi_key.find("_", index + 1)
        index_list.append(index)
        if index == -1:
            break


#вызываем функцию вытаскивания данных по нашим индексам
#    return print(clear_data.clear_wifi_key(index_list,wifi_key))
    return clear_data.clear_wifi_key(index_list, wifi_key)


#mikrotik_request(host)





