
# ============================================================
# PROJECT: QUICKGREETINGS AI
# APPLICATION: AI GREETING CARD ASSISTANT
# TECHNOLOGY: PYTHON, STREAMLIT, GOOGLE GEMINI API
# ============================================================

# STEP 1: IMPORT REQUIRED LIBRARIES

import streamlit as st
from google import genai


# STEP 2: STREAMLIT PAGE CONFIGURATION

st.set_page_config(
    page_title="QuickGreetings AI",
    page_icon="💌",
    layout="centered"
)


# STEP 3: APPLICATION TITLE AND DESCRIPTION

st.title("💌 QuickGreetings AI")

st.write(
    """
    Welcome to **QuickGreetings AI!**

    Create beautiful, personalized greeting messages
    for your friends, family, and loved ones using
    Google's Gemini Generative AI.
    """
)

st.divider()


# STEP 4: CONFIGURE GEMINI API SECURELY

try:

    # Retrieve API key from Streamlit secrets
    API_KEY = st.secrets["GEMINI_API_KEY"]

    # Initialize Gemini client
    client = genai.Client(api_key=API_KEY)

except KeyError:

    st.error(
        "Gemini API key not found! "
        "Please configure GEMINI_API_KEY "
        "inside .streamlit/secrets.toml."
    )

    st.stop()

except Exception as e:

    st.error(f"API configuration error: {e}")

    st.stop()


# STEP 5: INITIALIZE GEMINI MODEL

MODEL = "gemini-3.8-flash"


# STEP 6: CREATE USER INPUT INTERFACE

st.subheader("🎨 Create Your Greeting Card")

# Input 1: Occasion
occasion = st.text_input(
    "🎉 Enter the Occasion",
    placeholder="Example: Birthday, Anniversary, Diwali"
)

# Input 2: Recipient
recipient = st.text_input(
    "❤️ Who is this greeting for?",
    placeholder="Example: My best friend, Mother, Brother"
)

# Input 3: Tone selection
tone = st.selectbox(
    "✨ Select Your Desired Tone",
    [
        "Funny",
        "Formal",
        "Heartfelt",
        "Emotional",
        "Inspirational",
        "Romantic",
        "Friendly"
    ]
)

# STEP 7: GENERATE GREETING MESSAGE

if st.button("💌 Generate Message", use_container_width=True):

    # Validate user inputs
    if not occasion.strip() or not recipient.strip():

        st.warning(
            "Please enter both the occasion and recipient "
            "before generating your greeting!"
        )

    else:

        # STEP 8: CONSTRUCT AN ENGINEERED PROMPT

        prompt = f"""
        You are QuickGreetings AI, a professional
        greeting card writer.

        Your task is to create a personalized greeting
        card message based on the following information.

        OCCASION: {occasion}
        RECIPIENT: {recipient}
        DESIRED TONE: {tone}

        INSTRUCTIONS:

        1. Write a unique and personalized greeting.
        2. Match the writing style to the selected tone.
        3. Make the recipient feel special and appreciated.
        4. Use natural, grammatically correct English.
        5. Include appropriate emojis.
        6. Avoid generic and repetitive sentences.
        7. Keep the message between 80 and 120 words.
        8. Include a creative heading.
        9. End with a warm closing statement.
        10. Return only the greeting card content.

        Generate a beautiful greeting card message now.
        """

        # STEP 9: SEND PROMPT TO GEMINI API

        try:

            with st.spinner(
                "✨ Gemini AI is creating your greeting card..."
            ):

                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt
                )

            # STEP 10: DISPLAY GENERATED RESPONSE

            if response.text:

                st.success(
                    "Your greeting card has been generated!"
                )

                st.divider()

                st.subheader("💝 Your Personalized Greeting")

                st.markdown(response.text)

                st.divider()

                st.caption(
                    "Generated using Google Gemini AI | "
                    "QuickGreetings AI"
                )

            else:

                st.warning(
                    "The AI did not return any text. "
                    "Please try again."
                )

        except Exception as e:

            st.error(
                f"Something went wrong while generating "
                f"your greeting: {e}"
            )


# STEP 11: APPLICATION FOOTER

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <p>Made with ❤️ using Python and Gemini AI</p>
        <p>© 2026 QuickGreetings AI</p>
    </div>
    """,
    unsafe_allow_html=True
)
