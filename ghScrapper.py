import requests as req
from bs4 import BeautifulSoup

class githubScrapper():
    def __init__(self):
        print("\n\nGitHub Scrapper initialized successfully")
        self.currPg = 1
        self.nextPg = None
        self.tab = ["followers","following"]
        self.tab_index = None
        self.followers = []
        self.following = []
        
    def config(self,name,username):
        self.name,self.username = name,username
        

    def getSoup(self,tab_index):
        try:
            self.tab_index = tab_index
            self.BASE_URL = "https://github.com/{}?tab={}&page={}".format(self.username,self.tab[self.tab_index],self.currPg)
            self.url = self.BASE_URL
            self.response = req.get(self.url)

            if str(self.response.status_code) == '404':
                print("User not found. 404")
                exit()
            else:
                self.html = self.response.content
                self.soup = BeautifulSoup(self.html,'html.parser')
                return self.soup

        except Exception as e:
            print(e)
            exit()

    
    def getFollowers(self):
        self.currPg = 1
        prev_len = 0
        curr_len = 0
        while(True):
            try:
                self.soup = self.getSoup(tab_index=0)
                follower_list = self.soup.find_all("a",class_="d-inline-block no-underline mb-1")
                
                prev_len = len(self.followers)

                for element in follower_list:
                    data  = element.find_all("span","Link--secondary")
                    self.followers.append(data[0].string)
                
                curr_len = len(self.followers)
                self.currPg+=1

                if prev_len == curr_len:
                    return self.followers

                
            except Exception as e:
                exit()


    def getFollowing(self):
        self.currPg = 1
        prev_len = 0
        curr_len = 0
        while(True):
            try:
                self.soup = self.getSoup(tab_index=1)
                following_list = self.soup.find_all("a",class_="d-inline-block no-underline mb-1")
                
                prev_len = len(self.following)

                for element in following_list:
                    data  = element.find_all("span","Link--secondary")
                    self.following.append(data[0].string)
                
                curr_len = len(self.following)
                self.currPg+=1

                if prev_len == curr_len:
                    return self.following

                
            except Exception as e:
                exit()

    def notFollowingBack(self,followers,following):
        follower_set = set(followers)
        following_set = set(following)
        notFollowingBack = following_set - follower_set
        return list(notFollowingBack)


    def userNotFollowing(self,followers,following):
        follower_set = set(followers)
        following_set = set(following)
        meNotFollowingBack = follower_set - following_set
        return list(meNotFollowingBack)
    
    def follow(self,username):
        pass

    def unfollow(self,username):
        pass
