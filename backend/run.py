#!/usr/bin/env python3
"""
Production-ready application runner
"""
from app import app

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug)

