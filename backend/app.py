from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
from pathlib import Path
from routes.api import api_bp

app = Flask(__name__, static_folder=None)
CORS(app)  # Enable CORS for development

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Register blueprints
app.register_blueprint(api_bp)

# Get the project root directory
BASE_DIR = Path(__file__).parent.parent
FRONTEND_BUILD_DIR = BASE_DIR / 'frontend' / 'dist'

# Serve React app in production
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    """Serve the React frontend"""
    if FRONTEND_BUILD_DIR.exists():
        if path and os.path.exists(os.path.join(FRONTEND_BUILD_DIR, path)):
            return send_from_directory(FRONTEND_BUILD_DIR, path)
        else:
            return send_from_directory(FRONTEND_BUILD_DIR, 'index.html')
    else:
        return jsonify({
            'message': 'Frontend not built. Run "npm run build" in the frontend directory.',
            'api_endpoints': {
                'health': '/api/health',
                'stats': '/api/stats',
                'lessons': '/api/lessons',
                'about': '/api/about'
            }
        }), 200

if __name__ == '__main__':
    # Development server
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

