from fastapi import FastAPI

from API import api_endpoints

app = FastAPI()
app.include_router(api_endpoints)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
    #uvicorn.run(app, host="127.0.0.1", port=3307, log_level="info")