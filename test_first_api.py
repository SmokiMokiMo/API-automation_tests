import requests

class TestFirst:
    def test_hello_world(self):
        url = "https://petstore.swagger.io/v2/pet/9223372036854646575"
        name = {"id": 0, "name": "plakhotnuyk"}
        date = {"name": "name"}
        response = requests.get(url)
        assert response.status_code == 200, "Wrong response code"
        response_dict = response.json()
        assert "category" in response_dict, "There is no field 'answer' in the response"
        expected_response_txt = name
        actual_response_txt = response_dict["category"]
        assert actual_response_txt == expected_response_txt, "Actual text in the response is not corent"
