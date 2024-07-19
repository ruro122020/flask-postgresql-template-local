
#!/usr/bin/env python3

# Local imports
from config import app
# Add your model imports
from routes import *
from models import *

if __name__ == '__main__':
    app.run(port=5555, debug=True)
