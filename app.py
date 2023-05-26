import streamlit as st
import pickle
import pandas as pd


team=['Royal Challengers Bangalore',
 'Kings XI Punjab',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Sunrisers Hyderabad',
 'Chennai Super Kings',
 'Delhi Capitals']

city=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL WIN PREDICTION')

col1,col2 =st.columns(2)

with col1:
    batting_team=st.selectbox('select the batting team',sorted(team))
with col2:
    bowling_team=st.selectbox('select the bowling team',sorted(team))
selected_city=st.selectbox("selected the venue",sorted(city))
target=st.number_input('Target')
col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input('Current Score')
with col4:
    over=st.number_input('over_completed')
with col5:
    wickets=st.number_input('Wickets out')

if st.button('predict probability'):
    runs_left=target-score
    ball_left=120-(over*6)
    wickets=10-wickets
    crr=score/over
    rrr=(runs_left*6)/ball_left

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
                           'runs_left':[runs_left],'ball_left':[ball_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]
                           })
    
   # st.table(input_df)
    result=pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.header(batting_team+"-"+str(round(win*100))+"%")
    st.header(bowling_team+"-"+str(round(loss*100))+"%")