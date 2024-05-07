from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    yt_host: str = os.getenv("YT_HOST", default="localhost")
    yt_port: int = int(os.getenv("YT_PORT", default=8080))
    yt_scheme: str = os.getenv("YT_SCHEME", default="https")
    yt_disable_ssl_certificate_validation: bool = bool(
        os.getenv("YT_DISABLE_SSL_CERTIFICATE_VALIDATION", default=True)
    )
    yt_auth: str = os.getenv("YT_AUTH", default="")
