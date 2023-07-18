from typing import Optional
from pydantic import BaseModel, Field
from .media import (
    ChatPhoto, Audio, Voice, Video,
    VideoNote, PhotoSize, Document, Sticker
)


class Chat(BaseModel):
    id: Optional[int]
    type: Optional[str]
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    photo: Optional[ChatPhoto]
    bio: Optional[str]
    has_private_forwards: Optional[bool]


class ReplyMessage(BaseModel):
    date: Optional[int]
    chat: Optional[Chat]
    message_id: Optional[int]
    text: Optional[str]


class Message(BaseModel):
    message_id: Optional[int]
    from_field: Optional[User] = Field(alias="form")
    sender_chat: Optional[Chat]
    date: Optional[int]
    chat: Optional[Chat]
    forward_from: Optional[User]
    forward_from_chat: Optional[Chat]
    forward_from_message_id: Optional[int]
    forward_signature: Optional[str]
    forward_sender_name: Optional[str]
    forward_date: Optional[int]
    is_automatic_forward: Optional[bool]
    reply_to_message: Optional[ReplyMessage]
    text: Optional[str]
    audio: Optional[Audio]
    document: Optional[Document]
    photo: Optional[list[PhotoSize]]
    sticker: Optional[Sticker]
    video: Optional[Video]
    video_note: Optional[VideoNote]
    voice: Optional[Voice]
    caption: Optional[str]


class MessageBodyModel(BaseModel):
    update_id: Optional[int]
    message: Optional[Message]
