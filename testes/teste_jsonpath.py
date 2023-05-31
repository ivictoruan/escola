import requests
import jsonpath

url = 'http://localhost:8000/api/v2'


avaliacoes = requests.get(f'{url}/avaliacoes/')
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultados)

# GET nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

# print(nomes)

# GET avaliacoes (notas)
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(notas)