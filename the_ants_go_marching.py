# the_ants_go_marching.py

def unique_part(number, activity):
    print(f"The ants go marching {number} by {number}, hurrah! hurrah!")
    print(f"The ants go marching {number} by {number}, hurrah! hurrah!")
    print(f"The ants go marching {number} by {number},")
    print(f"The little one stops to {activity},")

def repeated_part():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!\n")

def sing_verse(number, activity):
    unique_part(number, activity)
    repeated_part()
    
activities = ["suck his thumb", "tie his shoe", "climb a tree", "lay on the floor", "dance a jive", 
            "throw a stick", "dial it up to eleven", "hit a mate", "look at a pine", "write with a pen"]

def main():
    for i in range(len(activities)):
        sing_verse(i+1, activities[i])

main()
