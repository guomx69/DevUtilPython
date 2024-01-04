# a function to create a dynamic table  
def create_table(dynamodb, table_name, attribute_definitions):
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        return table
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Table {table_name} created successfully.")
        return table
    return None