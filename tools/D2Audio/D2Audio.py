import os

def convert_to_wav(input_file):
    output_file = os.path.splitext(input_file)[0] + ".wav"
    os.system(f"ffmpeg -i {input_file} {output_file}")

def convert_to_mp3(input_file):
    output_file = os.path.splitext(input_file)[0] + ".mp3"
    os.system(f"ffmpeg -i {input_file} {output_file}")

def convert_to_ogg(input_file):
    output_file = os.path.splitext(input_file)[0] + ".ogg"
    os.system(f"ffmpeg -i {input_file} {output_file}")

def main():
    input_file = input("Enter the path to the Creative Voice File (.D): ")
    
    if not os.path.exists(input_file):
        print("File not found!")
        return

    print("Select the format to convert:")
    print("1. WAV")
    print("2. MP3")
    print("3. OGG")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        convert_to_wav(input_file)
    elif choice == "2":
        convert_to_mp3(input_file)
    elif choice == "3":
        convert_to_ogg(input_file)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
