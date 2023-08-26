import requests
import json

def tratar_cnpj(cnpj):
    if cnpj == 'a':
        print("CNPJ INVÁLIDO")
    if cnpj == '1':
        print("CNPJ INVÁLIDO")
    if cnpj == '2':
        print("CNPJ INVÁLIDO")
    if cnpj == '9':
        print("CNPJ INVÁLIDO")
    else:
        validar_cnpj(cnpj)

def validar_cnpj(cnpj):
    request = requests.get(f'https://api.nfse.io/validate/LegalEntities/taxNumber/{cnpj}')
    validador = json.loads(request.content)
    if not validador['valid']:
        print("CNPJ INCORRETO")
    else:
        buscar_dados(cnpj)

def buscar_dados(cnpj):
    request = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
    dados = json.loads(request.content)
    print("=============================")
    print("Nome:", dados['nome'])
    print("Data de abertura:", dados['data_situacao'])
    print("Endereço:", dados['logradouro'], dados['numero'])
    print(dados['bairro'])
    print(dados['cep'], dados['uf'])
    print("Contatos:", dados['email'], dados['telefone'])
    print("Complementos:", dados['natureza_juridica'])
    print("Situação:", dados['situacao'])

def exibir():
    print("codado por c0ala.py")

def main():
    cnpj = input("Digite o CNPJ: ")
    tratar_cnpj(cnpj)
    exibir()

if __name__ == '__main__':
    main()
