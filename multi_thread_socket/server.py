from http import client, server
import socket
import random
import threading

HOST = 'localhost'
PORT = 8080

secret_number = random.randint(1, 100)

def Welcome_client(client_socket):
    client_socket.send('접속에 성공했습니다. 어서요세요.\n'.encode('utf-8'))
    while True:
        try:
            guess = int(client_socket.recv(1024).decode('utf-8'))
            # 클라이언트로부터 최대 1024바이트의 데이터 수신
        except ValueError:
            client_socket.send('유효하지 않은 입력입니다. 숫자를 입력하세요\n'.encode('utf-8'))
        if guess == 0:
            client_socket.send('종료'.encode('utf-8'))
            break
        if guess == secret_number:
            client_socket.send(f'축하합니다!!!!!!!!!! 정답{secret_number}을(를) 맞췄습니다!\n'.encode('utf-8'))
            break
        elif guess < secret_number:
            client_socket.send('추측한 숫자가 작습니다.\n'.encode('utf-8'))
        else:
            client_socket.send('추측한 숫자가 큽니다.\n'.encode('utf-8'))
    client_socket.close()

def main():
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
   server.bind((HOST, PORT))
   server.listen(5)
   print(f"서버 대기중{HOST}:{PORT}")
   print(f"정답:{secret_number}")
   
   while True:
       client, addr = server.accept()
       print(f"다음에서 접속하였습니다. {addr[0]}:{addr[1]}")
       client_handler = threading.Thread(target=Welcome_client, args=(client,))
       client_handler.start()

if __name__ == "__main__":
    main()