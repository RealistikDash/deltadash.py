from __future__ import annotations

from deltadash import parser
from deltadash.maps.note import Note
from dataclasses import dataclass

@dataclass
class Difficulty:
    # Song Metadata
    artist: str
    title: str
    name: str
    mapper: str

    # Map Metadata
    preview_ms: int
    background_path: str
    thumbnail_path: str
    audio_path: str

    id: int
    set_id: int

    # Difficulty Settings
    speed: float
    health: float
    sensitivity: float

    # Difficulty contents
    notes: list[Note]

    # Events
    ...

    @staticmethod
    def from_str(string: str) -> Difficulty:
        """Parses a string of a `.dd` file's contents into a `Difficulty` object."""

        sections = parser.ini.parse(string)

        # Song Metadata
        artist = sections["Metadata"]["Artist"]
        title = sections["Metadata"]["Title"]
        name = sections["Metadata"]["DiffName"]
        mapper = sections["Metadata"]["Mapper"]

        # Map Metadata
        preview_ms = int(sections["Metadata"]["PreviewPoint"])
        background_path = sections["Metadata"]["Background"]
        thumbnail_path = sections["Metadata"]["Thumbnail"]
        audio_path = sections["Metadata"]["Audio"]

        id = int(sections["Metadata"]["BeatmapID"])
        set_id = int(sections["Metadata"]["BeatmapsetID"])

        # Difficulty Settings
        speed = float(sections["Difficulty"]["Speed"])
        health = float(sections["Difficulty"]["Health"])
        sensitivity = float(sections["Difficulty"]["Sensitivity"])

        # This is a bit cursed but required if we want to use an ini parser.
        # In this case, the dictionary keys are the note string we are lookign
        # for, and the values are empty.
        notes = [
            Note.from_str(note) for note in sections["HitObjects"]
        ]

        return Difficulty(
            artist,
            title,
            name,
            mapper,
            preview_ms,
            background_path,
            thumbnail_path,
            audio_path,
            id,
            set_id,
            speed,
            health,
            sensitivity,
            notes,
        )
    
    @staticmethod
    def from_file(path: str) -> Difficulty:
        """Parses a `.dd` file into a `Difficulty` object.
        
        Opens a `.dd` file, reading its contents fully at once and calls
        `Difficulty.from_str` to parse the contents into a `Difficulty` object.
        """
        with open(path, "r") as file:
            return Difficulty.from_str(file.read())
