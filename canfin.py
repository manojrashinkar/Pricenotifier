from nsetools import Nse
import pandas as pd
import streamlit as st

from paho.mqtt import client as mqtt_client


st.title("Price notifier")
ns = Nse()
key_v = list()
qu =ns.get_quote('CANFINHOME')
for value in qu.items():
    lcp =list(value)
print(type(lcp[-1]))
lcp = lcp[-1]
print(lcp)
print(type (int(lcp)))

if (int(lcp) > 600):
    print("Price of CANFIN is : ",lcp)
    st.header(lcp)
else:
    print("CANFINE price is : ",lcp)
    st.header("Price of CANFIN is : ",lcp)



