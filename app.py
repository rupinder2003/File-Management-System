import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name {filename} alredy exists !")
    except Exception as E:
        print("An error occurred")

def view_all_files():
    files=os.listdir()
    if not files:
        print("No files found!")
    else:
        print("Files in Directory")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occurred!")
        
def read_file(filename):
    try:
        with open("sample.txt","r") as f:
            content = f.read()
            print(f" Content of {filename}: \n{content}")    
            
    except FileNotFoundError:
        print(f"{filename} dosent exist!")
        
    except Exception as e:
        print("An error occurred")    
        
def edit_file(filename):
    try:
        with open("sample.txt","a") as f:
            content= input("Enter data to add = ")
            f.write(content + "/n") 
            print("Content added to {filename} successfully !")
    
    except FileNotFoundError:
        print(f"{filename} dosent exist!")
        
    except Exception as e:
        print("An error occurred")    
        
def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create File")
        print("2: View all File")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit File")
       
        choice =input("Enter your choice(1-6) = ")
       
        if choice=='1':
           filename=input("Enter the file-name to create = ")
           create_file(filename)
           
        elif choice =='2':
            view_all_files()
            
        elif choice =='3':
            filename= input("Enter the file name you want to delete =")
            delete_file(filename)
            
        elif choice=='4':
            print("Enter file name to read = ")
            read_file(filename)
            
        elif choice == '5':
            print("Enter file name to edit = ")
            edit_file(filename)
            
        elif choice == '6':
            print("Closing the app...")
            break
        
        else:
            print("Invalid syntax")
            
if __name__ == "__main__":
    main()