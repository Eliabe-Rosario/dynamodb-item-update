# dynamodb-item-update
# Função Lambda: UpdateDynamoDBItem
## Descrição

Esta função Lambda atualiza um item em uma tabela do DynamoDB.

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
Dependencias: boto3
