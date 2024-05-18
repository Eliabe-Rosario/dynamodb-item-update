import json
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    nome_tabela = 'NomeDaSuaTabelaDynamoDB'
    tabela = dynamodb.Table(nome_tabela)
    
    
    chave_item = event['key']  
    expressao_atualizacao = event['update_expression']  
    valores_atributos_expressao = event['expression_attribute_values'] 
    
    try:
        
        resposta = tabela.update_item(
            Key=chave_item,
            UpdateExpression=expressao_atualizacao,
            ExpressionAttributeValues=valores_atributos_expressao,
            ReturnValues="UPDATED_NEW"
        )
    except Exception as e:
    
        return {
            'statusCode': 400,
            'body': json.dumps(f'Erro ao atualizar o item: {str(e)}')
        }
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Item atualizado com sucesso: {resposta}')
    }
