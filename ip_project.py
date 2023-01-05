import pandas as pd
import matplotlib.pyplot as plt

file_path = "student.csv"
df = pd.read_csv(file_path, encoding="unicode_escape")

df.head(10)

def login():

  username = "admin"
  password = "password"

  input_username = input("Enter your username: ")
  input_password = input("Enter your password: ")

  if input_username == username and input_password == password:
    print("Login successful!")
  else:
    print("Incorrect username or password. Please try again.")

def selectOption():
  input_choice = int(input("Select your choice : "))
  if (input_choice == 1):
    Id=int(input("Enter Id to Edit : "))
    show_columns()
    column_name=input("Enter Column Name : ")
    value = (input("Enter Value : "))
    edit(Id,column_name,value)
  elif (input_choice == 2):
    id_to_delete=int(input("Enter Id to delete : "))
    delete(id_to_delete)
  elif (input_choice == 3):
    add_Record(int(input("Enter Id : ")),input("Enter Name : "),int(input("Enter Marks : ")),int(input("Enter Attendance : ")),input("Enter Email : "),int(input("Enter Number : ")))
  elif (input_choice == 4):
    search(int(input("Enter Id to search : ")))
  elif (input_choice == 5):
    print(df)
  elif (input_choice == 6):
    show_plot()
  elif (input_choice == 0):
    print("Exit Succesfully")
  else:
    list_option()
    selectOption()

def list_option():
  print(" 1. Edit \n 2. Delete \n 3. Add record \n 4. Search \n 5. Show Record \n 6. Show Graph \n 0. Exit")

def show_columns():
  for col in df.columns:
    print(col)

def edit(id_to_edit,column_name,new_value):
  df.at[id_to_edit-1, column_name] = new_value
  df.to_csv('file.csv', index=False)
  print("Record Updated Succesfully")
  list_option()
  selectOption()

def delete(id_to_delete):
  df1 = df[df['ï»¿id'] != id_to_delete]
  df1.to_csv('file.csv', index=False)
  print(df1)
  print("Record deleted Succesfully")
  list_option()
  selectOption()

def add_Record(value_1,value_2,value_3,value_4,value_5,value_6):
  new_record = pd.DataFrame({'id': [value_1], 'Name': [value_2],'Marks': [value_3], 'Attendance': [value_4],'Email': [value_5], 'Number': [value_6]},index=[0])
  df1 = df.append(new_record, ignore_index=True)
  df1.to_csv('file.csv', index=False)
  print("Record Added Succesfully")

  list_option()
  selectOption()

def search(search_id=1):
  results = df.loc[df['ï»¿id'] == search_id]
  print(results)
  list_option()
  selectOption()

def show_plot():
  x = df['name']
  y = df['marks']
  plt.plot(x, y)

  plt.show()


login()
list_option()
selectOption()