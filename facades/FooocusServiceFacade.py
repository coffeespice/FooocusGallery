import uuid
import websockets
import asyncio
import json
from websockets.exceptions import ConnectionClosed
from services.ConfigService import fooocus_ip

session_hash = uuid.uuid4().hex


def data_hash(fn_index):
    return json.dumps({"fn_index": fn_index, "session_hash": session_hash})


async def execute_web_socket(data, fn_index):
    async with websockets.connect(f"ws://{fooocus_ip()}/queue/join") as websocket:
        while True:
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=1.0)
            except asyncio.TimeoutError:
                pass
            except ConnectionClosed as _:
                break

            if "send_hash" in response:
                await websocket.send(data_hash(fn_index))

            if "send_data" in response:
                data = json.dumps(
                    {"data": data, "event_data": None, "fn_index": fn_index, "session_hash": session_hash})
                await websocket.send(data)


async def send31():
    await execute_web_socket([], 31)


async def send32():
    await execute_web_socket([True, 0], 32)


async def send33(prompt):
    data = [False, 1.5, 0.8, 0.3, 7, prompt.get('Sampler'), prompt.get('Scheduler'),
            False, -1, -1, -1,
            -1, -1, -1, False, False, False, False, 0.25, 64, 128, "joint", False, 1.01,
            1.02, 0.99, 0.95, False, False, "v2.6", 1, 0.618, False, False, 0]

    await execute_web_socket(data, 33)


async def send34(prompt):
    data = [prompt.get('Prompt'),
            prompt.get('Negative Prompt'),
            prompt.get('Styles'),
            prompt.get('Performance'),
            "1080×1080 <span style=\"color: grey;\"> ∣ 1:1</span>",
            1,
            prompt.get('Seed'),
            prompt.get('Sharpness'),
            prompt.get('Guidance Scale'),
            prompt.get('Base Model'),
            prompt.get('Refiner Model'),
            prompt.get('Refiner Switch'),
            "None",
            1,
            "None",
            1,
            "None",
            1,
            "None",
            1,
            "None",
            1,
            False,
            "uov",
            "Disabled",
            None,
            [],
            None,
            "",
            None,
            None,
            0.5,
            0.6,
            "ImagePrompt",
            None,
            0.5,
            0.6,
            "ImagePrompt",
            None, 0.5, 0.6, "ImagePrompt", None, 0.5, 0.6, "ImagePrompt"]

    await execute_web_socket(data, 34)
