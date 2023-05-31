import requests

url = 'http://localhost:8000/api/v2'


# GET cursos
headers = {'Authorization': 'Token d08f63f41b28e9ac0495571983024a01af8f5911'}
resultado = requests.get(url=f'{url}/cursos/', headers=headers)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# print(resultado.json())
# # Testando se a quantidade de paginação é 2
assert len(resultado.json()['results']) == 2