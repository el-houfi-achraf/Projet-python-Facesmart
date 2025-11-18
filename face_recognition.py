# Project-level shim to redirect imports of `face_recognition` to the local
# stub in `src/` when the real package is not installed.
try:
    from src.face_recognition import *
except Exception:
    # Fallback minimal definitions
    def load_image_file(path):
        return None
    def face_locations(image):
        return []
    def face_encodings(image, known_face_locations=None):
        return []
    def compare_faces(known_encodings, candidate_encoding):
        return [False for _ in known_encodings]
