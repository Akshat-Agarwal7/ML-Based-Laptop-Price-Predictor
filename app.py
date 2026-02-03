import streamlit as st
import numpy as np
import pandas as pd
import pickle
st.title("Latptop Predictor")
df=pickle.load(open('df.pkl','rb'))
pipe=pickle.load(open('pipe.pkl','rb'))

br=st.selectbox("Brand",df['Company'].unique())
tn=st.selectbox("What is the type of laptop",df['TypeName'].unique())
ram=st.selectbox("Select the RAM(in GB)",[2,4,6,8,12,16,32,64])
os=st.selectbox("Select the Operating System",df['OpSys'].unique())
weight=st.number_input("Tell the weight in kgs")
chip=st.selectbox("Select the chipset",df['chipset'].unique())
ips=st.selectbox("Does the laptop has IPS display",['No','Yes'])
touch=st.selectbox("Does the laptop has touch display",['No','Yes'])
gpu=st.selectbox("What is the gpu ",df['Gpu_brand'].unique())
ssd=st.selectbox("What is the ssd ",[0,128,256,512])
x=st.selectbox("What is the screen resolution ",['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
size=st.number_input("Tell the screen size in inches")


# if st.button("Predict Price"):
#     if touch=='Yes':
#         touch=1
#     else:
#         touch=0
#     if ips=='Yes':
#         ips=1
#     else:
#         ips=0
#     x_r=int(x.split('x')[0])
#     y_r=int(x.split('x')[1])
#     ppi=((x_r**2)+(y_r**2))**0.5/size


#     list=np.array([br,tn,ram,os,weight,chip,ips,touch,ppi,gpu,ssd])
#     list=list.reshape(1,11)
#     st.title(pipe.predict(list))

if st.button("Predict Price"):

    touch = 1 if touch == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    x_r = int(x.split('x')[0])
    y_r = int(x.split('x')[1])
    ppi = ((x_r**2 + y_r**2) ** 0.5) / size

    # 👇 Create dataframe FIRST
    input_df = pd.DataFrame([{
        'Company': br,
        'TypeName': tn,
        'Ram': ram,
        'OpSys': os,
        'Weight': weight,
        'chipset': chip,
        'ips': ips,
        'TouchScreen': touch,
        'ppi': ppi,
        'Gpu_brand': gpu,
        'ssd': ssd
    }])

    # 👇 Then predict
    prediction = pipe.predict(input_df)[0]
    price = np.exp(prediction)

    st.success(f"Predicted Price: ₹ {int(price)}")
