import strawberry
from models.user import User
from typing import List

@strawberry.type
class UserType:
    id: int
    name: str
    address: str
    phone_number: str
    gender: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, address: str, phone_number: str, gender: str) -> UserType:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        user = User()
        user.name = name
        user.address = address
        user.phone_number = phone_number
        user.gender = gender
        user.save()
        print(user.id)
        print(user.name)
        return user

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> List[UserType]:
        return User.all()


schema = strawberry.Schema(query=Query)