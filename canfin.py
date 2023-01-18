from nsetools import Nse
import streamlit as st

st.title("Price notifier")
ns = Nse()
allstocks =ns.get_stock_codes()
print(allstocks.values())



option = st.selectbox(
    'How would you like to be contacted?',
    allstocks,285)

st.write('You selected:', option)
print(option)


qu =ns.get_quote(option)




for value in qu.items():
    lcp =list(value)
print(type(lcp[-1]))
lcp = lcp[-1]
print(lcp)
print(type (int(lcp)))

if (int(lcp) > 600):
    print(f"Price of {option} is : ",lcp)
    st.write(f"Price of {option} is : ",lcp)


    
else:
    print("CANFINE price is : ",lcp)
    st.write(f"Price of {option} is : ",lcp)

   



