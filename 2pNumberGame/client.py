import socket
from urllib import response

HOST = 'localhost'
PORT = '8000'

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, int(PORT)))

    while True:
        try:
            response = client.recv(1024).decode('utf-8')
            print(response)
            if "축하합니다" in response:
                break
            guess = input("숫자를 입력하세요: ")
            client.send(guess.encode('utf-8'))
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력하세요.\n")

    client.close()

if __name__ == "__main__":
    main()