import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import emails
from emails.template import JinjaTemplate
from jose import jwt

from app.core.config import settings


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {}
) -> None:
    assert settings.EMAILS_ENABLED, "No provided configuration for email variables"

    message = emails.Message(subject=JinjaTemplate(subject_template),
                             html=JinjaTemplate(html_template),
                             mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL)
                             )

    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    smtp_options["tls"] = settings.SMTP_TLS
    smtp_options["user"] = settings.SMTP_USER
    smtp_options["password"] = settings.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def send_reset_password_email(
    email_to: str,
    full_name: str,
    token: str
) -> None:
    subject = f"{settings.PROJECT_NAME} - Restablece tu contraseña"

    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html", encoding="utf-8") as f:
        template_str = f.read()

    link = f"{settings.CLIENT_HOST}/restablecer?token={token}"

    send_email(email_to=email_to,
               subject_template=subject,
               html_template=template_str,
               environment={"project_name": settings.PROJECT_NAME,
                            "full_name": full_name,
                            "valid_minutes": settings.EMAIL_RESET_TOKEN_EXPIRE_MINUTES,
                            "link": link
                            }
               )


def send_new_account_email(
    email_to: str,
    full_name: str
) -> None:
    subject = f"{settings.PROJECT_NAME} - Bienvenido(a)"

    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "new_account.html", encoding="utf-8") as f:
        template_str = f.read()

    send_email(email_to=email_to,
               subject_template=subject,
               html_template=template_str,
               environment={"project_name": settings.PROJECT_NAME, "full_name": full_name, "link": settings.CLIENT_HOST}
               )


def generate_password_reset_token(
    email: str
) -> str:
    expires_delta = timedelta(minutes=settings.EMAIL_RESET_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    encoded_jwt = jwt.encode({"exp": expire, "sub": str(email)}, settings.SECRET_KEY, algorithm="HS256")

    return encoded_jwt


def verify_password_reset_token(
    token: str
) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["sub"]
    except jwt.JWTError:
        return None
