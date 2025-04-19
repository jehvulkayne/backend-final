import os
import uvicorn
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List, Optional
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiphrodite.crew import MyProjectCrew

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Temporary in-memory job store
jobs = {}

# Pydantic Models
class KeyValuePair(BaseModel):
    key: str
    value: str

class StartJobRequest(BaseModel):
    text: str

class ProvideInputRequest(BaseModel):
    job_id: str

@app.post("/start_job")
async def start_job(request_body: StartJobRequest):
    job_id = str(uuid.uuid4())
    payment_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "running",
        "payment_id": payment_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_data": request_body.text,
        "result": None
    }

    crew = MyProjectCrew()
    inputs = {"text": request_body.text}
    result = crew.crew().kickoff()

    jobs[job_id]["status"] = "completed"
    jobs[job_id]["result"] = result

    return {
        "status": "success",
        "job_id": job_id,
        "payment_id": payment_id
    }

@app.get("/status")
async def check_status(job_id: str = Query(..., description="Job ID to check status")):
    if job_id not in jobs:
        return {"error": "Job not found"}
    job = jobs[job_id]
    return {
        "job_id": job_id,
        "status": job["status"],
        "result": job["result"]
    }

@app.post("/provide_input")
async def provide_input(request_body: ProvideInputRequest):
    job_id = request_body.job_id
    if job_id not in jobs:
        return {"status": "error", "message": "Job not found"}
    return {"status": "success"}

@app.get("/availability")
async def check_availability():
    return {
        "status": "available",
        "message": "The server is running smoothly."
    }

@app.get("/input_schema")
async def input_schema():
    schema_example = {
        "input_data": [
            {"key": "text", "value": "string"}
        ]
    }
    return schema_example

def main():
    crew = MyProjectCrew()
    inputs = {"text": "Simulated user session"}
    result = crew.crew().kickoff()
    print("\nCrew Output:\n", result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        print("Starting FastAPI server...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        main()
