import requests

class TestCursos: # CLASSE TEST SUITE
    url = 'http://127.0.0.1:8000/api/v2/cursos'
    headers = {'Authorization': 'Token 51e9390d377759ccf9c949563b6fe7b00be29618'}

    # curso_id = 10

    def test_post_curso(self):
        novo_curso =  {
            "titulo":"Flutter Embbeding ",
            "url":"http://www.ivictoruan.dev.br/flutter-embbeding-8/"
        }

        # POST curso
        resposta = requests.post(url=f'{self.url}/', headers=self.headers, data=novo_curso)

        # Testando se o curso foi criado (código de status 201)
        assert resposta.status_code == 201 

        # Testando se o título do curso criado/retornado é o mvesmo do curso informado
        assert resposta.json()['titulo'] == novo_curso['titulo']


    def test_put_curso(self):    
        curso_atualizado =  {
        "titulo":"Gerencia Ágil de Projetos com Scrum 4",
        "url":"http://www.ivictoruan.dev.br/gerencia-agil-projetos-scrum-4/"
        }

        # POST curso
        resposta = requests.put(url=f'{self.url}/9/', headers=self.headers, data=curso_atualizado)
        
        # Testando se o curso com id 10 existe:
        assert requests.get(url=f'{self.url}/9/', headers=self.headers).status_code == 200

        # Testando se o código retornado é de sucesso (HTTP 200):
        assert resposta.status_code == 200


    def test_put_titulo_curso(self):
        curso_atualizado = {
            "titulo": "Testando alteração-3",
            "url":"https://ivictoruan.dev.br/testando-alteração-3/"
        }

        resposta = requests.put(url=f'{self.url}/9/', headers=self.headers, data=curso_atualizado) 
        # print(resposta.json())
        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url}/9/', headers=self.headers)

        assert resposta.status_code == 200


    def test_get_cursos(self):
        resposta = requests.get(url=self.url, headers=self.headers)

        assert resposta.status_code == 200

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url}/9/', headers=self.headers)
        # print(resposta.json())

        # TESTANDO se o retorno é de deleção
        assert resposta.status_code == 204 and len(resposta.text) == 0

        # TESTANDO se o objetivo foi realmente excluído
        assert len(resposta.text) == 0

