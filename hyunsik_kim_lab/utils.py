import os
from uuid import uuid4


def generate_filename(filename):
    generated_uuid = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return ''.join([
        generated_uuid + extension,
    ])
