# run.py

import threading
import uvicorn
from main import flask_app, fastapi_app  # <- ICI on importe depuis main.py

def run_flask():
    flask_app.run(host="127.0.0.1", port=5000, debug=True)

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_fastapi()
