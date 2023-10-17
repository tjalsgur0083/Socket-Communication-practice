import socket
import random
import threading

HOST = 'localhost'
PORT = '8000'

secret_number = random.randint(1, 100)

clients = []

def handle_client(client_socket, client_number):
    client_socket.send('접속에 성공했습니다. 어서오세요 \n'.encode('utf-8'))
    while True:
        try:
            guess = int(client_socket.recv(1024).decode('utf-8'))
        except ValueError:
            client_socket.send('유효하지 않은 입력입니다. 숫자를 입력하세요.\n'.encode('utf-8'))
            continue

        for client_socket in clients:
            if guess == secret_number:
                client_socket.send(f'축하합니다! 정답{secret_number}을(를) 맞췄습니다!\n'.encode('utf-8'))
                break
            elif guess < secret_number:
                client_socket.send('입력한 숫자가 작습니다.\n'.encode('utf-8'))
            elif guess > secret_number:
                client_socket.send('입력한 숫자가 큽니다.\n'.encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, int(PORT)))
    server.listen(2)
    
    print(f"서버 대기중 ({HOST}:{PORT})\n")
    print(f"정답: {secret_number}\n")

    while len(clients) < 2:
        client, addr = server.accept()
        print(f"{addr[0]}:{addr[1]}에서 접속하였습니다.\n")
        clients.append(client)
        client_handler = threading.Thread(target = handle_client, args = (client, len(clients)))
        client_handler.start()
    
    server.close()

if __name__ == "__main__":
    main()