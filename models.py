#!/usr/bin/python
from sqlalchemy import Column, String, Integer, create_engine, TEXT, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import *
import sqlalchemy

#setting for connect to database, we use MySQL
db = create_engine('mysql://fird0s:fird0s@localhost/banda_maps.db', convert_unicode=True)
#banda-maps is Mysql Username Privileges
#banda-maps is Mysql Password of Username 
#banda-maps.db is Database Name

Base = declarative_base()

class Users(Base):
	__tablename__ = "maps_users"
	
	id = Column(Integer, primary_key=True)
	Username = Column(String(25), primary_key=True, unique=True)
	FullName = Column(String(40))
	Alamat = Column(String(60))
	Password = Column(String(30))
	Email = Column(String(30), unique=True)
	Phone = Column(String(16))
	Work = Column(String(16))
	Profile_Image_Location = Column(String(200))
	Profile_Description = Column(TEXT())
	Website = Column(String(30))
	Date_Joined = Column(DATE())
	Last_Log = Column(String(100))
	
	def __init__(self, Username, FullName, Password, Email, Phone, Work, Last_Log):
		self.Username = Username 
		self.FullName = FullName
		self.Password = Password
		self.Email = Email
		self.Phone = Phone
		self.Work = Work
		self.Last_Log = Last_Log

	
class Markers(Base):
	__tablename__ = "maps_markers"
	
	id = Column(Integer, primary_key=True)
	Adder = Column(String(30))
	Title = Column(String(50))
	Latitude = Column(String(30))
	Longtitude = Column(String(30))
	Description = Column(TEXT)  
	Location = Column(String(30))
	Icon_Set = Column(String(15))
	Image_Upload1 = Column(String(40))
	Image_Upload2 = Column(String(40))
	Image_Upload3 = Column(String(40))
	Last = Column(String(100))
	Tags = Column(String(100))

	
		
	
	#icon set
	#Home = icon-home 
	#Bank = icon-money
	#Building = icon-building
	#store = icon-shopping-cart
	#Field = 
	#Toilet =  icon-user
	#Airport =  icon-plane
	#Terminal = truck
	#coffe = icon-coffee
	#Restaurant/Cantten  =  icon-food
	#Park = default-marker
	#ATM = icon-credit-card
	#Perpusakaan = icon-book
	#Rumah Sakir = icon-hospital
	#perkantoran = icon-suitcase
	#Uncategorized = no icon (use default marker without use awesome Markers)


	def __init__(self, Adder, Latitude, Longtitude, Description, Location, Icon_Set, Image_Upload1, Last):
		self.Adder = Adder
		self.Latitude = Latitude
		self.Longtitude = Longtitude
		self.Description = Description
		self.Location = Location
		self.Icon_Set = Icon_Set
		self.Image_Upload1 = Image_Upload1
		self.Last = Last 
		
Session = sessionmaker(bind=db)
session_db = Session()  	
Base.metadata.create_all(db)

