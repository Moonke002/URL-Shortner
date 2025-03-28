# URL Shortener

A simple URL shortener application built with Flask that allows you to create short URLs from long ones.

## Features

- Convert long URLs to short, memorable ones
- Modern, responsive UI
- One-click copy to clipboard
- Automatic redirection to original URLs
- In-memory URL storage (resets on server restart)

## Setup

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a long URL in the input field
2. Click "Shorten URL"
3. Copy the shortened URL using the "Copy" button
4. Share the shortened URL with others

## Technical Details

- Built with Flask
- Uses MD5 hashing for URL shortening
- In-memory storage (URLs are not persisted between server restarts)
- Modern UI with responsive design 