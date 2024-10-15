import streamlit as st

# Title for the app
st.title("Button Demonstration")

# Button to display a welcome message
if st.button("Click me for a welcome message"):
    st.write("Welcome to Streamlit! You've clicked the button.")

# Button to toggle a boolean state
if 'toggle' not in st.session_state:
    st.session_state['toggle'] = False

if st.button("Toggle Me"):
    st.session_state['toggle'] = not st.session_state['toggle']

if st.session_state['toggle']:
    st.write("The toggle is ON")
else:
    st.write("The toggle is OFF")

# Button to perform a counter
if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button("Increment Counter"):
    st.session_state['count'] += 1

st.write(f"Button pressed {st.session_state['count']} times.")

# Button to reset the counter
if st.button("Reset Counter"):
    st.session_state['count'] = 0
    st.write("Counter reset.")

# A button that performs multiple actions
if st.button("Perform Multiple Actions"):
    st.write("You triggered multiple actions!")
    st.session_state['count'] += 1
    st.session_state['toggle'] = not st.session_state['toggle']
    st.write(f"Counter incremented to {st.session_state['count']}. Toggle is now {'ON' if st.session_state['toggle'] else 'OFF'}.")


# Function that will be triggered by the button
def compute_square(number):
    return number ** 2

# Title for the app
st.title("Button Example with Function Execution")

# Input to get a number from the user
number = st.number_input("Enter a number", value=1)

# Button to trigger the function
if st.button("Compute Square"):
    result = compute_square(number)
    st.write(f"The square of {number} is {result}")



st.title("Exemplo do zero!")

if 'contador' not in st.session_state:
  st.session_state['contador'] = 0

if st.button("Exemplo"):
  st.session_state['contador']+=1
  contador = st.session_state['contador']
  
st.write(f"Contador: {contador}")
