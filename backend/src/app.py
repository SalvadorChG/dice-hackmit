from flask import Flask, jsonify
import database

app = Flask(__name__)

class Activity:
    def __init__(self, 
        id, 
        name, 
        photo, 
        address, 
        map_link, 
        category, 
        description, 
        rating, 
        sustainability, 
        family_owned, 
        lifestyle
    ):
        self.id = id
        self.name = name
        self.photo = photo
        self.address = address
        self.map_link = map_link
        self.category = category
        self.description = description
        self.rating = rating
        self.sustainability = sustainability,
        self.family_owned = family_owned,
        self.lifestyle = lifestyle

    def sameCategory(self, other_category):
        if other_category == self.category:
            return True
        return False
    
    def sameActivity(self, other_id):
        if self.id == other_id:
            return True
        return False

    def getDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "photo": self.photo,
            "address": self.address,
            "map_link": self.map_link,
            "category": self.category,
            "description": self.description,
            "rating": self.rating,
            "sustainability": self.sustainability,
            "family-owned": self.family_owned,
            "lifestyle": self.lifestyle
        }

    def getID(self):
        return self.id

used = []
all_activities = []

all_activities_json = database.getAllActivities()

for x in all_activities_json:
    
    """
     id
     name
     photo
     address
     map_link
     category
     description
     rating
     sustainability
     family_owned
    lifestyle
    """
    if x["description"] == None:
        print("idk", x["id"])
    acti = Activity(
        x["id"],
        x["name"],
        x["photo"],
        x["address"],
        x["map_link"],
        x["category"],
        x["description"],
        x["rating"],
        x["sustainability"],
        x["family-owned"],
        x["lifestyle"]
    )

    all_activities.append(acti)

def getNotUsedFromCategory(category):
    for x in all_activities:
        already_used = False
        for y in used:
            if x.sameActivity(y):
                already_used = True
                break

        if not already_used and x.sameCategory(category):
            return x
    return False

# This function should be returning a list of four activities
def getActivities():
    dining = getNotUsedFromCategory("dining")
    shopping = getNotUsedFromCategory("shopping")
    outdoors = getNotUsedFromCategory("outdoors")
    community = getNotUsedFromCategory("community")

    return [dining, shopping, outdoors, community]

@app.route("/dicing")
def userData():
    activities = getActivities()
    god_list = []
    for acti in activities:
        god_list.append(acti.getDict())
    return jsonify({
        "activities": god_list
    })

app.run(port=3000)
