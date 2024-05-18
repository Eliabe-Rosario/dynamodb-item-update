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
  
## Instruções para execução

- Acesse o console do AWS Lambda.
- Crie uma nova função Lambda.
- No editor de código cole o .py fornecido acima.
- Configure a função para ter permissões adequadas para acessar o DynamoDB.
- Defina as variáveis de ambiente necessárias (por exemplo o nome da tabela DynamoDB).

## Configurando o evento de teste e Executando o teste

- No console do AWS Lambda, entre na guia "Testar".
- Crie um novo evento com o formato descrito ao final do texto.
- Salve  o teste e clique em "Testar".
- Verifque se os reseultados no console estão de acordo/se o item foi atulizado corretamente no DynamoDB.
## Depuração

- Acesse o console do Amazon CloudWatch.
- Navegue até "Logs".
- Encontre o grupo de logs que corresponde à sua função Lambda.
- Examine os logs para entender o comportamento da função e identificar erros.
  ## Estrutura do Evento de Entrada e que sera usado na configuração do evento de teste ( Na guia "Testar" do console do AWS Lambda)

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
