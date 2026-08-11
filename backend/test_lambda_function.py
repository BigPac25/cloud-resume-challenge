import json
import boto3
from moto import mock_aws

@mock_aws
def test_lambda_handler_increments_count():
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = dynamodb.create_table(
        TableName='cloud-resume-visitors',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': 'visitors', 'count': 5})

    import lambda_function

    result = lambda_function.lambda_handler({}, {})

    assert result['statusCode'] == 200
    
@mock_aws
def test_count_actually_increments():
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = dynamodb.create_table(
        TableName='cloud-resume-visitors',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    table.put_item(Item={'id': 'visitors', 'count': 5})

    import lambda_function
    result = lambda_function.lambda_handler({}, {})

    body = json.loads(result['body'])

    assert body['count'] == 6

@mock_aws
def test_handles_empty_table_gracefully():
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    table = dynamodb.create_table(
        TableName='cloud-resume-visitors',
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )

    import lambda_function
    result = lambda_function.lambda_handler({}, {})

    assert result['statusCode'] == 200