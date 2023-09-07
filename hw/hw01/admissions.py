# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	
# define your functions here

def convert_row_type(old_list):
    index = 0
    new_list = []
    while index <=7:
        new_list.append(float(old_list[index]))
        index+=1
    return new_list


def main():
    # Change this line of code as needed but 
    # make sure to change it back to "superheroes_tiny.csv"
    # before turning in your work!
    filename = "hw/hw01/superheroes_tiny.csv"
    input_file = open(filename, "r")    
    
    
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
   
    
    # TODO: loop through the rest of the file
    headers = headers[:-3]
    headers_splitted = headers.split(',')
    #print(headers_splitted)

    index = 1
    while index <=214:
        line = input_file.readline()
        if index==214:
            line = line
        else:
            line = line[:-1]
        original_list = line.split(',')

        student_name = [original_list[0]]
        newList = original_list[1:]
        floatList = convert_row_type(newList)

        #print(student_name)
        #print(original_list)
        #print(newList)
        #print(floatList)
        check_row_types(floatList)

        quality_list = floatList[0:4]
        semester_list = floatList[4:8]

        #print(quality_list)
        #print(semester_list)


        index+=1

    # TODO: make sure to close all files you've opened!

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()