# text-detection-restapi
### Microservise that uses Flask as a backend for detecting text using tesseract. App contains docker image to be built and run on your machine. 
### App is running on the localhost port 8000, http://localhost:8000/ocr with POST method for sending images.
## Prerequisities
### I assume you have installed Docker and it is running. See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instrucitons.
## Build
1. Clone this repo
    ``` git clone https://github.com/mradzikowski/text-detection-restapi.git ```
2. Build the docker image
    ``` docker-compose build ```
3. Fire up the container in detached mode
    ``` docker-compose up -d ```
4. If you make any change, update the container using command
    ``` docker-compose up -d --build ```
5. To see docker-compose logs use:
    ``` docker-compose logs ```
## Testing
``` docker-compose exec api python -m pytest "src/tests" ```
## To check code quality using linters
### Flake8
``` docker-compose exec api flake8 src ```
### Black
``` docker-compose exec api black src ```
### Isort
``` docker-compose exec api isort src ```

## Reqeust using curl
``` curl -X POST http://localhost:8000/ocr -F "file=@{your_file_name.jpg}" ```
## Example response on POST request
```
[
    {
        "left": 71,
        "top": 67,
        "right": 155,
        "bottom": 78,
        "text": "GALARETKA"
    },
    {
        "left": 79,
        "top": 137,
        "right": 147,
        "bottom": 151,
        "text": "cytrynowa"
    },
    {
        "left": 240,
        "top": 74,
        "right": 279,
        "bottom": 86,
        "text": "mleko"
    },
    {
        "left": 363,
        "top": 148,
        "right": 407,
        "bottom": 163,
        "text": "woda"
    }
]
 ```


