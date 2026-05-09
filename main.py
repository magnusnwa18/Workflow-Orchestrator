from fastapi import FastAPI

app = FastAPI(title='Workflow Orchestrator')

@app.get('/')
def root():
    return {'message': 'Workflow Orchestrator running - Secure PII pipelines active'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)