# Home Harmony Full API

This project provides a FastAPI application with three core features:
1. **Image Search**
2. **Text-Based Search**
3. **Designer Matchmaking**

## Setup

1. Navigate to the project directory:
   ```
   cd home_harmony_full_api
   ```

2. (Optional) Create and activate a virtual environment:
   - **Unix/macOS**:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows**:
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running

Start the server:
```
uvicorn main:app --reload --port 8000
```

The API docs will be available at:
```
http://127.0.0.1:8000/docs
```

## Endpoints

- **GET /**  
  Health check; returns a welcome message.

- **POST /search/image**  
  Upload form file `file` (an image).  
  Returns JSON:
  ```json
  {
    "filename": "<uploaded_filename>",
    "results": ["<dummy_result>"]
  }
  ```

- **POST /search/text**  
  Form field `query` (string).  
  Returns JSON:
  ```json
  {
    "query": "<your_query>",
    "results": ["Product matching ... #1", "Product matching ... #2"]
  }
  ```

- **POST /match**  
  Form fields:
  - `style` (string)
  - `budget` (string)

  Returns JSON:
  ```json
  {
    "matched_designers": [
      {"name": "Alice", ...},
      {"name": "Bob", ...}
    ]
  }
  ```
