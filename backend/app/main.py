from fastapi import FastAPI
from app.controllers.auth_controller import auth_router
from app.controllers.sms_controller import sms_router
from app.controllers.country_operator_controller import country_operator_router

app = FastAPI(
    title="Dynamic SMS Management System",
    description="A web-based dashboard for managing and monitoring SMS programs.",
    version="1.0.0"
)

# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(sms_router, prefix="/sms", tags=["SMS Management"])
app.include_router(country_operator_router, prefix="/country-operator", tags=["Country Operator Management"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the SMS Management API"}
