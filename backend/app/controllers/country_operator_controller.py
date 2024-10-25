from fastapi import APIRouter
from app.models.country_operator_model import add_country_operator, update_country_operator, delete_country_operator

country_operator_router = APIRouter()

@country_operator_router.post("/add")
def add_operator(country: str, operator: str, high_priority: bool = False):
    return add_country_operator(country, operator, high_priority)

@country_operator_router.put("/update/{country}/{operator}")
def update_operator_status(country: str, operator: str, status: str):
    return update_country_operator(country, operator, status)

@country_operator_router.delete("/delete/{country}/{operator}")
def delete_operator(country: str, operator: str):
    return delete_country_operator(country, operator)
