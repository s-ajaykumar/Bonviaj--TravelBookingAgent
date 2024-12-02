import string
import boto3
import random
import json
import config

DEBUG = False # Enable debug to see all trace steps

SESSION_ID_LENGTH = 10
'''SESSION_ID = "".join(
    random.choices(string.ascii_uppercase + string.digits, k=SESSION_ID_LENGTH)
)'''
SESSION_ID = 'session_id'
MEMORY_ID = 'memory_id' 

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1', aws_access_key_id=config.ACCESS_KEY,
    aws_secret_access_key=config.SECRET_KEY)

#Test agents
AGENT_ID = 'LQER1UC724'
AGENT_ALIAS_ID = 'D42RECL3Z1'

def invoke_agent(prompt, end_session=False):
    response = bedrock_agent_runtime.invoke_agent(
        agentId=AGENT_ID,
        agentAliasId=AGENT_ALIAS_ID,
        sessionId=SESSION_ID,
        inputText=prompt,
        memoryId=MEMORY_ID,
        enableTrace=DEBUG,
        endSession=end_session,
    )

    completion = ""

    for event in response.get('completion'):
        if DEBUG:
            print(event)
        if 'chunk' in event:
            chunk = event['chunk']
            completion += chunk['bytes'].decode()

    return completion

prompt = "book a flight from essex to singapore"
output = invoke_agent(prompt, end_session=False)
print(output)
print(SESSION_ID)