from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import io,os
#loading the environment variable
load_dotenv()
api_key=os.getenv("GIMINI_API_KEY")

#initializing a client
client=genai.Client(api_key=api_key)

#Generator note 
def note_generator(images):
    promt="""summarize the picture in note formate at max 100 words in Bangla language
          make sure to add necessary markdown to differentiate diffent section"""
    response=client.models.generate_content(
          model="gemini-3-flash-preview",
          contents=[images,promt]
    ) 
    return response.text  
#Audio transcription:
def audio_transcription(text):
    speech=gTTS(text,lang="bn",slow=False)
    speech_buffer=io.BytesIO()
    speech.write_to_fp(speech_buffer)
    return speech_buffer 

#Quiz Generator
def quiz_generator(images,difficulty):
      promt=f"""Generate 3 quizzes base on {difficulty}in bangla laguage.
            Make sure to add markdown to differentiate to option and add currect answer"""
      response=client.models.generate_content(
          model="gemini-3-flash-preview",
          contents=[images,promt]
      )
      return response.text