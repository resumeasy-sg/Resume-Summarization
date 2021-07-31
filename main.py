from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
from resumeasy import extract_email
from resumeasy import extract_skills
from resumeasy import preprocessing
from resumeasy import delimiter_removal
from skillsapi import skills_list_extraction
from resumeasy import mobile_number_extraction
from resumeasy import ner_extraction
from tika import parser

app = FastAPI()

class User(BaseModel):
    user_name: dict

@app.post("/files/")
def create_upload_files(resume: str = Form(...)):
    resume= preprocessing(resume)
    resume= delimiter_removal(resume)
    #return ner_extraction(resume)
    return {"Email": extract_email(resume),"Mobile Number": mobile_number_extraction(resume),"skills":extract_skills(resume)}




@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="resume" type="text">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)