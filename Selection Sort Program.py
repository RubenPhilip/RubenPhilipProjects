import random # random integer values 
import time # import time for the delay statements  
import os # import os to open up the notepad file with the timings 

print ("Welcome to the Selection Sort Program")
time.sleep(3)
print ("The purpose of the program is find the sorting times for different user inputed array lengths")
time.sleep(4)
print ("Let's begin")
print (" ")

def selectionsort(length):
    """selectionsort(int) -> str
    Takes the list length and determines the time is takes for the selection sort to take place. 
    >>> selectionsort (10)
    Length 10 took 5.2e-05 s 
    """
    
    find_list = [] # create list 
    for i in range (length): # loop to generate random numbers between 1 and 100 to add to the list. The amount of integers in the list depends on the length. 
        find_list.append(random.randrange(1, 101, 1))
    alist = find_list # stores find_list to alist 

    t0 = time.clock() # clock starts time 
    
    for i in range(len(alist)): # start of the selection sort code 

       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j

       position = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = position # end of the selection sort code 

    final_time = str(round(time.clock()-t0,6)) # stores the time is takes to complete the selection sort process 
    num = str(len(alist)) # stores the array length 

    return  "Length "+num+" took "+final_time+" s" # final output 

    
def find_times(mylist):
    """find_times(list) -> str
    Takes the list of array lengths inputed by the user and runs it through the selectionsort function.
    A file will appear to show the time it takes for each inputed array length. 
    >>> find_times ([10, 20])
    Length 10 took 5.2e-05 s
    Length 20 took 5.9e-05 s
    """
    
    num_list = len(mylist) # stores num_list as amount of array lengths inputed 
    x = 0
    answer_list =[] 
    while x < num_list: # puts each array length inputed through the selectionsort function to get times 
        t = selectionsort(int(mylist[x]))
        answer_list.append(t) # inputs each time into the answer list 
        x += 1 

    answer_list = "\n".join(answer_list) 
    my_file = open("TimeSortingTest.txt", "w+") # open file 
    my_file.writelines(answer_list) # prints the list into the file, separate line for each value 
    my_file.close() # close file 
    os.startfile("TimeSortingTest.txt") # opens the file so the user can get the different timings 
    time.sleep(3) 
    print("")
    main()

def leave(): # the quit function
    """leave()-> str 
    Prints out Good Bye
    """
    print("Good Bye") # just prints good bye

def main(): # main function to allow user to choose which option needs to be performed
    """main()-> 
    Records the user inputs and depending on the input, the output appears 
    """
    print("1. The sorting process") 
    print("2. Quit program")
    option = input("Your Option: ") # user inputs the number that corresponds the option they want
    print ("")
    
    if option == "1":
        while True: # using try catch to get the user to only input an integer
            try:
                num_list = int(input("How many lists do you want? (only integer): "))
                break
            except:
                print ("Invalid Entry")
        print ("Enter", num_list, "list length(s)") 
        my_list = []
        print ("WARNING: Inputing high values will result in a longer wait time")
        print ("If you want quick results recommended length should be under 5000")
        for i in range (num_list): # loop runs the number of times of the num_list
            while True:
                try:
                    list_length = int(input("Enter list length (only integer): ")) # user inputs list lengths  
                    break
                except:
                    print ("Invalid Entry")
            my_list.append(list_length) # add inputed list length to the list 
        print ("Please Wait")
        find_times(my_list) 
    elif option == "2":
        print("Thank you for trying the sorting program.") 
        leave() # closes the program 
    else:
        print("Invalid Input. Try Again.") # result if anything else is inputed by the user 
        main() # recall function again

main() 

