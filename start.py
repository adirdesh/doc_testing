import streamlit as st
import urllib.parse

# Configuration
COGNITO_DOMAIN = "https://ap-south-1ldsecczr5.auth.ap-south-1.amazoncognito.com"
CLIENT_ID = "2sv0anl655lqjtbvdu8m38amp6"
REDIRECT_URI = "https://deploytrial-37ugp2tcfqfhm8epae3ftf.streamlit.app/"
RESPONSE_TYPE = "code"
SCOPE = "email openid phone"

# Build the Cognito URL properly
def build_cognito_url():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': RESPONSE_TYPE,
        'scope': SCOPE
    }
    
    query_string = urllib.parse.urlencode(params)
    return f"{COGNITO_DOMAIN}/login?{query_string}"

COGNITO_LOGIN_URL = build_cognito_url()

st.set_page_config(page_title="RAG System Login", layout="centered")

# Debug information (remove in production)
if st.sidebar.checkbox("Show Debug Info"):
    st.sidebar.write("**Cognito URL:**")
    st.sidebar.code(COGNITO_LOGIN_URL)
    st.sidebar.write("**Current URL:**")
    st.sidebar.write(st.experimental_get_query_params())

st.markdown(f"""
    <style>
        .title {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #2E8B57;
            margin-bottom: 20px;
        }}
        .description {{
            text-align: center;
            font-size: 18px;
            color: #444;
            margin-bottom: 40px;
        }}
        .login-button {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }}
        .login-link {{
            background-color: #2E8B57;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            font-size: 16px;
            transition: background-color 0.3s;
        }}
        .login-link:hover {{
            background-color: #246B47;
            color: white;
            text-decoration: none;
        }}
        .footer {{
            margin-top: 60px;
            text-align: center;
            font-size: 14px;
            color: #888;
        }}
        .manual-link {{
            margin-top: 20px;
            text-align: center;
        }}
    </style>
    <div class="title">🔐 Secure Login</div>
    <div class="description">
        Welcome to the Retrieval-Augmented Generation (RAG) Application.<br>
        Please log in using your AWS Cognito account to continue.
    </div>
    <div class="login-button">
        <a class="login-link" href="{COGNITO_LOGIN_URL}" target="_self">Login with AWS Cognito</a>
    </div>
    <div class="manual-link">
        <small>If the button doesn't work, <a href="{COGNITO_LOGIN_URL}" target="_blank">click here</a></small>
    </div>
    <div class="footer">
        This platform ensures secure access and robust data handling for enterprise knowledge retrieval.
    </div>
""", unsafe_allow_html=True)

# Alternative JavaScript-based redirect (uncomment if needed)
# st.markdown(f"""
# <script>
# function redirectToCognito() {{
#     window.location.href = "{COGNITO_LOGIN_URL}";
# }}
# </script>
# <button onclick="redirectToCognito()" style="
#     background-color: #2E8B57;
#     color: white;
#     padding: 12px 24px;
#     border: none;
#     border-radius: 10px;
#     font-weight: bold;
#     font-size: 16px;
#     cursor: pointer;
# ">Login with JavaScript</button>
# """, unsafe_allow_html=True)

# Handle the callback after Cognito redirect
query_params = st.experimental_get_query_params()
if 'code' in query_params:
    auth_code = query_params['code'][0]
    st.success(f"✅ Authorization code received: {auth_code[:10]}...")
    st.info("You can now exchange this code for tokens using your backend service.")
    
    # Here you would typically:
    # 1. Exchange the authorization code for tokens
    # 2. Validate the tokens
    # 3. Set session state or redirect to main app
    
elif 'error' in query_params:
    error = query_params['error'][0]
    st.error(f"❌ Authentication error: {error}")
    if 'error_description' in query_params:
        st.error(f"Description: {query_params['error_description'][0]}")
