# System Software

The Colorboard system software.

## Upload new firmware

To upload new firmware you need to send a post request to the server by following address:

```
POST http://127.0.0.1:5000/api/v1/firmware/upload
```

and it needs to contain the content you uploading at the data section in the json format like that:

```json
{
    "content": "print('Hello, world')\nprint('Welcome!')"
}
```

hahah

## Get current firmware log

To get current firmware log send a get request to the server by following address:

```
GET http://127.0.0.1:5000/api/v1/firmware/log
```

it will return json with list of lines:

```json
{
    "status": true,
    "log": [
        "Hello, world",
        "Welcome"
    ]
}
```