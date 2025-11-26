# Environment Setup Guide

## Creating Environment Variables

Create a `.env` file in the `backend` directory with the following content:

```bash
# Flask Configuration
SECRET_KEY=your-secret-key-here-change-in-production
FLASK_ENV=development
FLASK_DEBUG=1

# Database Configuration (for future use)
# DATABASE_URL=sqlite:///learnokrika.db

# API Configuration
API_URL=http://localhost:5000
```

## Quick Setup Commands

### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## Running the Application

### Development Mode (Separate Servers)

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Production Mode (Flask serves React)

1. Build React:
```bash
cd frontend
npm run build
```

2. Run Flask:
```bash
cd backend
python app.py
```

Now Flask will serve both the API and the React app from `http://localhost:5000`

