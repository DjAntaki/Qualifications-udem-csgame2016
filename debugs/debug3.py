#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ce programme s'exécute python 2.x
# Par contre, il y a une faille de sécurité.

import hashlib

def hash_value(val):
  return hashlib.sha224(val).hexdigest()

admin_data = { 'name':      '12345',
               'password':  hash_value("45678") }

def login(username, password):
  hashed_password = hash_value(password) 
  if admin_data['name'] != username or admin_data['password'] != hashed_password:
      print "Invalid username or password"
  else:
      print "Welcome"

input_name = input("Username: ")
input_pwd  = input("Password: ")

login(str(input_name), str(input_pwd))
