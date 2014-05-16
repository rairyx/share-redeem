from blueprints import index_page
from models import Models

@index_page.route('/', defaults={'page': 'index'})
@index_page.route('/<page>')
def show(page):
 #   print page
  for  user in  Models.User.find():
    print  user['signedup_days']   
  return 'simple_page %s' % page

@index_page.route('/user/<username>')
def show_user_profile(username):
  for  user in  Models.User.find(): 
    print user['user_phone']
  return 'user profile'   
