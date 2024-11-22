import random
import string
import boto3
import json

DEBUG = False # Enable debug to see all trace steps
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

AGENT_ID = 'URSVOGLFNX'
AGENT_ALIAS_ID = 'JHLX9ERCMD'

SESSION_ID_LENGTH = 10
SESSION_ID = "".join(
    random.choices(string.ascii_uppercase + string.digits, k=SESSION_ID_LENGTH)
)

# A unique identifier for each user
MEMORY_ID = 'danilop-92f79781-a3f3-4192-8de6-890b67c63d8b' 
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')


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