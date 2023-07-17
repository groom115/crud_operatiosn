import motor.motor_asyncio
from .models.manager import ManagerSchema


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Employees


# Create a collection and insert a document
# managers_collection = database.managers
managers_collection = database.get_collection("managers")


def manager_helper(manager) -> dict:
    return {
        "id": str(manager["_id"]),
        "name": manager["name"],
        "role": manager["role"],
        "age": manager["age"],
    }


async def retrieve_managers():
    managers = []
    async for manager in managers_collection.find():
        managers.append(ManagerSchema(manager))
    return managers


# Add a new student into to the database
async def add_manager(manager_data: dict) -> dict:
    print("aa")
    manager = await managers_collection.insert_one(manager_data)
    new_manager = await managers_collection.find_one({"_id": manager.inserted_id})
    return manager_helper(new_manager)


# Retrieve a student with a matching ID
async def retrieve_manager(id: str) -> dict:
    managers = await managers_collection.find_one({"_id": ObjectId(id)})
    if manager:
        return ManagerSchema(manager)


# Update a student with a matching ID
async def update_manager(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    manager = await managers_collection.find_one({"_id": ObjectId(id)})
    if manager:
        updated_manager = await managers_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_manager:
            return True
        return False


# Delete a student from the database
async def delete_manager(id: str):
    student = await managers_collection.find_one({"_id": ObjectId(id)})
    if manager:
        await managers_collection.delete_one({"_id": ObjectId(id)})
        return True
