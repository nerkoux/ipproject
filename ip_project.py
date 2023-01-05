import pandas as pd
import matplotlib.pyplot as plt

file_path = "data.csv"
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
    Id=int(input("Enter Sector to Edit : "))
    show_columns()
    column_name=input("Enter Column Name : ")
    value = (input("Enter Value : "))
    edit(Id,column_name,value)
  elif (input_choice == 2):
    id_to_delete=(input("Enter Sector to delete : "))
    delete(id_to_delete)
  elif (input_choice == 3):
    add_Record(input("Enter Sector Name : "),int(input("Enter Year : ")),input("Enter Month : "),int(input("Enter Cereal and products : ")),int(input("Enter Meat and Fish : ")),int(input("Enter Egg : ")),int(input("Enter Milk and Products : ")),int(input("Enter Oils and Fats : ")),int(input("Enter Fruits : ")),int(input("Enter Vegetables : ")),int(input("Enter Pulses and products : ")),int(input("Enter Sugar And Confectionery : ")),int(input("Enter Spices : ")),int(input("Enter Non Alcoholic Beverages : ")),int(input("Enter Prepared meals, snacks, sweets etc. : ")),int(input("Enter Food and beverages:  ")),int(input("Enter Pan, tobacco and intoxicants:  ")),int(input("Enter General index:  ")))
  elif (input_choice == 4):
    search(input("Enter Sector to search : "))
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
  df1 = df[df['Sector'] != id_to_delete]
  df1.to_csv('file.csv', index=False)
  print(df1)
  print("Record deleted Succesfully")
  list_option()
  selectOption()

def add_Record(value_1,value_2,value_3,value_4,value_5,value_6,value_7,value_8,value_9,value_10,value_11,value_12,value_13,value_14,value_15,value_16,value_17,value_18):
  new_record = pd.DataFrame({'Sector': [value_1], 'Year': [value_2],'Month': [value_3], 'Cereal and Products': [value_4],'Meat and Fish': [value_5], 'Egg': [value_6],'Milk and products': [value_7],'Oils and Fats': [value_8],'Fruits': [value_9],'Vegetables': [value_10],'Pulses and Products': [value_11],'Sugar and Confectionery': [value_12],'Spices': [value_13],'Non-alcoholic Beverages': [value_14],'Prepared meals, snacks, sweets etc.': [value_15],'Enter food and beverasges': [value_16],'Pan, tobacco and intoxicants': [value_17],'General index': [value_18]},index=[0])
  df1 = df.append(new_record, ignore_index=True)
  df1.to_csv('file.csv', index=False)
  print("Record Added Succesfully")

  list_option()
  selectOption()

def search(search_id=1):
  results = df.loc[df['Sector'] == search_id]
  print(results)
  list_option()
  selectOption()

def show_plot():
  x = df['Sector']
  y = df['General index']
  plt.plot(x, y)

  plt.show()


login()
list_option()
selectOption()
