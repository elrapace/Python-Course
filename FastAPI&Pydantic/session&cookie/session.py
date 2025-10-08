from fastapi import FastAPI, Cookie, Response, HTTPException

app = FastAPI()

#  DIZIONARIO PER SIMULARE LA SESSIONE (IN REALTÀ SAREBBE DATABASE O CACHE)
sessions = {}

@app.get("/login")
async def login(response : Response):
    # CREAZIONE ID SESSIONE
    session_id = str('12345')

    # SALVA LA SESSIONE IN UN DIZIONARIO
    sessions[session_id] = {'username' : 'admin', 'role' : 'admin'}

    # IMPOSTA UN COOKIE 'session_id' NEL BROWSER
    response.set_cookie(key='session_id', value=session_id)

    return {'message' : 'Login successful!'}

@app.get("/profile")
async def profile(session_id: str = Cookie(None)):
    if session_id is None or session_id not in sessions:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    
    # Recupera i dati della sessione usando il session_id
    user_data = sessions[session_id]
    return {"message": f"Welcome {user_data['username']} to your profile!", "role": user_data['role']}

@app.get("/logout")
async def logout(session_id: str = Cookie(None), response: Response):
    if session_id in sessions:
        del sessions[session_id]  # Rimuovi la sessione dal dizionario
    response.delete_cookie("session_id")  # Elimina il cookie 'session_id'
    
    return {"message": "Logged out successfully"}