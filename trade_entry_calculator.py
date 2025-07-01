import streamlit as st

st.title("Trade Entry Calculator")

st.header("Inputs")

# Define function for bigger heading text
def big_heading(text):
    st.markdown(f"<h3 style='margin-bottom: 5px;'>{text}</h3>", unsafe_allow_html=True)

# Fixed inputs 1 to 7 with bigger headings and unique keys
big_heading("WDRR (Total credit -3)")
wdrr = st.selectbox("", options=[0, 1, 2, 3], key="wdrr")

big_heading("Full Set (Total credit -3)")
full_set = st.selectbox("", options=[0, 1, 2, 3], key="full_set")

big_heading("Partial (Total credit -3)")
partial = st.selectbox("", options=[0, 1, 2, 3], key="partial")

big_heading("DDR (Total credit -2)")
ddr = st.selectbox("", options=[0, 1, 2], key="ddr")

big_heading("Model (Total credit -2)")
model = st.selectbox("", options=[0, 1, 2], key="model")

big_heading("Zero Line +/- (Total credit -1)")
zero_line = st.selectbox("", options=[0, 1], key="zero_line")

big_heading("Entry Model (Total credit -1)")
entry_model = st.selectbox("", options=[0, 1], key="entry_model")

# Optional input 8 with bigger heading and 'Not Applicable'
st.header("Optional Input")
big_heading("TRN (Total credit -2) (Optional)")
trn_options = ['Not Applicable', 0, 1, 2]
trn = st.selectbox("", options=trn_options, index=0, key="trn")

# Compute total possible credit
base_total_credit = 15
optional_credit = 2 if trn != 'Not Applicable' else 0
total_possible_credit = base_total_credit + optional_credit

# Compute obtained credit sum
obtained_credit = wdrr + full_set + partial + ddr + model + zero_line + entry_model
if trn != 'Not Applicable':
    obtained_credit += trn

# Compute percentage
percentage = (obtained_credit / total_possible_credit) * 100 if total_possible_credit > 0 else 0

# Outputs
st.header("Results")
st.markdown(
    f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit} / {total_possible_credit}</span></h3>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h3><b>Percentage of Total Credit:</b> <span style='color:green;'>{percentage:.2f}%</span></h3>",
    unsafe_allow_html=True,
)
