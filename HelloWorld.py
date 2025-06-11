import json

def lambda_handler(event, context):
    # Log the event (optional)
    print("Received event:", json.dumps(event))

    # Create a response
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'Hello from AWS Lambda!',
            'input': event
        })
    }

    return response