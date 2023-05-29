import requests

url = 'http://localhost:8000/api/v2'
# GET Avaliacoes

avaliacoes = requests.get(f'{url}/avaliacoes/')

# print(avaliacoes.status_code)
avaliacaoesJson = avaliacoes.json()
# Acessando os dados das resposta
# print(avaliacaoesJson)
# print(type(avaliacaoesJson))

# Acessando a quantidade de registros
# print(avaliacaoesJson['count'])

# Acessando a próxima página
# print(avaliacaoesJson['results'][0]['id'])


# GET cursos
headers = {'Authorization': 'Token d08f63f41b28e9ac0495571983024a01af8f5911'}
cursos = requests.get(url=f'{url}/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())
