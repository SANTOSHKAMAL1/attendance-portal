"""Vercel serverless entrypoint.

Vercel builds each file under api/ into its own function. We expose the
existing Flask app as `app`; the Python runtime speaks WSGI, so no adapter
is needed. vercel.json rewrites every incoming path here, which keeps all
routing decisions inside Flask exactly as they are locally.
"""
import os
import sys

# app.py, config.py, templates/ and static/ live one level up.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402  (path shim has to run first)

__all__ = ["app"]
