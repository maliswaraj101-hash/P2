from fastapi import FastAPI
from queues.worker import process_query 
from client.rq_client import queue

app = FastAPI()

@app.get("/health")
def health_check():
    return {"health" : "Working correctly"}

@app.post("/chat")
def chat(query : str):
    
    job = queue.enqueue(process_query , query)

    return {"status" : "queued" , "job_id" : job.id}


@app.get("/result")
def get_result(job_id : str):

    job = queue.fetch_job(job_id = job_id)
    result = job.return_value()
    # or job.result

    return {"result" : result}




# {
#   "status": "queued",
#   "job_id": "fab0f8de-6e7c-4e08-90f3-acbcf4c66756"
# }



# in both cases, query: str is just a parameter—but where FastAPI gets it from depends on the HTTP method and how you declare it.

# 1. @app.post("/chat")
# @app.post("/chat")
# def chat(query: str):

# Here, query is NOT automatically the request body. By default, FastAPI treats simple types (str, int, etc.) as query parameters, even in POST requests.

# So this expects:

# POST /chat?query=hello

# If you want it from the request body, you need to explicitly tell FastAPI:

# from fastapi import Body

# @app.post("/chat")
# def chat(query: str = Body(...)):

# Or better (common practice), use a Pydantic model:

# from pydantic import BaseModel

# class ChatRequest(BaseModel):
#     query: str

# @app.post("/chat")
# def chat(req: ChatRequest):
#     return {"message": req.query}
# 2. @app.get("/chat")
# @app.get("/chat")
# def chat(query: str):

# Here, query is always a query parameter, because GET requests don’t have a body in typical usage.

# So it expects:

# GET /chat?query=hello
# Key difference
# GET: parameters → query string
# POST: parameters → query string by default, unless you explicitly use Body or a model
# Quick rule of thumb
# Simple types (str, int) → query params
# Pydantic models → request body