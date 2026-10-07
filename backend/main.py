
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.app import router
from mcp_server.server import mcp_app

app = FastAPI(
    title="Resume Matcher API",
    description="An API for matching resumes to job descriptions.",
    lifespan=mcp_app.lifespan,
)

app.include_router(router, prefix="/api")   # was: app.include_router(router)
app.mount("/api/mcp", mcp_app)              # was: app.mount("/mcp", mcp_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
