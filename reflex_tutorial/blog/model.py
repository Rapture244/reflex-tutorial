from datetime import datetime
import reflex as rx

import sqlalchemy
from sqlmodel import Field

from .. import utils

class BlogPostModel(rx.Model, table=True):
    # user
    title: str
    content: str
    created_at: datetime= Field(
        default_factory = utils.timing.get_utc_now,
        sa_type = sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs = {
            'server_default' : sqlalchemy.func.now()
            },
        nullable=False
        )
    updated_at: datetime= Field(
        default_factory = utils.timing.get_utc_now,
        sa_type = sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs = {
            'onupdate' : sqlalchemy.func.now(),
            'server_default' : sqlalchemy.func.now()
            },
        nullable=False
        )
    # publish_date
    # publish_time