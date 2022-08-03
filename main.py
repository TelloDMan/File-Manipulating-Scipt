import os
import shutil

print("=====================    ===================  ======               ======                  ===============\n=====================    ===================  ======               ======                ===================\n        =====            =====                ======               ======                =====         =====\n        =====            =====                ======               ======                =====         =====\n        =====            ===================  ======               ======                =====         =====\n        =====            ===================  ======               ======                =====         =====\n        =====            ===================  ======               ======                =====         =====\n        =====            =====                ======               ======                =====         =====\n        =====            =====                ======               ======                =====         =====\n        =====            ===================  ===================  ===================   ===================\n        =====            ===================  ===================  ===================     ===============\n")
print("                                       ######WELCOME TO MY PROGRAM######                                ")

#this code gets the source folder of images that will be copied
def get_dest_images():
    loc=input("\n\n----->Write the destination Folder: ")
    while True:
        try:
            os.chdir(loc)
            images=os.getcwd()
            break
        except:
            print("!!!!!!!!!INVALID LOCATION!!!!!!!!!")
            print("\nTry again!!")
            loc=input("\n\n----->Write the destination Folder: ")
            continue
    return images
#this function takes the text.txt file of image names
def get_file_name():
    number_file_name=input("\n\n\n--The file name of the Numbers: ")
    return number_file_name

#this function gets file types
def get_file_type():
    file_type=input("\n\n--->Enter the file type like('.jpg' , '.png' , '.jpeg): ")
    return file_type

#this function lists the names in a list 
def name_lister(list_name):
    name=list_name()
    while True:
        try:
            os.path.isfile(str(name))
            with open(name+".txt","r") as f:
                number_list=f.read()
            break
        except:
            print("Wrong file name!\n\n------>>>Try Again...")
            name=list_name()
            continue
    seperator=input("****Please mention the seperator used inside the File: ")
    number_list_filtered=number_list.split(seperator)
    return number_list_filtered

#this function copies the files to destination
def process(inputs):
    ext=get_file_type()
    while True:
        try:
            new_folder=input("\n\n\n\n###What do you wanna be the name of the copy Folder: ")
            os.mkdir(new_folder)
            break
        except:
            print("#########!!!!!!!!!You Cant use this Name!!!!!!!!!#########")
            continue
    loc_nat=os.getcwd()
    dest1=get_dest_images()
    dest2=loc_nat+'\\'+new_folder
    for x in inputs:
        os.chdir(dest1)
        os.path.isfile(x)
        os.chdir(dest2)
        shutil.copy(dest1+'\\'+x+ext ,dest2)


def process_rename():
    start=0
    get_dest_images()
    list_of_file=os.listdir()
    for x in list_of_file:
        if len(str(start))<2:
            start="0"+str(start)
        os.rename(x,str(start)+".png")
        start=int(start)
        start+=1

x=input("Please Press Enter To Continue---->")
y=input("\n\n\n\n\n\nChoose one of the functions to Continue:\n(1)File Renamer.\n(2)File Copier.\n(3)File prefix Adder.\n\n\nChoose(1--2--3):---->")

if int(y)==1:
    process_rename()
elif int(y)==2:
    process(name_lister(get_file_name))