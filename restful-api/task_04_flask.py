#!/usr/bin/python3
"""
Simple Flask API
Endpoints:
- /              → Welcome message
- /data          → Returns list of usernames
- /status        → Returns API status
- /users/<username> → Returns user object or 404 if not found
- /add_user      → POST endpoint to add a new user
"""
