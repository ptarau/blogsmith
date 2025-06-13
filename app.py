import streamlit as st
import os

from blogsmith import __version__
from blogsmith.blogger import (
    run_blogger,
    set_openai_api_key,
    clear_key,
)

st.sidebar.title(
    f"[blogsmith {__version__}](https://github.com/ptarau/blogsmith/): LLM-based multi-agent bloger"
)


def collect_key():
    placeholder = st.empty()
    key = os.getenv("OPENAI_API_KEY")
    key = set_openai_api_key(key)

    if not key:
        with placeholder.form("my_form", clear_on_submit=True):
            key = st.text_input("Enter your OPENAI_API_KEY:", "", type="password")
            submitted = st.form_submit_button("Submit")
            if submitted:

                key = set_openai_api_key(key)
                if not key:
                    st.write("We need a valid key to run this!")
                else:
                    placeholder.empty()
    return key


key = collect_key()

with st.sidebar:
    initiator = st.text_area(
        "Topic to generate a blog post about:",
        value="automate blog development with help of LLMs",
    )

    query_it = st.button("Generate the blog!")
    clear_it = st.button("Clear the key!")


def do_query():
    if not key:
        st.write("No key provided yet!")
        return
    html = run_blogger(initiator)
    st.write(html)


if query_it:
    do_query()

if clear_it:
    clear_key()
