prompt = input("Tell me something,and I will repeat it back to you:\n")
prompt="\nEnter 'quit' to end the program. "

# message = ""
# while message !='quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
active = True
while active:
    message = input(prompt)
    if message =='quit':
        active=False
    else:
        print(message)