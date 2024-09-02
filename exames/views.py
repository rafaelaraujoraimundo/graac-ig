import pandas as pd
import os
from django.conf import settings
from django.shortcuts import render
from .api_requests import get_authorization_code, get_access_token, get_product_details

def view_padrao(request):
    activegroup = 'Exame'
    title = 'Orientações de Exames - Fleury'
    activemenu = 'orientacoes_exames_fleury'
    product_details = None

    # Caminho para o arquivo Excel
    excel_path = os.path.join(settings.BASE_DIR, 'exames', 'exames.xlsx')

    # Carregar os dados do Excel
    df = pd.read_excel(excel_path)

    # Exibir os primeiros registros para depuração
    print(df.head())

    # Verificar os nomes das colunas
    print(df.columns)

    # Converter o DataFrame para uma lista de dicionários
    exames_list = df.to_dict('records')

    if request.method == 'POST':
        product_code = request.POST.get('fruitCode')

        # Chamar as funções para obter os detalhes do produto
        authorization_code = get_authorization_code()
        access_token = get_access_token(authorization_code)
        product_details = get_product_details(product_code, access_token)

    context = {
        'activegroup': activegroup,
        'title': title,
        'activemenu': activemenu,
        'product_details': product_details,
        'exames_list': exames_list,  # Passar a lista de exames para o template
    }

    return render(request, 'exames/orientacoes_exames.html', context)
