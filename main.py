from decouple import config
import requests
import pandas as pd
from datetime import datetime

# we use this function to convert responses to dataframes
def df_from_response(res):
    # initialize temp dataframe for batch of data in response
    df = pd.DataFrame()

    # loop through each post pulled from res and append to df
    for post in res.json()['data']['children']:
        df = df.append({
            # 'subreddit': post['data']['subreddit'],
            # 'upvote_ratio': post['data']['upvote_ratio'],
            # 'ups': post['data']['ups'],
            # 'downs': post['data']['downs'],
            # 'created_utc': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'score': post['data']['score'],
            'id': post['data']['id'],
            'kind': post['kind']
        }, ignore_index=True)

    return df

REDDIT_USERNAME = config('REDDIT_USERNAME')

print("hello")
print(REDDIT_USERNAME)
# # authenticate API
# client_auth = requests.auth.HTTPBasicAuth(constant.CLIENT_ID, constant.SECRET_TOKEN)

# data = {
#     'grant_type': 'password',
#     'username': constant.USERNAME,
#     'password': constant.PASSWORD
# }
# headers = {'User-Agent': constant.USER_AGENT}

# # send authentication request for OAuth token
# res = requests.post('https://www.reddit.com/api/v1/access_token',
#                     auth=client_auth, data=data, headers=headers)
# # extract token from response and format correctly
# token = res.json()['access_token']

# # update API headers with authorization (bearer token)
# headers = {**headers, **{'Authorization': f"bearer {token}"}}





# # initialize dataframe and parameters for pulling data in loop
# data_frame = pd.DataFrame()
# params = {'limit': 100}

# # loop through 10 times (returning 1K posts)
# for i in range(3):
#     # make request
#     res = requests.get("https://oauth.reddit.com/r/wallstreetbets/new",
#                     headers=headers,
#                     params=params)

#     # get dataframe from response
#     new_df = df_from_response(res)
#     # take the final row (oldest entry)
#     row = new_df.iloc[len(new_df)-1]
#     # create fullname
#     fullname = row['kind'] + '_' + row['id']
#     # add/update fullname in params
#     params['after'] = fullname
    
#     # append new_df to data
#     data_frame = data_frame.append(new_df, ignore_index=True)
    
# print(data_frame)