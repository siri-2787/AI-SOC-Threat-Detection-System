import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import random
import time

st.set_page_config(page_title="AI SOC Center", layout="wide")

# HEADER
st.markdown("<h1 style='text-align:center;color:#00ffcc;'>🛡️ AI SOC Intelligence Center</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:gray;'>Real-Time Cyber Threat Detection</h4>", unsafe_allow_html=True)

st.divider()

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Total Traffic", random.randint(4000, 9000))
c2.metric("Threats", random.randint(50, 200))
c3.metric("Safe Requests", random.randint(3000, 8000))

st.divider()

mode = st.selectbox("Select Mode", ["Manual Analysis", "Bulk Analysis", "Live Simulation"])


# ---------------- MANUAL ----------------
if mode == "Manual Analysis":
    st.subheader("Manual Threat Check")

    col1, col2 = st.columns(2)

    with col1:
        duration = st.number_input("Duration", 0)
        src_bytes = st.number_input("Source Bytes", 0)
        dst_bytes = st.number_input("Destination Bytes", 0)

    with col2:
        count = st.number_input("Connection Count", 0)
        serror = st.slider("Error Rate", 0.0, 1.0)

    if st.button("Run Scan"):
        payload = {
            "duration": duration,
            "protocol_type": 1,
            "service": 1,
            "src_bytes": src_bytes,
            "dst_bytes": dst_bytes,
            "count": count,
            "srv_count": count,
            "serror_rate": serror,
            "srv_serror_rate": serror,
            "same_srv_rate": 1
        }

        try:
            res = requests.post("http://127.0.0.1:5000/predict", json=payload).json()

            st.metric("Threat Score", res["score"])

            if res["result"] == "ATTACK":
                st.error(f"🚨 ATTACK ({res['severity']})")
            else:
                st.success("🟢 NORMAL")

            st.info(res["reason"])

        except:
            st.error("API NOT RUNNING")


# ---------------- BULK ----------------
elif mode == "Bulk Analysis":

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)

        if st.button("Run SOC Audit"):

            results = []
            progress = st.progress(0)

            p_map = {"icmp":0,"tcp":1,"udp":2}
            s_map = {"http":1,"private":2,"ftp_data":3,"other":0}

            for i in range(len(df)):
                row = df.iloc[i]

                payload = {
                    "duration": float(row.get("duration",0)),
                    "protocol_type": p_map.get(str(row.get("protocol_type")).lower(),1),
                    "service": s_map.get(str(row.get("service")).lower(),1),
                    "src_bytes": float(row.get("src_bytes",0)),
                    "dst_bytes": float(row.get("dst_bytes",0)),
                    "count": float(row.get("count",0)),
                    "srv_count": float(row.get("srv_count",0)),
                    "serror_rate": float(row.get("serror_rate",0)),
                    "srv_serror_rate": float(row.get("srv_serror_rate",0)),
                    "same_srv_rate": float(row.get("same_srv_rate",1))
                }

                try:
                    res = requests.post("http://127.0.0.1:5000/predict", json=payload).json()
                except:
                    res = {"result":"ERROR","severity":"UNKNOWN","score":0}

                results.append(res)
                progress.progress((i+1)/len(df))

            df["RESULT"] = [r["result"] for r in results]
            df["SEVERITY"] = [r["severity"] for r in results]
            df["SCORE"] = [r["score"] for r in results]

            st.subheader("SOC Report")

            # FIXED COUNTS
            summary = df["RESULT"].value_counts().reset_index()
            summary.columns = ["RESULT","COUNT"]

            col1,col2 = st.columns(2)

            with col1:
                st.plotly_chart(px.pie(summary,names="RESULT",values="COUNT"), use_container_width=True)

            with col2:
                sev = df["SEVERITY"].value_counts().reset_index()
                sev.columns=["SEVERITY","COUNT"]
                st.plotly_chart(px.bar(sev,x="SEVERITY",y="COUNT"), use_container_width=True)

            st.dataframe(df)

            st.download_button("Download Report", df.to_csv(index=False), "report.csv")


# ---------------- LIVE ----------------
elif mode == "Live Simulation":

    st.subheader("Live Attack Simulation")

    box = st.empty()

    for i in range(15):
        payload = {
            "duration": random.randint(1,1000),
            "protocol_type": random.randint(0,2),
            "service": random.randint(0,3),
            "src_bytes": random.randint(100,5000),
            "dst_bytes": random.randint(50,3000),
            "count": random.randint(1,100),
            "srv_count": random.randint(1,50),
            "serror_rate": random.random(),
            "srv_serror_rate": random.random(),
            "same_srv_rate": random.random()
        }

        try:
            res = requests.post("http://127.0.0.1:5000/predict", json=payload).json()
        except:
            res = {"result":"ERROR","score":0}

        with box.container():
            st.write("Packet Result:", res["result"])
            st.progress(res.get("score",0)/100)

        time.sleep(0.5)