import asyncio
import queue
import threading
import time

class WebSocketClient:
    _host: str
    _port: int
    _is_running: bool
    _command_queue: queue.Queue()
    _result_queue: queue.Queue()

    def __init__(self): 
        self._is_running = False
        self._command_queue = queue.Queue()
        self._result_queue = queue.Queue()


    def connect(self) -> None:
        self._is_running = True
        while self._is_running == True:
            time.sleep(0.1)
            if not self._command_queue.empty():
                cmd = self._command_queue.get()
                if cmd == 'name':
                    self._result_queue.put("I'm the WebSocket server.")
                elif cmd == 'age':
                    self._result_queue.put("I'm 2735 days old.")
                else:
                    self._result_queue.put("I don't undertsand your question.")

        print("WebSocket loop finished.")


    def send_recv(self, cmd: str) -> str:
        self._command_queue.put(cmd)
        while self._result_queue.empty():
            time.sleep(0.1)
        
        result = self._result_queue.get()
        return result

    def stop(self):
        self._is_running = False



# asyncio.run(main())
websocket = WebSocketClient()
# asyncio.create_task(asyncio.get_event_loop().run_until_complete(websocket.connect()))
thread = threading.Thread(target=websocket.connect, args=())
thread.daemon = True
thread.start()



print('Ask the server for its "name" or "age". Empty line for exit.')
while True:
    user_input = input("send to ws >> ")
    if(len(user_input) == 0):
        websocket.stop()
        break
    
    result = websocket.send_recv(user_input)
    print(result + "\n")
