import requests

class TestPostApi:
    def post_tu_pet_store(self):
        url = "https://petstore.swagger.io/v2/pet"
        data = {
    "id": 0,
    "category": {
    "id": 0,
    "name": "plakhotnuyk"
    },
    "name": "anna_puppy",
    "photoUrls": [
    "https://images.pexels.com/photos/58997/pexels-photo-58997.jpeg?cs=srgb&dl=pexels-muhannad-alatawi-58997.jpg&fm=jpg"
    ],
    "tags": [
    {
      "id": 0,
      "name": "ihor"
    }
    ],
    "status": "available"
    }

    resource = requests.post(url, data=data)
