# FastMCP Python Server: Internet Browsing

## Features

- Fetch HTML from any URL
- Optional keyword search in page text

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python server.py
```
Server runs on port 8000.

## Example Usage

POST to `http://localhost:8000/command/browse` with JSON:

```json
{
  "url": "https://www.example.com",
  "keyword": "example"
}
```
- `"keyword"` is optional.

## Response

- If no keyword: returns page HTML.
- If keyword: returns HTML, keyword count, and matching sentences.