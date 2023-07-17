from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..database import add_manager

from ..models.manager import responseModel, ManagerSchema, UpdateManagerSchema

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_manager_data(manager: ManagerSchema):
    manager = jsonable_encoder(manager)
    new_manager = await add_manager(manager)
    return responseModel(new_manager, "manager added")
