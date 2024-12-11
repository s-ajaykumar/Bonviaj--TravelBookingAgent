
import json
from datetime import date

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    def is_PastDate(year, month, day):
        if year == "None":
            year = date.today().year
        today_date = date.today()
        provided_date = date(year, month, day)
        if provided_date >= today_date:
            return "positive. Not a past date. YYYY/MM/DD: {}/{}/{}".format(year, month, day)
        else:
            return "negative. It's a past date. Ask the user to provide the correct date."

    date_dic = {param['name']:param['value'] for param in parameters}

    
    if date_dic['YYYY'] == "None":
        result = is_PastDate(date_dic['YYYY'], int(date_dic['MM']), int(date_dic['DD']))
    else:
        result = is_PastDate(int(date_dic['YYYY']), int(date_dic['MM']), int(date_dic['DD']))

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    responseBody =  {
        "TEXT": {
            "body": "{}".format(result)
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response
