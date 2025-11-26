# Learn Okrika - Language Learning Platform

A modern, full-stack language learning website for the Okrika language from Rivers State, Nigeria.

## 🏗️ Project Structure

```
learnOkrika/
├── frontend/          # React + Vite frontend
├── backend/           # Flask Python backend
└── README.md          # This file
```

## 🚀 Quick Start

### Frontend (React)

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

### Backend (Flask)

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start Flask server:
```bash
python app.py
```

Backend API will be available at `http://localhost:5001`

## 📡 API Endpoints

The Flask backend provides the following API endpoints:

- `GET /api/health` - Health check
- `GET /api/stats` - Website statistics
- `GET /api/lessons` - Get all lessons (supports `?level=beginner&category=greetings`)
- `GET /api/lessons/<id>` - Get specific lesson
- `GET /api/about` - Information about Okrika language
- `POST /api/contact` - Submit contact form

## 🛠️ Development

### Running Both Frontend and Backend

**Terminal 1 - Frontend:**
```bash
cd frontend
npm run dev
```

**Terminal 2 - Backend:**
```bash
cd backend
source venv/bin/activate  # if using venv
python app.py
```

### Production Build

1. Build React frontend:
```bash
cd frontend
npm run build
```

2. Run Flask backend (it will serve the built frontend):
```bash
cd backend
python app.py
```

The Flask app will automatically serve the React build from `frontend/dist`.

## 📦 Technologies

### Frontend
- React 18
- Vite
- Modern CSS with animations

### Backend
- Flask 3.0
- Flask-CORS
- Python 3.8+

## 🎯 Features

- ✨ Modern, responsive landing page
- 🎨 Smooth animations and transitions
- 📱 Mobile-friendly design
- 🔌 RESTful API backend
- 🌐 CORS support for development
- 🚀 Production-ready configuration

## 📝 Future Enhancements

- User authentication
- Lesson progress tracking
- Database integration
- Audio pronunciation files
- Interactive quizzes
- User profiles and achievements

## 📄 License

© 2025 Learn Okrika

