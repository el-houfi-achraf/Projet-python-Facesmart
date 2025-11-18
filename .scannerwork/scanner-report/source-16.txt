# Lightweight stub for `face_recognition` to allow UI preview when the real
# `face-recognition` package (and dlib) is not installed.
#
# This stub provides minimal functions used by the codebase so the application
# can start for UI/theme verification. It does NOT perform any real face
# recognition. Replace/remove this file once `face-recognition` is installed.

from typing import List, Tuple, Any

__all__ = [
    'load_image_file',
    'face_locations',
    'face_encodings',
    'compare_faces',
]


def load_image_file(path: str) -> Any:
    """Return a placeholder image object (None)."""
    return None


def face_locations(image: Any) -> List[Tuple[int, int, int, int]]:
    """Return empty list (no faces)."""
    return []


def face_encodings(image: Any, known_face_locations=None) -> List[Any]:
    """Return empty encodings list."""
    return []


def compare_faces(known_encodings: List[Any], candidate_encoding: Any) -> List[bool]:
    """Return list of False (no matches)."""
    return [False for _ in known_encodings]
