import json

print('Loading function')

def lambda_handler(event, context):
    print('Received event: ' +
        json.dumps(event, indent=2))
    
    if 'greet' in event:
        greeting = event['greet']
    else:
        greeting = 'Hello'
        
    if 'name' in event:
        name = event['name']
    else:
        name = 'World'        
        
    greetings = greeting + ' ' +  name + '!'
    print(greetings)
    return greetings
