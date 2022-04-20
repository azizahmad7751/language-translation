from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def download_model():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    return model, tokenizer

st.title('English to Pashto Translator ')
st.markdown("[Developd By: Aziz Ahmad](https://www.linkedin.com/in/theazizahmad/)", unsafe_allow_html=True)

text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()

if st.button('Translate to Pashto'):
    if text == '':
        st.write('Please enter English text for translation') 
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_IN"
        encoded_hindi_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["ps_XX"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))
else: pass