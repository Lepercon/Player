import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    username = event['queryStringParameters']['username']
    password = event['queryStringParameters']['password']
    print(f"username is {username}")
    if authenticate(username, password):
        s3 = boto3.client('s3')
        url = create_presigned_url(s3, 'DeathInParadise/Season12/blah.drawio')
        print(f"url is {url}")
        return {
            'statusCode': 200,
            'body': json.dumps(url)
        }
    
def authenticate(username, password):
    allowed_users = ['jmmem', 'kdpb', 'aeb', 'oeb']
    # TODO turn the above into a dict with usernames & pwords
    return True

def create_presigned_url(client, object_name):
    url = client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': 'silberwolk-videos-en-uk',
            'Key': object_name
        },
        ExpiresIn=3600
    )
    return url