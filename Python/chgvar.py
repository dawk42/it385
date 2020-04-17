#!/usr/bin/python3
# working with variables

my_var = 'hi'

def read_var():
  print(my_var)

def chg_local():
  my_var = 'Bye'
  print(my_var)

def chg_glb():
  global my_var
  my_var = 'Adios'
  print (my_var)

read_var()
chg_local()
print(my_var)
chg_glb()
read_var()
