import streamlit as st

# Cognito Hosted UI URL
COGNITO_LOGIN_URL = (
    "https://ap-south-1ldsecczr5.auth.ap-south-1.amazoncognito.com/login?"
    "client_id=2sv0anl655lqjtbvdu8m38amp6&"
    "redirect_uri=https://deploytrial-37ugp2tcfqfhm8epae3ftf.streamlit.app/&"
    "response_type=code&"
    "scope=email+openid+phone"
)

st.set_page_config(page_title="RAG System Login", layout="centered")

st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2E8B57;
            margin-bottom: 20px;
        }
        .description {
            text-align: center;
            font-size: 18px;
            color: #444;
            margin-bottom: 40px;
        }
        .login-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .login-link {
            background-color: #2E8B57;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            font-size: 16px;
        }
        .footer {
            margin-top: 60px;
            text-align: center;
            font-size: 14px;
            color: #888;
        }
    </style>
    <div class="title">🔐 Secure Login</div>
    <div class="description">
        Welcome to the Retrieval-Augmented Generation (RAG) Application.<br>
        Please log in using your AWS Cognito account to continue.
    </div>
    <div class="login-button">
        <a class="login-link" href='""" + COGNITO_LOGIN_URL + """' target="_self">Login with AWS Cognito</a>
    </div>
    <div class="footer">
        This platform ensures secure access and robust data handling for enterprise knowledge retrieval.
    </div>
""", unsafe_allow_html=True)
