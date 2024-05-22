from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import json
import random

app = FastAPI()

def generate_random_data(num_points):
    # Generate random data points for a line chart
    data = []
    for i in range(num_points):
        x = i  # X value can be index or timestamp depending on your requirement
        y = random.uniform(0, 100)  # Random Y value between 0 and 100
        data.append({"x": x, "y": y})
    
    return data

async def send_data(websocket: WebSocket):
    while True:
        # Generate random data with 10 points
        data = generate_random_data(10)
        # Convert data to JSON format
        data_json = json.dumps(data)
        # Send JSON data over WebSocket
        await websocket.send_text(data_json)
        await asyncio.sleep(1)  # Send data every second



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await send_data(websocket)

async def send_data_for_ws2(websocket: WebSocket):
    while True:
        # Generate random data points for a wake pattern
        data = []
        for i in range(100):
            # Generate x and y coordinates with a wake-like pattern
            x = i
            y = random.uniform(0, 100) + 20 * (1 - abs(i - 50) / 50)  # Wake pattern formula
            data.append({"x": x, "y": y})

        # Convert data to JSON format
        data_json = json.dumps(data)

        # Send JSON data over WebSocket
        await websocket.send_text(data_json)
        await asyncio.sleep(1)  # Send data every second
@app.websocket("/ws2")
async def websocket_endpoint2(websocket: WebSocket):
    await websocket.accept()
    await send_data_for_ws2(websocket)
