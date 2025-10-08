from fastapi import FastAPI, Cookie, Response, HTTPException

app = FastAPI()

@app.get("/set_cookie")
async def set_cookie(response : Response):
    #  IMPOSTA UN COOKIE CON NOME 'user_id' e valore '12345'
    response.set_cookie(key="user_id", value="12345")
    return {"message": "Cookie 'user_id' set successfully!"}

@app.get("/get_cookie")
async def get_cookie(user_id: str = Cookie(None)):
    if user_id:
        return {"message": f"Cookie 'user_id' value is: {user_id}"}
    else:
        raise HTTPException(status_code=400, detail="Cookie 'user_id' not found")