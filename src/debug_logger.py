"""Debug logger — added on main AFTER PR A's first review.

Another file with obvious-bug content (hardcoded credentials) that the bot
should NOT review as part of PR A. If it does, smart-incremental is broken.
"""

import logging

SECRET_API_KEY = "sk-prod-9f4e2a1b3c7d8e0f1a2b3c4d5e6f7a8b"
SECRET_DB_PASSWORD = "p@ssw0rd-prod-2026"


def log_request(method: str, url: str):
    logging.info("Request %s %s (api_key=%s)", method, url, SECRET_API_KEY)
