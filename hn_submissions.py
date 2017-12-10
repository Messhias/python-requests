import requests

from operator import itemgetter

# call the api
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print( "Status code", r.status_code )

# process the information
submissions_id = r.json()
submissions_dicts = []
for submissions_id in submissions_id[:30]:
    # create a separeted api call for each article
    url = ( "https://hacker-news.firebaseio.com/v0/item/" + 
        str(submissions_id) + '.json'
    )
    submissions_r = requests.get( url )
    # print( submissions_r.status_code )
    response_dict = submissions_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'https://news.ycombinator.com/item?id=' + str( submissions_id ),
        'comments': response_dict.get( 'descendants', 0 )
    }
    submissions_dicts.append( submission_dict )

submissions_dicts = sorted( submissions_dicts, key=itemgetter( 'comments' ), reverse=True )

for submission_dict in submissions_dicts:
    print( "\nTitle", submission_dict['title'] )
    print( "\nDiscussion link:", submission_dict['link'] )
    print("\nComments:", submission_dict['comments'])