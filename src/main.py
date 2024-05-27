import uvicorn
from auth.auth import auth

if __name__ == "__main__":
    uvicorn.run("auth.auth:auth", host="127.0.0.1", port=8000, reload=True)
