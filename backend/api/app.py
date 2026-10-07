from fastapi import APIRouter

from mcp_server import storage as db
from schema import Application, RewrittenResume
from process.match_score_resume import match_score_resume   
from process.gated_agent import gated_agent_check,gated_agent_resume    
router = APIRouter()


@router.get("/applications")
def list_applications() -> list[Application]:
    """Endpoint to list all job applications."""
    return db.list_all_applications()


@router.post("/applications")
def add_application(application: Application) -> Application:
    """Endpoint to add a new job application."""
    return db.create_application(application=application)

@router.post("/match-analysis")
def analyze_match(request: dict) -> dict:
    """Endpoint to analyze the match between a resume and a job description."""
    match_result =  match_score_resume(request["resume_text"], request["job_description"])

    thread_id = gated_agent_check(request["resume_text"], request["job_description"])
    return {"match_result": match_result.model_dump(), "thread_id": thread_id}

@router.post("/approve-tailoring")
def approve_tailoring(request: dict) -> RewrittenResume:
    """Endpoint to approve the tailoring of a resume."""
    print("Tailoring approved for thread_id:", request)
    response =  gated_agent_resume(request["thread_id"], request["decision"])
    print(response)
    return response 


@router.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}
