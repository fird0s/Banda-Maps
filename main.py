from flask import Flask, request
from flask import *
bandamaps = Flask(__name__)
from flask import render_template
import base64
from models import *
from sqlalchemy.exc import *
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
import os
import random, string
import imghdr

@bandamaps.route('/')
def index():
	return render_template('index.html')


@bandamaps.route('/about')
def about():
	return render_template('about.html')


@bandamaps.route('/account')
def account():
	if "user" in session:
			get_user = session.get("user", None)  
			return redirect("/user/" + get_user)
	return render_template('account.html')

@bandamaps.route('/add_point', methods=["POST", "GET"])
def add_point():
	if  "user" not in session:
		return redirect(url_for('singin'))

	if request.method == "POST":
		if  request.form["Judul"] and request.form["Latitude"] and request.form["Longtitude"] and request.form["Description"] and request.form["TypeIcon"] and request.form["Town"] :
			point = Markers(session.get("user"), request.form["Latitude"], request.form["Longtitude"], request.form["Description"], request.form["Town"], request.form["TypeIcon"], "no-image-icon", datetime.now())
			point.Title = request.form["Judul"]
			if request.form["Tag"]:
				point.Tags = request.form["Tag"]
			else: 
				point.Tags = "None"	
			session_db.add(point)
			session_db.commit()
			session_db.close()
			
			#check last commit by session
			session_login =  session.get("user", None) 
			if session_login:
					session_login = session.get("user", None) 
			else:
				return redirect("index")		
			last_commit = session_db.query(Markers).filter_by(Adder = session_login).all()[-1]
		
			#return to /point/route/id_of_point
			return redirect("/edit_point/route/%s" % (int(last_commit.id)))

		else: 
			return "Please fill all form"	
			
	return render_template('add_point.html')

@bandamaps.route('/edit_point/route/<route>', methods=["GET", "POST"])
def point_edit(route):
	if  "user" not in session:
		return redirect(url_for('singin'))

	try:		
		data_marker = session_db.query(Markers).filter_by(id = route).one()	 
	except sqlalchemy.orm.exc.NoResultFound:
		abort(404)

	if request.method == "POST":
		if request.form["Judul"] and request.form["Latitude"] and request.form["Longtitude"] and request.form["Description"] and request.form["TypeIcon"] \
		and request.form["Town"]:
			marker_edit = session_db.query(Markers).filter_by(id = route).one()           
			if request.files["Image1"]:
				file = request.files["Image1"]
				if imghdr.what(file) == None:
					return "Please Upload just Image Extension"

				rand = [random.choice(string.letters+string.digits) for x in xrange(35)]
				rand = "".join(rand)				
				
				# remove last image uploaded
				try:
					os.remove("/home/fird0s/femaps/static/uploads/images_markers/%s" % (data_marker.Image_Upload1) ) 
				except OSError:
					pass	

				# add new images 
				file.save('/home/fird0s/femaps/static/uploads/images_markers/%s' % (rand) )
				marker_edit.Image_Upload1 = rand

			if request.form["Tag"]:
	 	   		marker_edit.Tags = request.form["Tag"]	
	 	   	else: 
	 	   		marker_edit.Tags = "None"	
				
			try:
				marker_edit.Adder = session.get("user", None)  
				marker_edit.Title = request.form["Judul"]
				marker_edit.Latitude = request.form["Latitude"]		
				marker_edit.Longtitude = request.form["Longtitude"]		
				marker_edit.Description = request.form["Description"]
				marker_edit.Location = request.form["Town"]
				marker_edit.Icon_Set = request.form["TypeIcon"]
				marker_edit.Last = datetime.now()
			#if request.files["Image1"]:
			#	file = request.files["Image1"]
			#	rand = [random.choice(string.letters+string.digits) for x in xrange(35)]
	 	   	#	rand = "".join(rand)				
	 	   	#	file.save('/home/fird0s/femaps/uploads/images_markers/%s' % (rand))
	 	   	#	marker_edit.Image_Upload1 = rand
	 	   	#if request.form["Tag"]:
	 	   	#	marker_edit.Tags = request.form["Tag"]
		 	   	session_db.add(marker_edit)		
		 	   	session_db.commit()	
	 	   	except:
	 	   		return "Error"

	return render_template("point_edit.html", route=route, data_marker= data_marker)

@bandamaps.route('/make_direction')
def make_direction():
	return render_template('make_direction.html')

@bandamaps.route('/favicon.ico')
def favicon():
	return "OK"

def encrypt(string):
	""" for make password user secure"""
	decode = base64.b64encode(string)
	return decode
	
def decrypt(string):
	""" for extrack user password from encryptinh"""
	encode = base64.b64decode(string)
	return encode
	
@bandamaps.route('/singin', methods=["POST", "GET"])
def singin():
	if "user" in session:
			get_user = session.get("user", None)  
			return redirect("/user/" + get_user)

	if request.method == "POST":
		if request.form["Username"] and request.form["Password"]:
			
				login = session_db.query(Users).filter_by(Username = request.form["Username"]).one()
				if request.form["Password"] == decrypt(login.Password):
					session["user"] = request.form["Username"]
					return redirect("/user/"+login.Username)
				else:
					return "Sorry your username/password wrong !"
			
	return render_template('singin.html')
	
@bandamaps.route('/forgotpassword')
def forgotpassword():
	return render_template('forgotpassword.html')
	
@bandamaps.route('/register', methods=["POST", "GET"])
def register():	

	if "user" in session:
			get_user = session.get("user", None)  
			return redirect("/user/" + get_user)	

	if request.method == "POST":
		if request.form["Username"] and request.form["Password"] and  request.form["Email"] \
		   and request.form["FullName"] and request.form["Address"]  and request.form["Phone"] and request.form["Work"]:
			try:	
				register = Users(request.form["Username"], request.form["FullName"], encrypt(request.form["Password"]), request.form["Email"], request.form["Phone"], request.form["Work"], datetime.now())
				register.Alamat = request.form["Address"]
				register.Date_Joined = datetime.now()
				session_db.add(register)
				session_db.commit()
				return "OK"
			except IntegrityError:
				return "Sorry, your mail/username have already registered"
		else:
			return "Please fill all form"	
	return render_template("register.html")

@bandamaps.route('/user/<username>')
def user(username):
	try :
		data = session_db.query(Users).filter_by(Username = username).one() 
		
	except sqlalchemy.orm.exc.NoResultFound, sqlalchemy.exc.InvalidRequestError:	
		return "No User"
	return render_template('user.html', data=data)


@bandamaps.route('/user/logout', methods=["POST", "GET"])
def logout():
	 if not "user" in session:
	 	 return redirect(url_for("index"))
	 get_user = session.get("user", None)
	 profil_data = session_db.query(Users).filter_by(Username = get_user).one()	 
	 profil_data.Last_Log = request.remote_addr
	 session_db.add(profil_data)
	 session_db.commit() 
         session_db.close()
         session.pop("user", None)
         return redirect(url_for('account'))

@bandamaps.errorhandler(404)
def page_not_found(e):
	return render_template("error404.html")

@bandamaps.route('/histories', methods=["POST", "GET"])
def history():
	all_markers = session_db.query(Markers).all()
	all_markers.reverse()
	return render_template("history.html", all_markers=all_markers)

@bandamaps.route('/test', methods=["POST", "GET"])
def test():
	if request.method == "POST":
		if request.files["file"]:
			file = request.files["file"]
	 	   	rand = [random.choice(string.letters+string.digits) for x in xrange(35)]
	 	   	rand = "".join(rand)
	    	
			file.save('/home/fird0s/femaps/uploads/images_markers/%s' % (rand))
		
	return render_template("file.html")



if __name__ == '__main__':
    bandamaps.debug = True
    bandamaps.secret_key = '_Wx0ksck~\[p99923@#@!#!@#423raakleas'
    bandamaps.run()
    
