import boto3
import json
import config
import os
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

#DynamoDB 
#Update items in a table
'''
dynamodb = boto3.resource('dynamodb', region_name = "us-east-1",  aws_access_key_id=config.ACCESS_KEY,
    aws_secret_access_key=config.SECRET_KEY)

table = dynamodb.Table('flight_chat_history')
try:
    chat_history = "User: MAdurai to cehnnai\n\nAssistant: Provide the departure date"
    response = table.update_item(
        Key = {'key' : key},
        UpdateExpression = "set chat_history = list_append(chat_history, :a), summarized_chat_history = :b",
        ExpressionAttributeValues = {
            ':a' : [current_conversation],
            ':b' : current_conversation
        },
        ReturnValues = "UPDATED_NEW" 
    )
    print(response['Attributes'])
except ClientError as e:
    print(e)
'''

#Put items in a table
'''
table.put_item(
Item = {
    'key' : key,
    'chat_history' : [],
    'summarized_chat_history' : ""
}
)'''

#Get items in a table
'''try:
    summarized_chat_history = table.get_item(Key = {'key' : key})
    print(summarized_chat_history['Item']['summarized_chat_history'])
except ClientError as e:
    print(f"Error in fetching summarized chat history: {e}")'''

#List the items
'''try:
    is_key_exists = table.query(KeyConditionExpression = Key("key").eq(key))
    if is_key_exists["Items"] == []:
        table.put_item(Item = {
            'key' : key,
            'chat_history' : "",
            'summarized_chat_history' : ""
            })
    else:
        retrieve_chat_history(key)
        
except ClientError as e:
    print(e)'''
    

#Lambda functions
#Invoke a lambda function
'''
lambda_client = boto3.client('lambda', region_name = 'us-east-1', aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY)


params = {
        'chat_history' : 'chat_history'
    }
try:
    response = lambda_client.invoke(
        FunctionName = "test",
        Payload = json.dumps(params),
        LogType = 'Tail'
    )
    print(json.load(response['Payload']))
except ClientError as e:
    raise e
'''

#Invoke a prompt in prompt management
'''
prompt_client = boto3.client('bedrock-runtime', region_name='us-east-1', aws_access_key_id=config.ACCESS_KEY,
    aws_secret_access_key=config.SECRET_KEY)
def invoke_prompt(chat_history):
        prompt_arn = "arn:aws:bedrock:us-east-1:851725391855:prompt/629TKUXHLV:2"
        response = prompt_client.converse(
            modelId = prompt_arn,
            promptVariables = {
                'topic' : {'text' : chat_history}
            })
        output = response['output']['message']['content'][0]['text']
        print(output)
        return output
invoke_prompt('User: madurai to chennai\nAssistant: Please provude the departure date')
'''

#Using requests to invoke a prompt in prompt management      [Still connection timeout error persists]
'''
os.environ['AWS_ACCESS_KEY_ID'] = config.ACCESS_KEY
os.environ['AWS_SECRET_ACCESS_KEY'] = config.SECRET_KEY
current_datetime = datetime.now(timezone.utc)
iso_datetime = current_datetime.isoformat()
endpoint = "http://bedrock-runtime.us-east-1.amazonaws.com/model/arn:aws:bedrock:us-east-1:851725391855:prompt/629TKUXHLV/converse"
payload = {
    'promptVariables' : {'text' : 'hi'}
}
headers = {
    'Content-type' : 'application/json'
}
try:
    response = requests.post(endpoint, json = payload, headers = headers)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"error: {str(e)}")
    '''

#Invoke a model
'''
prompt = "how are you"
body = {
    'anthropic_version' : 'bedrock-2023-05-31',
    'max_tokens' : 512,
    'temperature' : 1.0,
    'messages' : [{
        'role' : 'user',
        'content' : [{'type' : 'text', 'text' : prompt}]
    }]
}

model_id = "anthropic.claude-3-haiku-20240307-v1:0"
response = client.invoke_model(modelId = model_id, body = json.dumps(body) )
content = json.loads(response['body'].read())
print(content["content"][0]['text'])

'''
