import socket
import random

HOST = ""
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('server start.')

    conn,addr = s.accept()
    with conn:
        secret_number = random.randint(1, 100)
        print(f'클라이언트  접속함:{addr}, 정답:{secret_number}')
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f'데이터:{data}')

            try:
                guess = int(data)
            except ValueError:
                conn.sendall(f'입력값이 올바르지 않음:{data}'.encode('utf-8'))
                continue
            if guess == 0:
                conn.sendall(f'종료'.encode('utf-8'))
                break
            if guess < secret_number:
                conn.sendall("추측한 숫자가 너무 작음".encode('utf-8')) 
            elif guess > secret_number:
                conn.sendall("추측한 숫자가 너무 큼".encode('utf-8')) 
            else:
                conn.sendall(f"!!!!정답! 시크릿 숫자는{secret_number}입니다!".encode('utf-8'))
                break