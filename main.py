from ghScrapper import githubScrapper

def main():
    name = input("Enter your name: ")
    username = input("Enter your github username: ")

    gh = githubScrapper()
    gh.config(name=name,username=username)

    followers = gh.getFollowers()
    following = gh.getFollowing()   
    
    print("---------------------------------------------------")
    print("                      UserInfo")
    print("---------------------------------------------------")
    print("Username: {}".format(username))
    print("Followers: {}".format(len(followers)))
    print("Following: {}".format(len(following)))
    
    notFollowingBack = gh.notFollowingBack(followers,following)
    userNotFollowing = gh.userNotFollowing(followers,following)

    print("Not following Back: {}".format(notFollowingBack))
    print("\nUser not following: {}".format(userNotFollowing))
    
    



if __name__ == '__main__':
    main()




