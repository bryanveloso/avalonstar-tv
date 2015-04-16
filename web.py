#!/usr/bin/env python
import os

from avalonstar import wsgi
from waitress import serve


PORT = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    serve(wsgi.application, port=PORT)
