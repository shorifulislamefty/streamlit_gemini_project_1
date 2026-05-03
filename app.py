import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image
st.title("Note summary and Quiz generator",anchor=False)
st.markdown("Upload upto 3 images to generator note summary and Quiz")
st.divider()
with st.sidebar:
    st.header("Control")

    #work for Images
    images=st.file_uploader(
        "Upload photos on your notes ",
        type=["jpg","jepg","png"],
        accept_multiple_files=True
    )
    if images:
        #images convert to pil_images
        pil_images=[]
        for img in images:
            pil_image=Image.open(img)
            pil_images.append(pil_image)

        if len(images)>3:
            st.warning("Upload max 3 images")
        else: 
            st.subheader("Uploaded images")   
            clm=st.columns(len(images))
            for i,img in enumerate(images):
                with clm[i]:
                    st.image(img)
    #difficulty
    selected_option=st.selectbox(
       "Enter the difficulty of your Quiz",
        ("Easy","Medium","Hard"),
        index=None
    )
    if selected_option:
        st.markdown(f"You select **{selected_option}** as difficulty of your Quiz")
   
    pressed=st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not images:
        st.error("You must 1 image Upload")
    if not selected_option:
        st.error("You must select difficulty")
    if images and selected_option:
        #Note 
        with st.container(border=True):
            st.subheader("Your note",anchor=False) 

            #The portion will replace by API call
            with st.spinner("AI is writing note for you"): 
                note_generated=note_generator(pil_images)  
                st.markdown(note_generated)

        #Audio
        note_generated=note_generated.replace("*","")
        note_generated=note_generated.replace("#","")
        note_generated=note_generated.replace("(","")
        note_generated=note_generated.replace(")","")
        note_generated=note_generated.replace("$","")
        with st.container(border=True):
            st.subheader("Audio trancription",anchor=False) 

            #The portion will replace by API call
            with st.spinner("AI is generating voice of note for you"): 
                audio_transcript=audio_transcription(note_generated)   
                st.audio(audio_transcript)    
        
        #Generate Quiz
        with st.container(border=True):
            st.subheader(f"Your Quiz ({selected_option}) difficulty",anchor=False) 

            #The portion will replace by API call
            with st.spinner("AI is making your Quiz"):
                quizzes=quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)
