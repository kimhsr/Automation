import requests

headers = {'Authorization': 'Bearer 본인_토큰'}  # "Bearer" 라는 글자는 지우시면 안됩니다! "
data = {"message": "테스트!"}
requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
