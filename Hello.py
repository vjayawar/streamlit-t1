from urllib.error import URLError

import numpy as np
import pandas as pd
import random
import altair as alt
#import plotly
import plotly.graph_objects as go
#import plotly.express as px

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

    s=10
    c = []     

    for i in range(s):
        c.append(random.choice(capability))

    data = {'P': rng.integers(low=0, high=1000000, size=s),
            'D': rng.integers(low=0, high=2, size=s),
            'C' : c
    }

    df = pd.DataFrame(data)

    cap_select = st.selectbox("select capabilities", capability)

    df2 = df[ df['C'] == cap_select ]

    st.dataframe(df2)

    chart = alt.Chart(df).mark_bar().encode(
        x='D',
        y='P',
        color='C'
    )
    st.altair_chart(chart, use_container_width=False, theme="streamlit")


    fig = go.Figure(go.Treemap(
        labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch",
            "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    ))

    st.plotly_chart(fig)




if __name__ == "__main__":
    run()
