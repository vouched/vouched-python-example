from vouched import config
import requests
from vouched.client import request_api
import base64

def base64_image(file):
  return base64.encodestring(open(file,"rb").read())

def test_jobs():
  result = request_api('/jobs?id=w32334', 'GET' )
  assert result.get('items') == []

def test_submit_job():
  selfie = base64_image('./data/large.jpg')
  id = base64_image('./data/small.jpg')
  data = {
    "type": "id-verification",
    "params": {
      "userPhoto": selfie,
      "idPhoto": id
    }
  }
  result = request_api('/jobs', 'POST', data)
  assert len(result.get('errors')) > 0 

def test_crosscheck():
  r = request_api('/identity/crosscheck', 'POST', data= {
      "firstName": "John",
      "lastName": "Bao",
      "email": "baoman@mail.com",
      "phone": "917-343-3433",
      "ipAddress": "73.19.102.110",
      "address": {
        "streetAddress": "1 Main St",
        "city": "Seattle",
        "postalCode": "98031",
        "state": "WA",
        "country": "US"
      }
    })

  assert r.get('id') != None
  assert r.get('result').get('confidences').get('identity') < 0.39

def test_all_invites():
  r = request_api('/invites?pageSize=3&id=mKAUux8h_', 'GET')
  assert r.get('items') == []

def test_delete_job():
  r = request_api('/jobs/23432', 'DELETE')
  assert len( r.get('errors') ) > 0

def test_submit_invite():
  r = request_api('/invites', 'POST', data={
    "email":"darwin66@lkxloans.com",
    "firstName": 'John',
    "lastName": 'Bao',
    "phone": '0000000000',
    "contact": 'phone'
  })
  assert len( r.get('errors') ) > 0

    
