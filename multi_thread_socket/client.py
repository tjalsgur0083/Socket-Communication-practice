import socket
from urllib import response

HOST = 'localhost'
PORT = 8080

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print(client.recv(1024).decode('utf-8'))
    
    while True:
        try:
            guess = input("숫자를 입력하세요: ")
            client.send(guess.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(response)
            if "축하합니다" in response:
                break
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력하세요.")

    client.close()

if __name__ == "__main__":
    main()