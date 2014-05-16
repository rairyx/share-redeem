from mongokit import Connection, Document
from config import *

connection = Connection(MONGODB_HOST,MONGODB_PORT)
Document   = Document
