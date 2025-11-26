import os
from pathlib import Path

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    BASE_DIR = Path(__file__).parent.parent
    FRONTEND_BUILD_DIR = BASE_DIR / 'frontend' / 'dist'
    
    # Database configuration (for future use)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///learnokrika.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API configuration
    API_PREFIX = '/api'
    
    # CORS configuration
    CORS_ORIGINS = ['http://localhost:5173', 'http://localhost:3000', 'http://localhost:5000']

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or None
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY must be set in production")

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

