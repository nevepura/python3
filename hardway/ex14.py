from sys import argv

script, uname = argv
prompt = '8===D - -  '
print(f"Hi {uname}, this is the {script} script")
print('I\'ll ask some questions')
print(f"do you like me {uname}?")
likes= input(prompt)

print("where do u live?")
lives = input (prompt)

print ("any gf?")
gf = input(prompt)
	
if gf == 'yes' or gf == 'Yes':
	answer = 'do'
else:
	answer = 'don\'t'

print(f"""
aight, so you said {likes} about liking me, 
you live in {lives}
and you {answer} have a gf. Thanks!
""")