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
**##** **Instruções para execução **
- Acesse o console do AWS Lambda.
- Crie uma nova função Lambda.
- No editor de código cole o .py fornecido acima.
- Configure a função para ter permissões adequadas para acessar o DynamoDB.
- Defina as variáveis de ambiente necessárias(por exemplo o nome da tabela DynamoDB).

**##** **Configurando o evento de teste e Exeutando o teste**
- No console do AWS Lambda, entre na guia "Testar"
- Crie um novo evento com o seguinte formato:
        {
  "key": {
    "PrimaryKeyAttribute": "valor"
  },
  "update_expression": "SET attribute = :val",
  "expression_attribute_values": {
    ":val": "novo_valor"
  }
}
- Salve o teste e clique em "Testar".
- Verifique os reseultados no console para garantir que  o item no DynamoDB foi atualizado corretamente.
**##** **Depuração**
- Acesse o console do Amazon CloudWatch.
- Navegue até "Logs".
- Encontre o grupo de logs que corresponde à sua função Lambda.
- Examene os logs para entender o comportamento da função e identificar erros
