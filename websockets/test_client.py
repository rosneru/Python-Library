import asyncio
import websockets

async def hello(uri: str) -> None:
    async with websockets.connect(uri, subprotocols=["lws-minimal"]) as websocket:
        while True:
            user_input = input("send to ws >> ")
            if(len(user_input) == 0):
                break

            server_cmd = user_input + '\n'
            await websocket.send(server_cmd)
            result = await websocket.recv()
            print(result)

if __name__ == "__main__":
    print('========================================')
    print('Send JSON commands to Websocket, e.g.')
    print('  { "id" : "CompanyName" }')
    print('========================================\n')
    asyncio.get_event_loop().run_until_complete(hello('ws://localhost:7681'))
    print("Finished.")
