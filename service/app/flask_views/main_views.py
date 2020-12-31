from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    g,
    make_response,
    jsonify,
    session,
    redirect,
    url_for,
    )
from app.flask_views import crawl 

view = Blueprint('view',__name__,url_prefix='/')

class User:
    users = []
    drivers_info = []
    user_Instances = []   

@view.route('/')
def main():
    return render_template('index.html')

@view.route('/response/set',methods=['POST']) 
def setUserAPI():
    req = request.get_json()
    user_id =req['Id'] 
    user_passwd = req['passwd'] 
    print(user_id)
    print(user_passwd)
    session['user_id'] = user_id  
    user = {
    'id': user_id,
    'passwd' : user_passwd 
    } 
    User.users.append(user)  
    print('success')
    response = 'sent data'
    return make_response(jsonify(response),200)  


@view.route('/response/crawl/profile',methods=['POST'])
def getProfileAPI():
    user_id = session['user_id']  
    user = [x for x in User.users if x['id'] == session['user_id']][0] 
    user_id = user['id']
    user_passwd = user['passwd'] 
    
    # store instance 
    instance = crawl.Crawl(user_id,user_passwd)
    user_instance = {
        'id' : user_id,
        'instance' : instance 
    }

    # unexpected error 
    try: 
        response = instance.getProfile() 
    except Exception as e:
            print("error :",e)
            return make_response(jsonify(response),504)  

    # expected error 
    if response == 'Error':
        return make_response(jsonify(response),504)  

    # correct response 
    user_driver ={
    'id' : user_id,
    'driver' : response['driver'] 
    }  

    User.drivers_info.append(user_driver)
    User.user_Instances.append(user_instance)
    response = response['res']  
    return make_response(jsonify(response),200) 


@view.route('/response/crawl/unfollower',methods=['POST']) 
def startCrawlAPI(): 
    user_id = session['user_id']  
    instance = [x for x in User.user_Instances if x['id'] == user_id][0]['instance']
    driver = [x for x in User.drivers_info if x['id'] == user_id][0]['driver']
    try: 
        response = instance.startCrawl(driver) 
    except Exception as e:
        print("error :",e)
        response = e 
        return make_response(jsonify(response),504)  

    # expected error 
    if response == 'Error':
        return make_response(jsonify(response),504) 
    session.pop('user_id', None) 
    return make_response(jsonify(response),200)  
