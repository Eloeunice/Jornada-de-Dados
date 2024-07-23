import requests

import requests
import csv

# Configurações da API do ClickUp
api_token = 'seu_token_de_api_do_ClickUp'
base_url = 'https://api.clickup.com/api/v2'

# ID da lista que você deseja exportar
list_id = 'id_da_sua_lista_no_ClickUp'

# Endpoint para obter as tarefas da lista
endpoint = f'{base_url}/list/{list_id}/task'

# Cabeçalhos necessários para a API do ClickUp
headers = {
    'Authorization': api_token
}

# Faz a requisição GET para obter as tarefas da lista
response = requests.get(endpoint, headers=headers)

if response.status_code == 200:
    tasks_data = response.json()['tasks']

    # Nome do arquivo CSV onde os dados serão salvos
    csv_filename = 'tarefas_clickup.csv'

    # Abre o arquivo CSV em modo de escrita
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Define os campos do cabeçalho do CSV
        fieldnames = ['Título', 'Descrição', 'Status', 'Responsável']

        # Inicializa o escritor CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escreve o cabeçalho no arquivo CSV
        writer.writeheader()

        # Itera sobre as tarefas e escreve cada uma no arquivo CSV
        for task in tasks_data:
            title = task['name']
            description = task['description'] if 'description' in task else ''
            status = task['status']['status']
            assignee = task['assignees'][0]['username'] if task['assignees'] else ''

            # Escreve a linha no arquivo CSV
            writer.writerow({'Título': title, 'Descrição': description, 'Status': status, 'Responsável': assignee})

    print(f'Dados exportados para {csv_filename}')
else:
    print(f'Erro ao acessar API do ClickUp. Código de status: {response.status_code}')

