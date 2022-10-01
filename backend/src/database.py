# modules
import json

# opening the files
activities_file = open("data/activities.json")
post_file       = open("data/post.json")
profiles_file   = open("data/profiles.json")

# loading the json
activities_json = json.load(activities_file)
post_json       = json.load(post_file)
profiles_json   = json.load(profiles_file)

# closing files
activities_file.close()
post_file.close()
profiles_file.close()

# All data

# get all activities
def getAllActivities():
    return activities_json["activities"]

# get all posts
def getAllPost():
    return post_json["posts"]

# get all profiles
def getAllProfiles():
    return profiles_json["profiles"]

# put an username and u get their data
def getProfileByUsername(username):
    for it_user in profiles_json["profiles"]:
        if it_user["username"] == username:
            return it_user
    return "Error my broda"
