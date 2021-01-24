import os

'''This version works fine'''

#Function that splits the string in the alphabetical and numerical component.
#'Casacca11' --> 'Casacca' '11'
def mysplit(s):
     head = s.rstrip('0123456789')
     tail = s[len(head):]
     return head, tail


print('What\'s the starting folder? The path must be written as follows: C:\..\.. etc.')
starting_path=input()
path=(starting_path)        #There could be an error depening on how starting_path must be implemented in path.

#Creating the directory (if not already existing)
print('What\'s the target folder to which the files must be moved?')
ending_path=input()
try:
    os.mkdir(ending_path)
    print("I created the '{}' folder".format(ending_path))
except:
    print('The {} folder already exists, the file will just be transfered'.format(ending_path))
#Moving the files to declared directory
for file in os.listdir(starting_path):
    	os.rename(starting_path + '\\' + file, ending_path + '\\' + file)


ciclo = 'y'
while ciclo == 'y':
    print('What is the extensions of the file you want to sort? Don\'t write the .(dot) just the extension.')
    ext=input()

    for aut in os.listdir(ending_path):
        a=aut.split('.')   
        if ext not in a:  #This line makes sure that only files with a .txt extensions are considered by this program.
            continue        
        else:
            b=mysplit(a[0])     #The mysplit function, as defined above, divides the string in his letteral and numerical part
            if b[0] in os.listdir(ending_path):    #If there is already a file in the directory with the same letteral part and with no extension.
                                                    #In other words a folder
                os.replace(ending_path + '\\' + aut, ending_path + '\\' + b[0] + '\\' + aut)
            else:
                os.mkdir(ending_path + '\\' + b[0])     
                os.replace(ending_path + '\\' + aut, ending_path + '\\' + b[0] + '\\' + aut) 
    
    print('All the .{} files have been sorted, do yo wish to continue?'.format(ext))
    print('Press y/n')
    ciclo = input()