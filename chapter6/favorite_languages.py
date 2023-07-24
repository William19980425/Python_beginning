favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    'eren':'rust'
}
print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is : '{language}'.")

print("====================================分割线====================================")

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
print("====================================分割线2====================================")    
for name in favorite_languages.keys():
    print(name.title())
 #遍历字典时，会默认遍历所有的key   
print("====================================分割线3====================================")    
for name in favorite_languages:
    print(name.title())    
print("====================================分割线4====================================")    
for language in favorite_languages.values():
    print(language.title())        

print("====================================分割线5====================================") 
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}")
        00
print("====================================分割线6====================================")         
if 'erin' not in favorite_languages.keys():
    print("erin,please take our poll")

print("====================================分割线7====================================")    
for language in set(favorite_languages.values()): #为剔除重复项，可使用集合set()
    print(language.title())

print("====================================分割线7====================================")    
favorite_languages = {
    'jen':['python','rust'],
    'sarah':['c'],
    'edward':['rust','go'],
    'phil':['python','haskell'],
    'eren':['rust','ruby']
}    
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"{language.title()}")