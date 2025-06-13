import streamlit as st
import os

from blogsmith import __version__
from blogsmith.blogger import run_blogger, set_openai_api_key, ensure_openai_api_key

st.sidebar.title(
    f"[blogsmith {__version__}](https://github.com/ptarau/blogsmith/): LLM-based multi-agent bloger"
)


def collect_key():
    key = os.getenv("OPENAI_API_KEY")
    if key and len(key) > 40:
        set_openai_api_key(key)
    key = ensure_openai_api_key()
    if not key:
        key = st.text_input("Enter your OPENAI_API_KEY:", "", type="password")
        if not key:
            st.write("We need a key to run this!")
            exit(0)
        else:
            set_openai_api_key(key)


with st.sidebar:
    initiator = st.text_area(
        "Topic to generate a blog post about:",
        value="automate blog development with help of LLMs",
    )

    collect_key()
    query_it = st.button("Generate the blog!")


def do_query():
    html = run_blogger(initiator)
    st.write(html)


if query_it:
    do_query()
