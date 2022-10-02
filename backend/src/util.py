from random import randint

def getRandomActivity(activities):
    return activities[randint(0, len(activities)-1)]

def getAvailableActivities(all_activities, used_activities):
    response = []

    for act in all_activities:
        found = False

        for used in used_activities:
            if used == act:
                found = True
                break
        if not found:
            response.append(act)

    # If the activities end, just start again with all activities
    if len(response) == 0:
        return all_activities

    return response