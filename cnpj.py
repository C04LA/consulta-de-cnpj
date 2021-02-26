import requests
import json

def buscar_dados():
    request = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    dados = json.loads(request.content)
    print("Nome:")
    print(dados['nome'])
    print("Data de abertura:")
    print(dados['data_situacao'])
    print("Endereço:")
    print(dados['logradouro'])
    print(dados['numero'])
    print(dados['bairro'])
    print(dados['cep'])
    print(dados['uf'])
    print("Contatos:")
    print(dados['email'])
    print(dados['telefone'])
    print("Complementos:")
    print(dados['natureza_juridica'])
    print(dados['situacao'])



def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string

def exibir():
    print("codado por c0ala.py ")

cnpj = input("Digite o cnpj: ")


if __name__ == '__main__':
 buscar_dados()
 exibir()


