import requests

def get_data(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    return response
    
   
def get_events(response):
    events = response.json()
    
    for event in events:
        type = event['type']
        if (type == 'WatchEvent'):
            print(f'- Starred {event['repo']['name']} at {event['created_at']}.')
            
        elif (type == 'PushEvent'):
            print(f'- Pushed {event['payload']['size']} commit(s) to {event['repo']['name']} at {event['created_at']}.')
            
        elif (type == 'PullRequestEvent'):
            print(f'- Created pull request "{event['payload']['pull_request']['title']}" on {event['repo']['name']} at {event['created_at']}.')
            
        elif (type == 'PullRequestReviewEvent'):
            print(f'- Made review: "{event['payload']['review']['body']}"  on pull request: "{event['payload']['pull_request']['title']}" at {event['created_at']}.')
        