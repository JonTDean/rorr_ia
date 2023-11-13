import struct
import os
import json

from lib.utils.data_interpretation import find_next_header_position, interpret_general_header_data, read_data_chunk

def extract_and_organize_data(file_path):
	"""
	Extracts headers from the .win file, noting their positions.

	Args:
	file_path (str): The path to the .win file to be analyzed.

	Returns:
	dict: A dictionary with headers and their positions in the file.
	"""
	# Predefined list of headers typically found in Game Maker .win files
	headers = [
		"FORM",  # Indicates the start of a composite file format
		"GEN8",  # General game information (like settings, version)
		"OPTN",  # Game options
		"EXTN",  # Extensions used in the game
		"SOND",  # Sound resources
		"SPRT",  # Sprite resources
		"BGND",  # Background resources
		"PATH",  # Path resources
		"SCPT",  # Script resources
		"SHDR",  # Shader resources
		"FONT",  # Font resources
		"TMLN",  # Timeline resources
		"OBJT",  # Object resources (potentially including characters)
		"ROOM",  # Room resources (levels/stages in the game)
		"DAFL",  # Data file resources
		"TPAG",  # Texture page or atlas information
		"CODE",  # Code resources
		"VARI",  # Global variables
		"FUNC",  # Functions
		"STRG",  # String resources
		"TXTR",  # Texture resources
		"AUDO",  # Audio resources
		"LANG",  # Language resources
		"GLOB"   # Global settings
	]
	organized_data = {}


	with open(file_path, 'rb') as file:
		file_position = 0
		while True:
			chunk = file.read(1024)
			if not chunk:
				break

			for header in headers:
				encoded_header = header.encode()
				if encoded_header in chunk:
					next_header_position = find_next_header_position(file, file_position, headers)
					data_chunk = read_data_chunk(file, file_position, next_header_position)
					interpreted_data = interpret_general_header_data(data_chunk, header)
					organized_data[header] = interpreted_data

					# Save the interpreted data in a structured manner
					save_data(interpreted_data, header)

			file_position += 1024

	return organized_data

def save_data(data, header, directory='../data/extracted_headers'):
    """
    Saves extracted header information in a structured format.
    """
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f'{header}_headers.json')
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)