import streamlit as st
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go


# import config


# auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
# auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

st.title("Finance Dashboard")

# df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
# st.dataframe(df)
# st.sidebar.image("https://charts.finanzen100.de/bwcharts/images/finanzen100/plain/fe-hist.png?expires=3600&ID_INSTRUMENT=181045095&chart.xAxis.dateFormat=MMM&start=2020-10-22&timeSpan=1Y&key.codeMarket=_GAT&codeResolution=1d")

stonk = st.sidebar.selectbox('Select your Stonk?', ('Aker Carbon Capture', 'Palantir', 'Paypal', "Twitter"), 3)
option = st.sidebar.selectbox("Chose", ("Charts", "Twitter Posts"))
st.header(option)

if stonk == "Palantir":
    st.image("https://charts2.finviz.com/chart.ashx?t=PLTR")


if stonk == "Paypal" :
    if option == "Charts":
        symbol = st.sidebar.text_input("Symbol", value='MSFT', max_chars=None, key=None, type='default')
    
        data = pd.read_sql("""
            select date(day) as day, open, high, low, close
            from daily_bars
            where stock_id = (select id from stock where UPPER(symbol) = %s) 
            order by day asc""", connection, params=(symbol.upper(),))
    
        st.subheader(symbol.upper())
    
        fig = go.Figure(data=[go.Candlestick(x=data['day'],
                        open=data['open'],
                        high=data['high'],
                        low=data['low'],
                        close=data['close'],
                        name=symbol)])
    
        fig.update_xaxes(type='category')
        fig.update_layout(height=700)
    
        st.plotly_chart(fig, use_container_width=True)
    
        st.write(data)
    
        
    if option == "Twitter Posts":
        symbol = st.sidebar.text_input("Symbol", value="PYPL", max_chars=5, key=None, type="default")
        r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")      
        data = r.json()     
        for message in data["messages"]:
            st.image(message["user"]["avatar_url"])
            st.write(message["user"]["username"])
            st.write(message["created_at"])
            st.write(message["body"])       

if stonk == "Twitter":
    st.subheader("Dashboard")