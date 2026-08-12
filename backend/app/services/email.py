"""
Outbound email for verification/reset links. stdlib smtplib only - no new
network dependency needed.

SMTP_HOST unset (the default, zero-config dev state) means "don't actually
send" - the email is logged instead, so the verification/reset flows are
fully testable locally without any SMTP setup. Set SMTP_HOST (and the rest
of the SMTP_* vars in .env, see .env.example) to send for real.
"""
import logging
import os
import smtplib
from email.message import EmailMessage

logger = logging.getLogger("guided_learning.email")


def send_email(to: str, subject: str, html: str) -> None:
    host = os.environ.get("SMTP_HOST")
    if not host:
        logger.info("SMTP_HOST not configured - logging email instead of sending.\nTo: %s\nSubject: %s\n%s",
                     to, subject, html)
        return

    port = int(os.environ.get("SMTP_PORT", "587"))
    username = os.environ.get("SMTP_USERNAME")
    app_password = os.environ.get("SMTP_APP_PASSWORD")
    from_address = os.environ.get("SMTP_FROM_ADDRESS", username)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_address
    msg["To"] = to
    msg.set_content("This email requires an HTML-capable client to view.")
    msg.add_alternative(html, subtype="html")

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        if username and app_password:
            server.login(username, app_password)
        server.send_message(msg)
