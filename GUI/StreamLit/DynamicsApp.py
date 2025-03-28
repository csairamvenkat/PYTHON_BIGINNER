import streamlit as st
import requests
import json
from datetime import datetime, timedelta
import os

# Dynamics 365 Configuration
DYNAMICS_URL = "https://zmsdev.crm4.dynamics.com/"  # e.g., https://yourorg.crm.dynamics.com
CLIENT_ID = "c961d6dd-7168-497e-93fc-4eb43aecca2f"
CLIENT_SECRET = ""
TENANT_ID = "2bd16c9b-7e21-4274-9c06-7919f7647bbb"  # Azure AD Tenant ID
RESOURCE = DYNAMICS_URL  # Usually the same as DYNAMICS_URL


# OAuth 2.0 Token Acquisition (with caching)
@st.cache_data(ttl=3600)  # Cache for 1 hour (adjust as needed)
def get_dynamics_token():
    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "resource": RESOURCE,
    }
    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        token_data = response.json()
        token = token_data.get("access_token")
        expires_in = token_data.get("expires_in")

        if expires_in is not None:
          try:  # Try converting to int, if fails try float
            expires_in = int(expires_in)
          except ValueError:
            try:
                expires_in = float(expires_in)
            except ValueError:
                st.error("Invalid 'expires_in' value in token response. Should be a number.")
                return None, None  # Or handle the error as you see fit

          expiry_time = datetime.now() + timedelta(seconds=expires_in)
        else:
            expiry_time = datetime.now() + timedelta(hours=1)  # Default 1 hour if no expiry
            st.warning("Token response did not include 'expires_in'. Using default expiry of 1 hour.") # Inform user

        return token, expiry_time
    except requests.exceptions.RequestException as e:
        st.error(f"Token Acquisition Failed: {e}")
        return None, None

# Function to fetch countries from D365
def fetch_countries(token):  # Pass the token as an argument
    headers = {
        "Authorization": f"Bearer {token}",
        "OData-MaxPageSize": "500"
    }
    try:
        response = requests.get(f"{DYNAMICS_URL}/api/data/v9.2/qtq_countrieses?$select=qtq_name,qtq_countriesid", headers=headers)
        response.raise_for_status()
        countries_data = response.json().get('value', [])
        country_dict = {country["qtq_name"]:country["qtq_countriesid"] for country in countries_data if country.get("qtq_countriesid")} # Simplified
        return country_dict
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching countries: {e}")
        return {}

# Create Account Function (with improved error handling and return)
def create_account(account_data, token):
    url = f"{DYNAMICS_URL}/api/data/v9.2/accounts"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(account_data))
        response.raise_for_status()
        st.success("Account created successfully!")
        return response.json()  # Return the JSON response (including accountid)
    except requests.exceptions.RequestException as e:
        st.error(f"Account Creation Failed: {e}")
        try:
            error_data = response.json() if hasattr(response, 'json') else None # Check if response has json
            if error_data:
                st.error(f"D365 Error Details: {error_data}")
            else:
                st.error(f"D365 Error Details (non-JSON): {response.text if hasattr(response, 'text') else str(e)}") # Print the error or exception
        except json.JSONDecodeError:
            st.error(f"D365 Error Details (non-JSON): {response.text if hasattr(response, 'text') else str(e)}")
        return None

# Streamlit App
st.title("Dynamics 365 Account Creation")

# Get Token
token, expiry_time = get_dynamics_token()

if token:
    countries = fetch_countries(token) # Pass the token to fetch_countries
    if countries: # Check if countries were fetched successfully
        with st.form("account_form"):
            account_name = st.text_input("Account Name") # Make account name required
            website = st.text_input("Website")
            email = st.text_input("Email")
            registrationdate = st.date_input("Registration Date").strftime("%Y-%m-%d")
            description = st.text_area("Description")

            country_names = list(countries.keys())
            selected_country = st.selectbox("Country", country_names)
            
            # # For non-unique values:
            # countries_reverse_dict = {}
            # for key, value in countries.items():
            #  countries_reverse_dict.setdefault(value, []).append(key) #Handles duplicate values by storing them in a list
            country_id = countries.get(selected_country) # Use .get to handle potential missing keys
            submitted = st.form_submit_button("Create Account")

        if submitted:
            if not country_id:
                st.error("Please select a country.")
            else:

                account_data = {
                    "name": account_name,
                    "qtq_CountryId@odata.bind": f"/qtq_countrieses({country_id})",
                    "websiteurl": website,
                    "emailaddress1": email,
                    "fz_registrationdate": registrationdate,
                    "description": description,
                }
                response_data = create_account(account_data, token) # Capture the response

                if response_data:
                    st.write("Account created successfully with ID:", response_data.get("accountid")) # Display account id
    else:
        st.error("Failed to fetch countries. Check your D365 connection.")
else:
    st.error("Failed to obtain Dynamics 365 access token. Check your credentials and environment variables.")