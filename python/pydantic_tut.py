from pydantic import BaseModel

class User(BaseModel):
    id : int 
    name : str
    section : str

user_info =  {'id' : 3 , 'name' : 'random' , 'section' : 'A'}


user = User(**user_info)
user2 = User(id = 12 , name ='swaraj' , section = 'B')

print(user.name)
print(user2.name)




