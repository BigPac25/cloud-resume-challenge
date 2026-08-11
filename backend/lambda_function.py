# test again
import json
import boto3

db = boto3.resource('dynamodb')
table = db.Table('cloud-resume-visitors')

def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'id': 'visitors'
        }
    )

    if "Item" in response:
        visitor_count = response["Item"]["count"]
    else:
        visitor_count = 0

    visitor_count += 1

    table.put_item(
        Item={
            'id': 'visitors',
            'count': visitor_count
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({"count": int(visitor_count)})
    }
