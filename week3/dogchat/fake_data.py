# forshadowing
# replace for next week




dogs = [
    {
        "name" : "Marko",
        "handle" : "marko",
        "bio" : "I'ma good dog :))"
    },
    {
        "name" : "Shaggy",
        "handle" : "shagman",
        "bio" : "I REALLY LOVE Butter <3"
    },
    {
        "name" : "Chewie",
        "handle" : "chewie",
        "bio" : "I'm the best, i'm the best."
    }
]

posts = {
    ("marko", "IT's DINNER TIME :)))))"),
    ("marko", "I don't want to go to bed >:("),
    ("chewie", "@shaggy took my bed. you better watch OUT"),
    ("shagman", "I learned how to sit today, AGAIN")
}

def get_dog_by_handle(handle):
    for dog in dogs:
        if dog["handle"] == handle:
            return dog

    return None

def get_user_posts(handle):
    dogs_posts = []
    for post in posts:
        if post[0] == handle:
            dogs_posts.append(post)
    return dogs_posts
