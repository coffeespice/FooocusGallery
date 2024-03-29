## Project Objective

Fooocus Gallery is a project designed to simplify the process of navigating through images generated by Fooocus.

## Features

- **Image Navigation:** Quickly move through your images with a user-friendly interface
- **Fooocus Logs Based:** All the data and images are extracted directory from Fooocus Outputs directory
- **Prompt Search:** Filter generated images by prompts
- **Fast... Enough:** Fooocus Gallery was tested with 17k+ images, running smooth after logs index
- **Re-Index:** changes on log.html are detected and re-indexed time to time
- **Vary/Upscale/Regenerate:** Re-generate your image with a single click
- **Docker Image:** coffeespice/fooocus_gallery

![Fooocus Gallery Search](/static/fooocusMain.png)
![Fooocus Gallery Actions](/static/fooocusImageExplained.png)

## How to run

If using docker set the path to Fooocus outputs in outputs_directory

If running without docker copy the config.json.example to config.json and change the outputs_directory to the Fooocus
outputs and then run ``pip install --no-cache-dir -r requirements.txt`` and ``python main.py``

## config.json example

```
{
    "outputs_directory": "\\path\\to\\fooocus\\outputs",
    "fooocus_ip": "127.0.0.1:7865"
}
```

## doocker-compose.yml example

```
version: "3"

services:
    fooocus_gallery:
        image: coffeespice/fooocus_gallery:latest
        ports:
            - "8080:8080"
        environment:
            - outputs_directory=
            - fooocus_ip=127.0.0.1:7865
```

## Alternatives

- [Fooocus Gallery by mattmarkwick](https://github.com/mattmarkwick/fooocus-gallery)
- [Fooocus Log Viewer by toutjavascript](https://github.com/toutjavascript/Fooocus-Log-Viewer)