from pydantic import BaseModel

class User(BaseModel):
    id : int


user = User(id=4)

print(user.model_dump())
print(user.model_dump_json())

#  Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.
# Serialization
# -> converting pydantic models to dict / json / xml strings