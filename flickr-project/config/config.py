import mysql.connector
import os, time, sys, math
from flickrapi import FlickrAPI
#mySQL接続情報
db_config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "flickr_SQL"
}
#Flickr_API接続情報
flickr_api_key = "your_flickr_api_key"
flickr_api_secret = "your_flickr_api_secret"
