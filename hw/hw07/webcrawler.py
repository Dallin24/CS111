import requests

def parse_robots(domain_name):
    """Returns the list of paths to exclude from domain_name's robots.txt file."""
    requests_object = requests.get(domain_name + '/robots.txt')
    text_info = requests_object.text
    
    avoid_list = []
    for line in text_info.splitlines():
        if line == 'User-agent: *':
            continue
        avoid_list.append(line[10:])
    return avoid_list