import motor.motor_asyncio
from app.server.models.manager.py import ManagerSchema


MONGO_DETAILS = "mongodb://localhost:27017"


base = client.Employees


# Create a collection and insert a document
collection = database.managers
managers_collection = database.get_collection("managers")


async def retrieve_students():
    managers = []
    async for managers in managers_collection.find():
        managers.append(ManagerSchema(student))
    return managers


# Add a new student into to the database
async def add_manager(manager_data: dict) -> dict:
    manager = await manager_collection.insert_one(manager_data)
    new_manager = await manager_collection.find_one({"_id": manager.inserted_id})
    return ManagerSchema(new_manager)


# Retrieve a student with a matching ID
async def retrieve_manager(id: str) -> dict:
    managers = await manager_collection.find_one({"_id": ObjectId(id)})
    if manager:
        return ManagerSchema(student)


# Update a student with a matching ID
async def update_manager(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    manager = await student_collection.find_one({"_id": ObjectId(id)})
    if manager:
        updated_manager = await manager_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_manager:
            return True
        return False


# Delete a student from the database
async def delete_manager(id: str):
    student = await manager_collection.find_one({"_id": ObjectId(id)})
    if manager:
        await manager_collection.delete_one({"_id": ObjectId(id)})
        return True
