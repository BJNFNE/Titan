# execute pip install pydub first to use the Converter correctly

import os
import subprocess
import argparse

def convert_to_voc(input_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"File {input_file} does not exist.")
        return

    # Get the file name without extension
    file_name = os.path.splitext(input_file)[0]

    # Define the output VOC file name
    output_file = f"{file_name}.voc"

    # Use ffmpeg to convert the input file to VOC format
    try:
        subprocess.run(['ffmpeg', '-i', input_file, output_file], check=True)
        print(f"File converted successfully to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return

    # Rename the output file extension to .D
    new_file_name = f"{file_name}.D"
    os.rename(output_file, new_file_name)
    print(f"File renamed to {new_file_name}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert audio file to VOC format and rename to .D extension.")
    parser.add_argument("input_file", type=str, help="Path to the input audio file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Convert the input file
    convert_to_voc(args.input_file)
