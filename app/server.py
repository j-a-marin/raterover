from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from langserve import add_routes
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# Edit this to add other chains
# add_routes(app, NotImplemented)

from rag_chroma import chain as rag_chroma_chain
add_routes(app, rag_chroma_chain, path="/rag-chroma")

# This class should match the structure of the request JSON body
class Question(BaseModel):
    text: str

@app.post("/ask")
def ask(question: Question):
    try:
        # Use the chain to get a response to the question
        # with the question text passed as a string, not as a dictionary
        answer = rag_chroma_chain.run(question.__root__)
        return {"answer": answer}
    except Exception as e:
        # Log the exception for debugging purposes
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.run(app, host="127.0.0.1", port=8000)

