## Project Objective

Fooocus Gallery is a project designed to simplify the process of navigating through images generated by Fooocus.

## Features

- **Image Navigation:** Quickly move through your images with a user-friendly interface
- **Fooocus Logs Based:** All the data and images are extracted directory from Fooocus Outputs directory
- **Prompt Search:** Filter generated images by prompts
- **Fast... Enough:** Fooocus Gallery was tested with 17k+ images, running smooth after the logs index
- **Re-Index:** changes on log.html are detected an re-indexed time to time
- **Docker Image:** coffeespice/fooocus_gallery

## How to run

If using docker set the path to Fooocus outputs in outputs_directory

If running without docker copy the config.json.example to config.json and change the outputs_directory to the Fooocus
outputs and then run pip install --no-cache-dir -r requirements.txt and python main.py

## Alternatives

- [Fooocus Gallery by mattmarkwick](https://github.com/mattmarkwick/fooocus-gallery)
- [Fooocus Log Viewer by toutjavascript](https://github.com/toutjavascript/Fooocus-Log-Viewer)