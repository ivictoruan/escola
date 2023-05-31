import requests

url = 'http://localhost:8000/api/v2'

headers = {'Authorization': 'Token 51e9390d377759ccf9c949563b6fe7b00be29618'}


# url_cursos = f'{url}/cursos/'
url_avaliacoes = f'{url}/avaliacoes/'

curso_atualizado =  {
    "titulo":"Gerencia Ágil de Projetos com Scrum 2",
    "url":"http://www.ivictoruan.dev.br/gerencia-agil-projetos-scrum-2"
}


# POST curso
resultado = requests.put(url=f'{url}/cursos/15/', headers=headers, data=curso_atualizado)

# print(resultado.json())

# Testando se o curso com id 15 existe:
assert requests.get(url=f'{url}/cursos/15/', headers=headers).status_code == 200


# Testando se o código retornado é de sucesso (HTTP 200):
assert resultado.status_code == 200

# Testando se a alteração foi realizada
assert resultado.json()['titulo']  == curso_atualizado['titulo'] 
