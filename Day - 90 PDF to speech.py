import os
from google.cloud import texttospeech
from PyPDF2 import PdfReader
import io

# Function to extract text from PDF


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to convert text to speech


def text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

# Main function


def pdf_to_speech(pdf_path, output_file):
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Convert text to speech
    text_to_speech(text, output_file)

    print(f"Audio file saved as {output_file}")


# Example usage
if __name__ == "__main__":
    pdf_path = "path/to/your/pdf/file.pdf" #add your path
    output_file = "output_audio.mp3"
    pdf_to_speech(pdf_path, output_file)
