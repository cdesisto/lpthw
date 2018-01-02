from sys import argv

script, user_name = argv
# Reset the propt to include f text
prompt = (f"{user_name}>>")

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
# Using the same value for prompt each time
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
An you have a {computer} computer. Nice
""")
