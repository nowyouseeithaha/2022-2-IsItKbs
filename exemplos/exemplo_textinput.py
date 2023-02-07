import streamlit as st
from isitkbs import *
from io import StringIO
import docx


def read_docx(file_path):
    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def write_text():
    input_text = st.text_input("Fale sobre você")

    if st.button("Enviar"):
        word = isitkbs().sentkbs(input_data=input_text)
        if(len(word) == 0):
            with open("descricao.txt", "w", encoding='utf-8') as f:
                f.write(input_text)
            st.success("Texto salvo com sucesso!")
        else:
            st.error("Você pode ter escrito algo errado: " + str(word))
        
def send_file():
    file = st.file_uploader("Escolha um arquivo", type=["txt", "docx"])

    if (file):
        try:
            stringio = StringIO(file.getvalue().decode("utf-8"))
            file_string = stringio.read()
            
        except:
            file_string = read_docx(file)
            
        words = isitkbs().sentkbs(file_string)
        file_stringList = file_string.split()
        formated_words = []
        clean_text = []
        for string in file_stringList:
            if string in words:
                formated_words.append("<font color='red'>" + string + "</font>")
            else:
                formated_words.append(string)
                clean_text.append(string)
                
        formatted_text = " ".join(formated_words)
        st.markdown(formatted_text, unsafe_allow_html=True)
        
        if st.button("Limpar texto"):
            clean_print(clean_text)
        

def clean_print(input_text):
    formatted_text = " ".join(input_text)
    st.markdown(formatted_text, unsafe_allow_html=True)
        
    
def main():
    st.title("Inscrição")
    
    write_text()
    
    send_file()
    
if __name__ == '__main__':
    main()

        