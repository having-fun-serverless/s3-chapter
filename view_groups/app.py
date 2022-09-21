import boto3
from boto3.dynamodb.conditions import Key
import json
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["GROUPS_SUBSCRIBERS_TABLE_NAME"])

def lambda_handler(event, context):
    response = table.query(KeyConditionExpression=(Key('PK').eq("GROUP") & Key('SK').begins_with("GROUP#METADATA")))
    
    groups = [{"id": group["SK"].split("#")[2], "name":group["name"], "description":group["description"]} for group in response["Items"]]
    
    return {
        "statusCode": 200,
        "body": json.dumps(groups)
    }
    
