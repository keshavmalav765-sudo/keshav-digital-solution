"""
Development server runner
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment
os.environ['FLASK_APP'] = 'app.py'
os.environ['FLASK_ENV'] = 'development'

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
    