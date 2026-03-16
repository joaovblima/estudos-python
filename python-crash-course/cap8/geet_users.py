def greet_users(names):
    """
    greet all the users with a simple message 
    """
    for name in names:
        print("Hello", name.title(), "welcome!")


users = ["joao", "alice", "ingrid", "sofia"]

greet_users(users)
