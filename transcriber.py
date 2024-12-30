import asyncio
import aiohttp
import json

url = "wss://api.deepgram.com/v1/listen"
headers = {"Authorization" : "Token 743d47adb613115d96850015d9122fcc11709c34"}

audio_data = "http://stream.live.vc.bbcmedia.co.uk/bbc_world_service"

async def transcriber():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url, headers = headers) as ws:
            print("web socket connection established")
            
            async def stream_speech():
                try:
                    async with session.get(audio_data) as response:
                        async for chunk in response.content.iter_chunked(4096):
                            if chunk:
                                await ws.send_bytes(chunk)
                except aiohttp.ClientError as e:
                    print(f"error fetching audio stream {e}")
                
            async def stream_text():
                try:
                    async for message in ws:
                        try:
                            response = json.loads(message.data)
                            if response.get('type') == "Results":
                                transcript = response['channel']['alternatives'][0].get('transcript', "")
                                if transcript:
                                    print(f"transcript: {transcript}")
                        except json.JSONDecodeError as e:
                            print(f"json decode erro: {e}")
                        except KeyError as e:
                            print(f"key error: {e}")
                except Exception as e:
                    print(f"websocket error: {e}")
                    
            await asyncio.gather(stream_speech(), stream_text())
            await close_websocket(ws)
                
async def close_websocket(ws):
    close_msg = {'type' : 'ClsoeStream'}
    await ws.send_str(close_msg)
    await ws.close()
   
#Altered main function 
def main():
    asyncio.run(transcriber())
        
if __name__ == "__main__":
    main()




#Existed main function
'''def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(transcriber())
    except KeyboardInterrupt:
        print("websecket connection closing")
        loop.run_until_complete(close_websocket())'''