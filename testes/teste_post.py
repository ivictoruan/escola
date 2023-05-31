import requests

url = 'http://localhost:8000/api/v2'

headers = {'Authorization': 'Token 51e9390d377759ccf9c949563b6fe7b00be29618'}


url_cursos = f'{url}/cursos/'
url_avaliacoes = f'{url}/avaliacoes/'

novo_curso =  {
    "titulo":"Gerenciaa Ágil de Projetos com Scrum",
    "url":"http://www.ivictoruan.dev.br/gerenciaa-agil-projetos-scrum"
}


# POST curso
resultado = requests.post(url=f'{url}/cursos/', headers=headers, data=novo_curso)

# Testando se o curso foi criado (código de status 201)
assert resultado.status_code == 201 

# Testando se o título do curso criado/retornado é o mvesmo do curso informado
# print(f'retorno: {resultado.json()}')
assert resultado.json()['titulo'] == novo_curso['titulo']




