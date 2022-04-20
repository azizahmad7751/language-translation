from transformers import MBartForConditionalGeneration, MBart50Tokenizer, MarianTokenizer, MarianMTModel
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)

def download_model():
    model_name = f'Helsinki-NLP/opus-mt-en-ur'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

st.title('English to Urdu Translator')
st.markdown("[Developd By: Aziz Ahmad](https://www.linkedin.com/in/theazizahmad/)", unsafe_allow_html=True)

text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()

if st.button('Translate to Urdu'):
    if text == '':
        st.write('Please enter English text for translation') 
    else: 
      
         # Tokenize the text
        batch = tokenizer(text, return_tensors="pt", padding=True)
        # tokenized text maximum allowed size of 512
        batch["input_ids"] = batch["input_ids"][:, :512]
        batch["attention_mask"] = batch["attention_mask"][:, :512]
        translation_encoded = model.generate(**batch)
        translation = tokenizer.batch_decode(translation_encoded, skip_special_tokens=True)
        st.write('', str(translation).strip('][\''))
else: pass