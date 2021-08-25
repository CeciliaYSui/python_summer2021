# --------------------------------------------------------------------------------------------------------------
# Project -------------------------- Python Camp HW#3 
# Developer ------------------------ Cecilia Y. Sui
# Date last updated ---------------- Aug 25, 2021 
# 
# Description ---------------------- Using Twitter API (this program uses the academic track version) to scrape
# ---------------------------------- required data based on wustlpolisci twitter account. The program uses the
# ---------------------------------- twarc package. (See more details in Sources.)
# 
# Limitations ---------------------- 1. When there is a duplicated maximum value, the algorithm only takes the 
# ---------------------------------- first occurence. e.g. if there are 2 tied most popular accounts, only 1 will
# ---------------------------------- be recorded here.
# ---------------------------------- 2. It takes a very very long time to run due to the rate limit exceeded 
# ---------------------------------- issue with Twitter API.
# 
# Sources -------------------------- https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/tree/3872e319f7ecf7c09921b076bf2a81f631e67aa9/labs-code/python/academic-research-product-track
# Access keys and tokens ----------- Twarc only requires the bearer_token. I deleted it from the code for security
# ---------------------------------- reasons. Please let me know if you need it to grade the hw. I am happy to share
# ---------------------------------- it and change it later. Thanks!
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# Imports: 
# This will import the Twarc2 client and expansions class from twarc library and also the json library
# --------------------------------------------------------------------------------------------------------------
import re
from twarc import Twarc2, expansions


# --------------------------------------------------------------------------------------------------------------
# Initialize: 
# This is where you initialize the client with my bearer token (not provided in this code)
# --------------------------------------------------------------------------------------------------------------
bearer_token = "my-token" # Please let me know if you need this to grade the hw. I am happy to share it for this purpose.
client = Twarc2(bearer_token=bearer_token)

# --------------------------------------------------------------------------------------------------------------
# Define follower():
# This function finds all the followers of @WUSTLPoliSci and all of their followers, with the Twitter id, 
# username, number of followers (-1 if in the 2nd degree), and number of tweets.
# --------------------------------------------------------------------------------------------------------------
def follower():
    all_followers = [] # list of lists [[id, username, # of followers, # of tweets]]
    followers_followers = [] # list of lists [[id, username, -1, # of tweets]]
    # The followers function gets followers for specified user
    followers = client.followers(user="WUSTLPoliSci") # id = "2752940851"
    for page in followers: 
        result = expansions.flatten(page)
        # print(len(result)) # = 628
        # append results to list 
        [all_followers.append([user["id"], user["username"]]) for user in result]
    for i in all_followers:
        # The followers function gets followers for specified user
        followers = client.followers(user = i[1])
        for page in followers: 
            # The loop is only iterated once for each follower,
            # The try and except loop attempts to deal with the raise value error.
            try:
                result = expansions.flatten(page)
                i.append(len(result))  
                [followers_followers.append([user["id"], user["username"], -1, count_tweets(user["username"])]) for user in result]
            except:
                # The continue in the except part does not cause losing values, as long as the follower account is valid. 
                continue  
    # append the tweet counts to list
    [i.append(count_tweets(i[1])) for i in all_followers]

    
    l_id,l_username,l_followers,l_tweets = map(list, zip(*all_followers)) # separate to 4 individual lists
    # # most popular: max # of followers
    max_pop = all_followers[l_followers.index(max(l_followers))] # the most popular user
    # # most active: max # of tweets
    max_act = all_followers[l_tweets.index(max(l_tweets))] # the most active user

    # # Followers of followers: 
    total_followers = all_followers + followers_followers # append two lists together 
    l_id,l_username,l_followers,l_tweets = map(list, zip(*total_followers)) # separate to 4 individual lists
    # # most active of all:
    total_max_act = total_followers[l_tweets.index(max(l_tweets))] # the most active user of all (2 degree)

    return max_pop, max_act, total_max_act


# --------------------------------------------------------------------------------------------------------------
# Define following():
# This function finds all the friends (accounts following) of @WUSTLPoliSci and all of their friends, with the 
# Twitter id, username, number of followers (-1 if in the 2nd degree), and number of tweets.
# --------------------------------------------------------------------------------------------------------------
def following():
    all_friends = [] # list of lists [[id, username, # of followers, # of tweets]]
    friends_friends = [] # list of lists [[id, username, -1, # of tweets]]
    # The following function gets users that the specified user follows
    following = client.following(user="WUSTLPoliSci")
    for page in following: 
        result = expansions.flatten(page)
        # append the info to list 
        [all_friends.append([user["id"], user["username"]]) for user in result]
    for i in all_friends:
        # The followers function gets followers for specified user
        followers = client.followers(user = i[1])
        for page in followers: 
            # The loop is only iterated once for each follower,
            # The try and except loop attempts to deal with the raise value error.
            try:
                result = expansions.flatten(page)
                i.append(len(result))  
                [friends_friends.append([user["id"], user["username"], -1, count_tweets(user["username"])]) for user in result]
            except:
                # The continue in the except part does not cause losing values, as long as the follower account is valid. 
                continue 
    # append the tweet counts to list
    [i.append(count_tweets(i[1])) for i in all_friends]

    l_id,l_username,l_followers,l_tweets = map(list, zip(*all_friends)) # separate to 4 individual lists
    # most popular: max # of followers
    max_pop = all_friends[l_followers.index(max(l_followers))] # sub list of the most popular user

    # most active: max # of tweets --> layman, expert and celebrity
    layman = [i for i in all_friends if i[2]<100] # strickly less than 100
    expert = [i for i in all_friends if i[2]>=100 and i[2] < 1000]
    celebrity = [i for i in all_friends if i[2] >=1000] 
    l_id,l_username,l_followers,l_tweets = map(list, zip(*layman)) # separate to 4 individual lists
    max_layman = layman[l_tweets.index(max(l_tweets))] # the most active layman
    l_id,l_username,l_followers,l_tweets = map(list, zip(*expert)) # separate to 4 individual lists
    max_expert = expert[l_tweets.index(max(l_tweets))] # the most active expert
    l_id,l_username,l_followers,l_tweets = map(list, zip(*celebrity)) # separate to 4 individual lists
    max_celebrity = celebrity[l_tweets.index(max(l_tweets))] # the most active celebrity
    max_act = [max_layman,max_expert,max_celebrity]

    # Friends of friends 
    total_friends = all_friends + friends_friends # append 2 lists together in order
    l_id,l_username,l_followers,l_tweets = map(list, zip(*total_friends)) # separate to 4 individual lists
    # most active of all:
    total_max_act = total_friends[l_tweets.index(max(l_tweets))] # the most active user of all (2 degree)

    return max_pop, max_act, total_max_act


# --------------------------------------------------------------------------------------------------------------
# Define count_tweets():
# This function takes in a username (as a stirng) as the input parameter, and returns the total number of tweets
# by that Twitter account. The default is set to @WUSTLPoliSci. 
# --------------------------------------------------------------------------------------------------------------
def count_tweets(user="WUSTLPoliSci"):
    # grab all tweets from the twitter account user
    # The counts_all method call the full-archive Tweet counts endpoint to get Tweet volume based on the query
    count_results = client.counts_all(query=user) # python generator
    for i in count_results:
        total_tweets = i["meta"]["total_tweet_count"]
        # dict_keys(['data', 'meta', '__twarc'])
    return total_tweets


# --------------------------------------------------------------------------------------------------------------
# Main
# The print statments provide the answers to the homework prompts in the order that were asked. 
# --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # follower stats return 
    max_pop1f, max_act1f, total_max_act2f = follower()
    # following stats return
    max_pop1g, max_act1g, total_max_act2g = following()
    # nested lists: [[id, username, # of followers, # of tweets]]
    print("One degree of separation ---------------------------------------------------------------------------")
    print("\nAmong the followers of @WUSTLPoliSci : ")
    print("the most active user is: {} with id: {} with {} number of tweets.".format(max_act1f[1],max_act1f[0],max_act1f[3]))
    print("the most popular user is: {} with id: {} with {} number of followers.".format(max_pop1f[1],max_pop1f[0],max_pop1f[2]))

    print("\nAmong the friends of @WUSTLPoliSci: ")
    print("the most active layman is: {} with id: {} with {} number of tweets.".format(max_act1g[0][1],max_act1g[0][0],max_act1g[0][3]))
    print("the most active expert is: {} with id: {} with {} number of tweets.".format(max_act1g[1][1],max_act1g[1][0],max_act1g[1][3]))
    print("the most active celebrity is: {} with id: {} with {} number of tweets.".format(max_act1g[2][1],max_act1g[2][0],max_act1g[2][3]))
    print("the most popular user is: {} with id: {} with {} number of followers.".format(max_pop1g[1],max_pop1g[0],max_pop1g[2]))

    print("\nTwo degrees of separation ---------------------------------------------------------------------------")
    print("Among the followers of @WUSTLPoliSci and their followers: ")
    print("the most active user is: {} with id: {} with {} number of tweets.".format(total_max_act2f[1],total_max_act2f[0],total_max_act2f[3]))
    print("Among the friends of @WUSTLPoliSci and their friends: ")
    print("the most active user is: {} with id: {} with {} number of tweets.".format(total_max_act2g[1],total_max_act2g[0],total_max_act2g[3]))


