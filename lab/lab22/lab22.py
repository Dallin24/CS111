import requests
import sys
import bs4

def main():
    args = sys.argv
    link = args[1]
    tag_type = args[2]
    checkpoint = args[3]
    output_filename = args[4]
    print(f'Link: {link}')
    print(f'Tag_Type: {tag_type}')
    print(f'Checkpoint: {checkpoint}')
    print(f'File: {output_filename}')
    
    requests_object = requests.get(link)
    soup_object = bs4.BeautifulSoup(requests_object.content, features="html.parser")
    final = soup_object.find(tag_type, {'final':True})
    if final != None:
        final = final.get('final')
    print(f'Final: {final}')
    tag_info = soup_object.find(tag_type, {checkpoint:True})
    tag_info = tag_info.get(checkpoint)
    print(f'Tag_Info: {tag_info}')
    
    while final == None:
        info_list = str(tag_info).split(',')
        link = info_list[0]
        tag_type = info_list[1]
        checkpoint = info_list[2]
        print(f'Link: {link}')
        print(f'Tag_Type: {tag_type}')
        print(f'Checkpoint: {checkpoint}')
        
        requests_object = requests.get(link)
        soup_object = bs4.BeautifulSoup(requests_object.content, features="html.parser")
        final = soup_object.find(tag_type, {'final':True})
        if final != None:
            final = final.get('final')
        print(f'Final: {final}')
        tag_info = soup_object.find(tag_type, {checkpoint:True})
        tag_info = tag_info.get(checkpoint)
        print(f'Tag_Info: {tag_info}')
    
    output_file = open(output_filename, 'w')
    output_file.write(final)
    output_file.close()
    
    
    
    
    
    

if __name__ == "__main__":
    main()