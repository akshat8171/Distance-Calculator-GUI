 
from tkinter import *
  
 
import requests, json 
  

def result(source, destination, travel_modes): 
  

    api_key = 'AIzaSyDL6WgHyXrV-FSw11cjcByobjIA1Ihgw1A'
  
    base = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
  
    if travel_modes == "train": 
  
        complete_url = (base + 'origins=' + source +  '&destinations=' + destination + '&mod= transit&transit_mode=train' +  '&key='+api_key )

        r = requests.get(complete_url) 
          
    else: 
          

        complete_url = base + 'origins=' + source+ '&destinations='+ destination + '&mode='+travel_modes+'&key='+ api_key 

        r = requests.get(complete_url) 

    x = r.json() 
  
    print(x['rows'])
    row = x['rows'][0] 
    cell = row['elements'][0] 
  
    if cell['status'] == 'OK' : 
  
        distance_field.insert(10, cell['distance']['text']) 
        duration_field.insert(10, cell['duration']['text']) 
          
    else : 
          

        mode_field.insert(10, cell['status']) 
        distance_field.insert(10, cell['status']) 
  
                          
def find() : 
  

    source = source_field.get() 
    destination = destination_field.get() 
    travel_modes = mode_field.get() 

    result(source, destination, travel_modes) 

def train() : 
    mode_field.insert(10, "train") 
  

def driving() : 
    mode_field.insert(10, "driving") 
  

def walking() : 
    mode_field.insert(10, "walking") 
  

def del_source() : 
    source_field.delete(0, END) 
    distance_field.delete(0, END) 
    duration_field.delete(0, END) 

def del_destination() : 
    destination_field.delete(0, END) 
    distance_field.delete(0, END) 
    duration_field.delete(0, END) 
  
def del_modes() : 
    mode_field.delete(0, END) 
    distance_field.delete(0, END) 
    duration_field.delete(0, END) 
  
 
def delete_all() : 
    source_field.delete(0, END) 
    destination_field.delete(0, END) 
    mode_field.delete(0, END) 
    distance_field.delete(0, END) 
    duration_field.delete(0, END) 
  
  
if __name__ == "__main__" : 
  

    root = Tk()
    
    root.configure(background = 'light blue')
    
    root.geometry("1024x1024") 
  
    headlabel = Label(root, text = 'welcome to distance time calculator', 
                      fg = 'black', bg = "red") 
      
    label1 = Label(root, text = "Source:", 
                   fg = 'black', bg = 'dark green') 
  
    label2 = Label(root, text = "Destination:", 
                   fg = 'black', bg = 'dark green') 
      

    label3 = Label(root, text = "Choose travelling modes: ", 
                   fg = 'black', bg = 'red') 
  

    label4 = Label(root, text = "Distance:", 
                    fg = 'black', bg = 'dark green') 
  
    label5 = Label(root, text = "Duration:",  
                    fg = 'black', bg = 'dark green') 
      

    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 2, column = 0, sticky ="E") 
    label3.grid(row = 3, column = 1) 
    label4.grid(row = 7, column = 0, sticky ="E") 
    label5.grid(row = 8, column = 0, sticky ="E") 
      

    source_field = Entry(root) 
    destination_field = Entry(root) 
    mode_field = Entry(root) 
    distance_field = Entry(root) 
    duration_field = Entry(root) 
  

    source_field.grid(row = 1, column = 1, ipadx ="100") 
    destination_field.grid(row = 2, column = 1, ipadx ="100") 
    mode_field.grid(row = 5, column = 1, ipadx ="50") 
    distance_field.grid(row = 7, column = 1, ipadx ="100") 
    duration_field.grid(row = 8, column = 1, ipadx ="100") 
  
  

    button1 = Button(root, text = "CLEAR", bg = "red", 
                     fg = "black", command = del_source) 
  
    button2 = Button(root, text = "CLEAR", bg = "red", 
                     fg = "black", command = del_destination) 
  
    button3 = Button(root, text = "RESULT",  
                     bg = "red", fg = "black", 
                                command = find) 
  
    button4 = Button(root, text = "CLEAR ALL", 
                     bg = "red", fg = "black", 
                            command = delete_all) 
  
    button5 = Button(root, text = "Train", command = train) 
  
    button6 = Button(root, text = "Driving", command = driving) 
  
    button7 = Button(root, text = "Walking", command = walking) 
  
    button8 = Button(root, text = "CLEAR", 
                     fg = "black", bg = "red", 
                           command = del_modes) 

    button1.grid(row = 1, column = 2) 
    button2.grid(row = 2, column = 2) 
    button3.grid(row = 6, column = 1) 
    button4.grid(row = 9, column = 1) 
    button5.grid(row = 4, column = 0) 
    button6.grid(row = 4, column = 1) 
    button7.grid(row = 4, column = 2) 
    button8.grid(row = 5, column = 2) 
  

    root.mainloop()
