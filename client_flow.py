import string
import boto3
import random
import json
import config


client = boto3.client('bedrock-agent-runtime', region_name='us-east-1', aws_access_key_id=config.ACCESS_KEY,
    aws_secret_access_key=config.SECRET_KEY)


#Test prompt flow
'''def invoke_flow():
    response = client.invoke_flow(
    enableTrace=False,
    flowAliasIdentifier='HJ81IO4W2A',
    flowIdentifier= 'LQER1UC724',
    inputs=[
            {
            'content': {
                'document': {'text' : "madurai to chennai", 'key': "chat001"}
            },
            'nodeName': 'FlowInputNode',
            'nodeOutputName': 'document'
            },
        ],
    )

    for event in response.get('responseStream'):
        output = event
        break
    print(output.get('flowOutputEvent').get('content').get('document'))
output = invoke_flow()'''


def invoke_flow():
    response = client.invoke_flow(
        flowAliasIdentifier='QW7EWJHOT4',
        flowIdentifier= 'HAK58N229X',
        inputs=[
                {
                'content': {
                    'document': {'key' : 'key', 'gotIATA' : 'gotIATA', 'IATACodes': 'IATACodes',
                     'bookingDetails' : 'bookingDetails', 'query' : 'query'}
                },
                'nodeName': 'FlowInputNode',
                'nodeOutputName': 'document'
                },
            ],
        )

    for event in response.get('responseStream'):
        output = event
        break
    print(output.get('flowOutputEvent').get('content').get('document'))
output = invoke_flow()

