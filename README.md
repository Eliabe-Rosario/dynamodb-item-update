# dynamodb-item-update
# Função Lambda: UpdateDynamoDBItem
## Descrição

Esta função Lambda atualiza um item em uma tabela do DynamoDB.

## Funcionalidades

- Atualiza itens em uma tabela DynamoDB especificada.
- Recebe dados de entrada através de um evento para definir a chave do item e os valores a serem atualizados.

## Pré-requisitos

- Python 3.x
- Boto3
  
## Estrutura do Evento de Entrada

A função espera receber um evento no seguinte formato:

```json
{
  "key": {
    "PrimaryKeyName": "PrimaryKeyValue"
  },
  "update_expression": "SET #attrName = :val",
  "expression_attribute_values": {
    ":val": "NewValue",
    "#attrName": "AttributeName"
  }
}

