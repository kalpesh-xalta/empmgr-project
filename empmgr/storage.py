 
import json

data_file = r"C:\Users\user\Downloads\Xalta-Training\Python-Bootcamp\Day-06\Assignments\empmgr-project\data\emp_data.json"

def load_employees(): 
    try: 
        with open(data_file, encoding="utf-8") as f: 
            return json.load(f) 
    except FileNotFoundError: 
        return [] 

def save_employees(employees): 
    with open(data_file, "w", encoding="utf-8") as f: 
        json.dump(employees, f, indent=2) 
