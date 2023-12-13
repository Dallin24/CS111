import requests

class LinkValidator:
    
    def __init__(self, domain_name, blocked_list):
        self.domain_name = domain_name
        self.blocked_list = blocked_list
    
    def can_follow_link(self, url):
        if(url[7:len(self.domain_name)] == self.domain_name[7:] or url[8:len(self.domain_name)] == self.domain_name[8:]):
            
            paths = url[(len(self.domain_name)):]
            next_slash = paths[1:].find('/')
            paths = paths[:next_slash + 1]
            if(paths in self.blocked_list):
                return False
            else:
                return True
        else:
            return False