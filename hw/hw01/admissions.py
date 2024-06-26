# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
import csv

def multiplier_maker(n):
    return lambda element : element * n

def make_water( multiplier ):
    nhydrogen,noxygen = 2.0, 1.0
    nmolecules = multiplier_maker()
    print( str(multiplier(nhydrogen) ) + ' atoms hydrogen.' )
    print( str(multiplier(noxygen) ) + ' atoms oxygen.' )
    print( 'Produces ' + str(multiplier(nmolecules)) + ' molecules of water.' )


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

def calculate_score(list):
    score = ((list[0] / 160)*0.3) + (((list[1] * 2) )*0.4) + ((list[2])*0.1) + ((list[3])*0.2)
    return score

def is_outlier(list):
    if((list[0] / 160 + 2 < list[1] * 2) or float(list[2]) == 0.0):
        return True
    else:
        return False

def calculate_score_improved(quality_list, student_score):
    if((is_outlier(quality_list)) or (float(student_score[1]) >= 6.00)):
        return True
    else:
        return False
    
def grade_outlier(list):
    list = sorted(list)
    if(list[1] - list[0] > 20):
        return True
    else:
        return False

def grade_improvement(list):
    if(list[3] >= (list[2]) and list[2] >= (list[1]) and list[1] >= (list[0])):
        return True
    else:
        return False
def main():
    make_water(lambda element: element * n)
    # Change this line of code as needed but 
    # make sure to change it back to "superheroes_tiny.csv"
    # before turning in your work!
    row_count = 0
    filename = "superheroes_tiny.csv"
    with open(filename,"r") as openfile:
        reader = csv.reader(openfile)
        row_count = len(list(reader))

    #print(row_count)
    input_file = open(filename, "r")    
    
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    headers = headers[:-3]
    headers_splitted = headers.split(',')
    #print(headers_splitted)
    
    # TODO: loop through the rest of the file
    index = 1
    student_scores_list = []
    chosen_students_list = []
    outlier_students_list = []
    chosen_improved_list = []
    improved_chosen_list = []
    extra_improved_list = []
    test_list = []

    while index < row_count:
        line = input_file.readline()
        original_list = line.split(',')
        student_name = original_list[0]
        newList = original_list[1:]
        floatList = convert_row_type(newList)

        check_row_types(floatList)

        quality_list = floatList[0:4]
        semester_list = floatList[4:8]

        raw_score = ("%.2f" % calculate_score(quality_list))
        student_score = student_name, raw_score
        student_scores_list.append(student_name + ','+ raw_score + '\n')

        if(float(student_score[1]) >= 6.00):
            chosen_students_list.append(student_name + '\n')

        if(is_outlier(quality_list)):
            outlier_students_list.append(student_name + '\n')
        
        if((is_outlier(quality_list) and float(student_score[1]) >= 5) or (float(student_score[1]) >= 6.00)):
            chosen_improved_list.append(student_name + '\n')
        
        if((float(student_score[1]) >= 6.00) or ((float(student_score[1]) >= 5.00) and (is_outlier(quality_list) or grade_outlier(semester_list) or grade_improvement(semester_list)))):
            extra_improved_list.append(student_name + '\n')

        if(calculate_score_improved(quality_list, student_score)):
            # test_list = quality_list
            # test_list.insert(0, student_name)
            list_string = str(quality_list)
            list_string = list_string[:-1]
            list_string = list_string[1:]
            list_string = list_string.replace(" ", "")
            improved_chosen_list.append(student_name + ',' + list_string + '\n')

        #print(student_name)
        #print(original_list)
        #print(newList)
        #print(floatList)
        #print(quality_list)
        #print(semester_list)
        #print(scores)
        index+=1
    
    #print(student_scores)

    # student_scores_file = "student_scores.csv"
    # with open(student_scores_file, 'w', newline='') as student_scores_csvfile:
    #     csvwriter = csv.writer(student_scores_csvfile)
    #     csvwriter.writerows(student_scores_list)
    student_scores_file = "student_scores.csv"
    student_scores_csvfile = open(student_scores_file, 'w')
    student_scores_csvfile.writelines(student_scores_list)

    chosen_students_file = "chosen_students.txt"
    chosen_students_txtfile = open(chosen_students_file, 'w') 
    chosen_students_txtfile.writelines(chosen_students_list)

    outlier_students_file = "outliers.txt"
    outlier_students_txtfile = open(outlier_students_file, 'w') 
    outlier_students_txtfile.writelines(outlier_students_list)

    chosen_improved_file = "chosen_improved.txt"
    chosen_improved_txtfile = open(chosen_improved_file, 'w') 
    chosen_improved_txtfile.writelines(chosen_improved_list)

    # improved_chosen_file = "improved_chosen.csv"
    # with open(improved_chosen_file, 'w', newline='') as  improved_chosen_csvfile:
    #     csvwriter = csv.writer(improved_chosen_csvfile)
    #     csvwriter.writerows(improved_chosen_list)
    improved_chosen_file = "improved_chosen.csv"
    improved_chosen_csvfile = open(improved_chosen_file, 'w')
    improved_chosen_csvfile.writelines(improved_chosen_list)

    extra_improved_file = "extra_improved_chosen.txt"
    extra_improved_txtfile = open(extra_improved_file, 'w') 
    extra_improved_txtfile.writelines(extra_improved_list)

    # TODO: make sure to close all files you've opened!

    input_file.close()

    student_scores_csvfile.close()
    improved_chosen_csvfile.close()

    chosen_improved_txtfile.close()
    outlier_students_txtfile.close()
    chosen_improved_txtfile.close()
    extra_improved_txtfile.close()

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()