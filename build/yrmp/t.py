import json
import io

with io.open("C:\\Users\\Frankie\\Documents\\GitHub\\emojipasta-bot\\build\\yrmp\\emoji-mappings.json", "r", encoding="utf-8") as mappings_file:
    _EMOJI_MAPPINGS = json.load(mappings_file)
