import requests

# uri = "://172.24.113.199:7890"
uri = "s://argus-api.hsrn.nyu.edu"
r = requests.post(url=f'http{uri}/token',
                  data={'username': 'test', 'password': 'test'})
print(r)
# token = r.json()['access_token']
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzb25pYSIsImV4cCI6MTY2NDA1NTg1N30.LyyYwW1zxZnLAW0RfLlNyxpY1UPLwM7ao"
header = {"Authorization": "Bearer "+token}


r = requests.post("http" + uri + "/data/test",
                  files={'entries': 'dump'}, headers=header)


print(r)