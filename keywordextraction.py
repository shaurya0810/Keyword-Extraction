import streamlit as st
import newspaper
import nltk

nltk.download('punkt')

# st.markdown('<style> .css-1v0mbdj {margin:0 auto; width:50%; </style>', unsafe_allow_html=True)


st.title('Article Summarizer')

url = st.text_input('', placeholder='Paste the URL of the article amd press Enter')

if url:
    try:
        article = newspaper.Article(url)

        article.download()
        # article.html
        article.parse()

        img = article.top_image
        st.image(img)
        

        title = article.title
        st.subheader(title)
        

        authors = article.authors
        st.text(','.join(authors))
        
        article.nlp()

        keywords = article.keywords
        st.subheader('Keywords:')
        st.write(', '.join(keywords))
        
        tab1, tab2= st.tabs(["Full Text", "Summary"])
        with tab1:
            txt = article.text
            txt = txt.replace('Advertisement', '')
            st.write(txt)
        
        with tab2:
            st.subheader('Summary')
            summary = article.summary
            summary = summary.replace('Advertisement', '')
            st.write(summary)
        
        
    except:
        st.error('Sorry something went wrong')
