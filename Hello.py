from urllib.error import URLError

import numpy as np
import pandas as pd
import random

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Data Test",
        page_icon="->",
    )

    rng = np.random.default_rng(98765)
    random.seed(98765)

    capability = ["client", "connectivity","trading","middle_office","settlements"]

    c = []     
    for i in range(50):
        c.append(random.choice(capability))

    data = {'P1': rng.integers(low=0, high=1000000, size=50),
            'P2': rng.integers(low=0, high=100, size=50),
            'C' : c
    }

    df = pd.DataFrame(data)
      
    st.write(df)

    st.write("# Welcome to Streamlit! Vince  👋")

    #st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
