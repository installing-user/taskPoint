from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    is_bot: Optional[bool]
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]
    is_premium: Optional[bool]
    added_to_attachment_menu: Optional[bool]
    can_join_groups: Optional[bool]
    can_read_all_group_message: Optional[bool]
    supports_inline_queries: Optional[bool]
