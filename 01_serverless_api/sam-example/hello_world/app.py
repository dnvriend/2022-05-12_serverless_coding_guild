import json

def lambda_handler(event, context):

    if event['resource'] == '/api':
        return {
            "statusCode": 200,
            'body': 'hello world!'
        }
    elif event['resource'] == '/api/hello/{name}':
        name = event['pathParameters']['name']
        return {
            "statusCode": 200,
            'body': f'hello {name}'
        }
    elif event['resource'] == '/api/users':
        body = event['body']
        return {
            "statusCode": 200,
            'body': body
        }
    else:
        return {
            "statusCode": 200,
            'body': json.dumps(event)
        }
