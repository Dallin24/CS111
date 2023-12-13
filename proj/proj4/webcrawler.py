import requests
import bs4
import matplotlib
import sys

def parse_robots(domain_name):
# Returns the list of paths to exclude from domain_name's robots.txt file.
    requests_object = requests.get(domain_name + '/robots.txt')
    text_info = requests_object.text
    
    avoid_list = []
    for line in text_info.splitlines():
        if line == 'User-agent: *':
            continue
        avoid_list.append(line[10:])
    return avoid_list

def main():
    args = sys.argv[1:]
    command = args[0]
    url_link = args[1]
    output_file_1 = args[2]
    output_file_2 = args[3]
    filter_command = args[3]
    
    if(len(args[3]) == 2):
        output_file_2 = None
    else:
        filter_command = None

    
    if(command == '-c'):
    # The -c command is for counting the links. 
    # A. The URL is the starting page of the search. 
    # B. Output file 1 will contain the histogram image 
    # C. Output file 2 will be CSV formatted file of all the links and their reference counts.
        pass
    
    elif(command == '-p'):
    # The -p command is to extract and plot data. 
    # A. The URL is the page that contains the data to extract. 
    # B. Output file 1 will contain the data plot
    # C. Output file 2 will contain the data in CSV format.
        pass
    
    elif(command == '-i'):
    # The -i option is for finding and manipulating an image. 
    # A. The URL is the page where we want to extract images. 
    # B. The output file prefix is a string that will be prepended to the name of every image manipulated to produce the name of the output image file. 
    # C. The filter to run will be a flag specifying which filter from your image manipulation program to run.
        if(filter_command == '-s'):
        # Sepia Filter
            pass
        elif(filter_command == '-g'):
        # Grayscale Filter
            pass
        elif(filter_command == '-f'):
        # Vertical Flip
            pass
        elif(filter_command == '-m'):
        # Horizontal Flip aka Mirror
            pass
        
        else:
            raise Exception('invalid arguments')
        
    else:
        raise Exception('invalid arguments')

if __name__ == "__main__":
    main()