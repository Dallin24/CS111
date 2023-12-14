import requests

class LinkValidator:
    
    def __init__(self, domain_name, blocked_list):
        self.domain_name = domain_name
        self.blocked_list = blocked_list
    
    def can_follow_link(self, url):
        whole_block_list = []
        for path in self.blocked_list:
            whole_block_list.append(self.domain_name + path)
        
        enumeration = [i for i, ltr in enumerate(url) if ltr == '/']
        short_url = url[0:enumeration[2]]

        
        if(short_url != self.domain_name):
            return False

        for blocked_path in whole_block_list:
            if(blocked_path in url):
                return False
        
        return True