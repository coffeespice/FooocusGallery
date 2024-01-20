import asyncio
import base64
import ast
import os.path
from urllib.parse import urlparse
from facades.FooocusServiceFacade import generate
from services.ConfigService import outputs_directory


def regenerate(prompt):
    prompt['Styles'] = ast.literal_eval(prompt.get('Styles'))
    asyncio.new_event_loop().run_until_complete(generate(prompt))


def vary_upscale(prompt, photo_path, action):
    photo_path = os.path.join(outputs_directory(), urlparse(photo_path).path)
    prompt['Styles'] = ast.literal_eval(prompt.get('Styles'))

    with open(photo_path, 'rb') as file:
        prompt["base64_image"] = base64.b64encode(file.read()).decode('utf-8')

    prompt["UpscaleVariant"] = action
    asyncio.new_event_loop().run_until_complete(generate(prompt))
