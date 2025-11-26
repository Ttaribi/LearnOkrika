# Learn Okrika - Flask Backend

Flask backend API for the Learn Okrika language learning website.

## Features

- 🔌 RESTful API endpoints
- 🌐 CORS support for frontend integration
- 📊 Statistics and lesson management
- 🎯 Ready for future database integration
- 🚀 Production-ready configuration

## Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Server

### Development Mode

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Production Mode

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### Health Check
- `GET /api/health` - Check API health status

### Statistics
- `GET /api/stats` - Get website statistics

### Lessons
- `GET /api/lessons` - Get all available lessons
- `GET /api/lessons/<id>` - Get a specific lesson

### About
- `GET /api/about` - Get information about the Okrika language

### Contact
- `POST /api/contact` - Submit contact form

## Project Structure

```
backend/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## Frontend Integration

### Development

In development, the React frontend runs on `http://localhost:5173` (Vite) and the Flask backend on `http://localhost:5000`. CORS is enabled to allow communication between them.

### Production

1. Build the React frontend:
```bash
cd ../frontend
npm run build
```

2. The Flask backend will automatically serve the built React app from the `/frontend/dist` directory.

## Future Enhancements

- Database integration (SQLAlchemy)
- User authentication and authorization
- Lesson progress tracking
- User profiles and achievements
- Audio file management for pronunciations
- Quiz and assessment system

## License

© 2024 Learn Okrika

