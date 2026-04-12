from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from log_parser import extract_issues
from ai_engine import analyze_errors

app = FastAPI()

# CORS (for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Log Analyzer Backend Running"}


@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    try:
        content = await file.read()
        log_text = content.decode("utf-8", errors="ignore")

        issues = extract_issues(log_text)

        # Only call AI if errors exist
        if issues["errors"]:
            try:
                ai_analysis = analyze_errors(issues["errors"])
            except Exception:
                ai_analysis = "AI analysis failed. Make sure Ollama is running."
        else:
            ai_analysis = "No critical errors found."

        return {
            "filename": file.filename,
            "issues": issues,
            "analysis": ai_analysis
        }

    except Exception as e:
        return {
            "error": str(e)
        }