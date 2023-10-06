#!/usr/bin/env python

########################################################
#### Script para consulta CNPJ via API do SERPRO    ####
#### Linguagem: Python 3.11.5                       ####
#### Criado em 06/10/2023                           ####
#### Versao: R00                                    ####
#### Copyright (c) 2023 by Alan Lopes               ####
########################################################
# 06/10/2023 - VERSAO INICIAL                          #
########################################################

# Declacao de bibliotecas
import requests

# Token Inicial
var_default_token = '06aef429-a981-3ec5-a1f8-71d38d86481e'

# Declaracao de variaveis
var_host = 'https://gateway.apiserpro.serpro.gov.br/consulta-cnpj-df-trial/v2'
var_header_content_type = {'Content-Type': 'application/json'}
var_header_basic = {'Authorization': 'Bearer '+ var_default_token}

# Criacao do headers inicial
var_headers = {}
var_headers.update(var_header_content_type)
var_headers.update(var_header_basic)

var_cnpj = '34238864000168'

def func_status():
    var_url = var_host + '/status'

    var_response = requests.get(
        var_url,
        headers=var_headers
    )
    return var_response.status_code

def func_get():
    var_url = var_host + '/basica/' + var_cnpj

    var_response = requests.get(
        var_url,
        headers=var_headers
    )
    return var_response
    

print(func_status())
print(func_get().json())
