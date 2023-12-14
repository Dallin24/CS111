import pprint
import requests
import bs4
import matplotlib
import sys
from LinkValidator import LinkValidator

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
    domain_name = 'https://cs111.byu.edu'
    args = sys.argv[1:]
    command = None
    input_link = None
    output_file_1 = None
    output_file_2 = None
    filter_command = None
    
    if (len(args) != 4):
        print(f'invalid arguments')
        return
    
    command = args[0]
    input_link = args[1]
    output_file_1 = args[2]
    output_file_2 = args[3]
    filter_command = args[3]
        
    if(len(args[3]) == 2):
        output_file_2 = None
        if filter_command not in ['-s','-g','-f','-m']:
            print(f'invalid arguments')
            return
    else:
        filter_command = None

    
    if(command == '-c'):
        print('-Count-')
    # The -c command is for counting the links. 
    # A. The URL is the starting page of the search. 
    # B. Output file 1 will contain the histogram image 
    # C. Output file 2 will be CSV formatted file of all the links and their reference counts.
        # Task 1
        exclusion_list = parse_robots(domain_name)
        print(f'Exclude: {exclusion_list}')
        link_validity = LinkValidator(domain_name, exclusion_list)
        
        # domain_name = input_link
        # enumeration = [i for i, ltr in enumerate(domain_name) if ltr == '/']
        # domain_name = domain_name[0:enumeration[2]]
        # exclusion_list = parse_robots(domain_name)
        # link_validity = LinkValidator(domain_name, exclusion_list)
        
        # Task 2
        visiting_list = [input_link]
        visiting_dict = {input_link:0}
        
        # Task 3
        current_index = 0
        while current_index < len(visiting_list):
            print(f'Cycle: {current_index}')
      
            current_link = visiting_list[current_index]
            print(f'  Searching Link: {current_link}')
            if (link_validity.can_follow_link(current_link)):
                print('  Can follow link? Yes')
                page = requests.get(current_link)
                html = bs4.BeautifulSoup(page.text,"html.parser")
                
                visit_count = visiting_dict.get(current_link)
                visiting_dict.update({current_link:visit_count+1})
                
                for tag in html.find_all('a'):
                    found_link = tag.get('href')
                    if (found_link[0:4] != 'http'):
                        enumeration = [i for i, ltr in enumerate(current_link) if ltr == '/']
                        current_link = current_link[0:enumeration[len(enumeration)-1]]
                        current_link += '/' + found_link
                        found_link = current_link   
                    
                    print(f'  Found Link: {found_link}')
                    if (found_link not in visiting_list):
                        visiting_list.append(found_link)
                        visiting_dict.update({found_link:0})
                    
                    if (found_link in visiting_list and visiting_list.index(found_link) < current_index):
                        visit_count = visiting_dict.get(found_link)
                        visiting_dict.update({found_link:visit_count+1})
                        
                    # if(href in visiting_list and visiting_list.index(href) < current_index):
                    #     visiting_dict.update({href: visiting_dict.get(href) + 1})
                    # else:
                    #     visiting_dict.update({href:0})
                    #     visiting_list.append(href)
            else:
                print('  Can follow link? No')        
            current_index+=1
        pprint.pprint(visiting_dict)
    
    elif(command == '-p'):
    # The -p command is to extract and plot data. 
    # A. The URL is the page that contains the data to extract. 
    # B. Output file 1 will contain the data plot
    # C. Output file 2 will contain the data in CSV format.
        print('Plot')
    
    elif(command == '-i'):
    # The -i option is for finding and manipulating an image. 
    # A. The URL is the page where we want to extract images. 
    # B. The output file prefix is a string that will be prepended to the name of every image manipulated to produce the name of the output image file. 
    # C. The filter to run will be a flag specifying which filter from your image manipulation program to run.
        if(filter_command == '-s'):
        # Sepia Filter
            print('Sepia')
        elif(filter_command == '-g'):
        # Grayscale Filter
            print('Greyscale')
        elif(filter_command == '-f'):
        # Vertical Flip
            print('Vertical')
        elif(filter_command == '-m'):
        # Horizontal Flip aka Mirror
            print('Mirror')

if __name__ == "__main__":
    main()