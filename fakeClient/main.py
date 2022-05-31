import websocket
import time

HOSTNAME = '127.0.0.1:8000'
URL = f'ws://{HOSTNAME}/data/'
DATA = ['135.5;8000', 'deactivate']

def main():
    ws = websocket.create_connection(URL)
    print(ws.recv())
    while True:
        ws.send(';'.join(DATA))
        print(ws.recv())
        time.sleep(1)
        

if __name__ == '__main__':
    main()
