from fastapi import APIRouter, HTTPException
from app.services.sms_service import start_session, stop_session, restart_session
from app.models.sms_model import get_sms_metrics

sms_router = APIRouter()

@sms_router.post("/start/{session_name}")
def start_sms_session(session_name: str):
    success = start_session(session_name)
    if success:
        return {"message": f"Started session: {session_name}"}
    raise HTTPException(status_code=400, detail="Failed to start session")

@sms_router.post("/stop/{session_name}")
def stop_sms_session(session_name: str):
    success = stop_session(session_name)
    if success:
        return {"message": f"Stopped session: {session_name}"}
    raise HTTPException(status_code=400, detail="Failed to stop session")

@sms_router.post("/restart/{session_name}")
def restart_sms_session(session_name: str):
    success = restart_session(session_name)
    if success:
        return {"message": f"Restarted session: {session_name}"}
    raise HTTPException(status_code=400, detail="Failed to restart session")

@sms_router.get("/metrics/{country}/{operator}")
def get_sms_metrics_endpoint(country: str, operator: str):
    metrics = get_sms_metrics(country, operator)
    if metrics:
        return metrics
    raise HTTPException(status_code=404, detail="Metrics not found")
