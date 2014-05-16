from models import Models,Base
import datetime

@Models.register


#user info
class User(Base):
   __collection__ ='user'

   structure = {

     'phone' : unicode

  }


"""
 User signeups are recorded here
 signedup_at: time of signedup
 signed_type: 1: wifi, 0: web
"""
@Models.register
class UserSignup(Base):
  
   __collection__ ='user_signup'
#   __database__ ='btdog'
   structure = {
     'user_phone': unicode,
     'signedup_at': datetime.datetime,
     'signedup_type' : int
   }


"""
user sharing profile
signed_days are updated through signed up, shared_times through access from shared pages, and are cleaned to zero when new round starts   
business: name of business venue
"""
@Models.register
class UserProfile(Base):
    __collection__ = 'user_events_profile'
    __database__ ='btdog'
    
    structure = {
        
        'phone_number'       : basestring,
         'event_id'     : basestring,
         'signedup_days'   : int,   
         'shares'   : int,
         'created' : int 
   }
    
    default_values = { 
        'phone_number'  : '',
         'signedup_days' : 0,
         'shares': 0  
    }
   

"""
Business info
title: business name

""" 
@Models.register
class Business(Base):
   __collection__ = 'business'
  
   structure = {
     'title' : unicode
   }
    

"""
User sharing
Each shared access is recorded here, most of the fields are decoded from referer_url 
referer:sharer's phone number 
referer_url: original url of shareing page
referer_platform: weixin, weibo..
access_time: time of shared access
ip: visitor's ip
"""


"""
Prize redeeming 
prize: prize redeemed
date: time of redeem

"""
@Models.register
class redeem(Base):
     __collection__ = 'redeem'
     structure = {
      'user_phone' : unicode,
      'event_id' : unicode,
      'date': int,
      'prize_type': unicode,
   }
        

