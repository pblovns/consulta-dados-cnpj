import requests
import json

def fazer_consulta(input):
    retorno = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{input}")
    base = retorno.json()

    dict_retorno = {
        "cnpj": base.get('cnpj'),
        "uf": base.get('uf'),
        "razao_social": base.get('razao_social'),
        "nome_fatatasia": base.get('nome_fantasia'),
        "municipio": base.get('municipio'),
        "logradouro": base.get('logradouro'),
        "natureza_juridica": base.get('natureza_juridica'),
        "situacao_especial": base.get('situacao_especial'),
        "atividade_fiscal": base.get('cnae_fiscal_descricao'),
        "situacao_cadastral": base.get('descricao_situacao_cadastral'),
        "identificador_filial_matriz": base.get('descricao_identificador_matriz_filial')
    }
    
    return dict_retorno