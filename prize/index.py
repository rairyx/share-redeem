from prize import redeem
from models import Models
from flask import render_template 

@redeem.route('/', defaults={'page': 'index'})
def index(page):
 #   print redeem page
 # for  user in  Models.User.find():
 #   print  user['signedup_days']   
  return render_template('redeem.html')

@redeem.route('/validate', methods=['POST'])
def validate():
  return redirect(url_for('index'))

@redeem.route('/redeem/<userphone>', methods=['POST'])
def redeem(username):
  user_profile=Models.user_events_profile.one({"phone":userphone})
  
  return render_template('redeem.html')
