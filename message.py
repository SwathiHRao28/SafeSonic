from twilio.rest import Client

# Twilio credentials from your account
TWILIO_ACCOUNT_SID = 'SID'
TWILIO_AUTH_TOKEN = 'TOKEN'
TWILIO_PHONE_NUMBER = 'ADD NUMBER'

# Function to send an SMS alert to the user
def send_sms_alert(user_phone_number, message):
    try:
        # Initialize the Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        user_phone_number=PHONE NUMBER
        # Send the SMS
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,  # Your Twilio phone number
            to=user_phone_number       # The user's phone number
        )
        st.success(f"Alert sent successfully to {user_phone_number}!")
    except Exception as e:
        st.error(f"Error sending SMS: {e}")
