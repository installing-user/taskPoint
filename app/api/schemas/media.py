from typing import Optional
from pydantic import BaseModel


class ChatPhoto(BaseModel):
    small_file_id: Optional[str]
    small_file_unique_id: Optional[str]
    big_file_id: Optional[str]
    big_file_unique_id: Optional[str]


class PhotoSize(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    width: Optional[int]
    height: Optional[int]
    file_size: Optional[int]


class Audio(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    duration: Optional[int]
    performer: Optional[str]
    title: Optional[str]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
    thumb: Optional[PhotoSize]


class Document(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    thumb: Optional[PhotoSize]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]


class Video(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    thumb: Optional[PhotoSize]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]


class VideoNote(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    length: Optional[int]
    duration: Optional[int]
    thumb: Optional[PhotoSize]
    file_size: Optional[int]


class Voice(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    duration: Optional[int]
    mime_type: Optional[str]
    file_size: Optional[int]


class File(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    file_size: Optional[int]
    file_path: Optional[str]


class MaskPosition(BaseModel):
    point: Optional[str]
    x_shift: Optional[float]
    y_shift: Optional[float]
    scale: Optional[float]


class Sticker(BaseModel):
    file_id: Optional[str]
    file_unique_id: Optional[str]
    type: Optional[str]
    width: Optional[int]
    height: Optional[int]
    is_animated: Optional[bool]
    is_video: Optional[bool]
    thumb: Optional[PhotoSize]
    emoji: Optional[str]
    set_name: Optional[str]
    premium_animation: Optional[File]
    mask_position: Optional[MaskPosition]
    custom_emoji_id: Optional[str]
    file_size: Optional[int]