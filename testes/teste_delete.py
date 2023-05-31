import requests

url = 'http://localhost:8000/api/v2'

headers = {'Authorization': 'Token 51e9390d377759ccf9c949563b6fe7b00be29618'}


url_cursos = f'{url}/cursos'


resultado = requests.delete(url=f'{url_cursos}/12/', headers=headers)
# print(resultado.json())

# TESTANDO se o retorno é de deleção
assert resultado.status_code == 204

# TESTANDO se o objetivo foi realmente excluído
assert len(resultado.text) == 0


