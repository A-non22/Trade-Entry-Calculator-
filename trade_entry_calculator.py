import streamlit as st

st.set_page_config(page_title="Trade Entry Calculators", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>Trade Calculators</h1>",
    unsafe_allow_html=True
)

# Create two columns
col1, col2 = st.columns(2)

# ------------------- Calculator 1: Trade Confidence Calculator -------------------
with col1:
    st.header("Trade Confidence Calculator")

    # Inputs for App 1
    wdrr = st.selectbox("WDRR (Total credit -3)", options=[0, 1, 2, 3], key="wdrr")
    full_set = st.selectbox("Full Set (Total credit -3)", options=[0, 1, 2, 3], key="full_set")
    partial = st.selectbox("Partial (Total credit -3)", options=[0, 1, 2, 3], key="partial")
    ddr = st.selectbox("DDR (Total credit -2)", options=[0, 1, 2], key="ddr")
    model = st.selectbox("Model (Total credit -2)", options=[0, 1, 2], key="model")
    zero_line = st.selectbox("Zero Line +/- (Total credit -1)", options=[0, 1], key="zero_line")
    entry_model = st.selectbox("Entry Model (Total credit -1)", options=[0, 1], key="entry_model")

    st.subheader("Optional Input")
    trn_options = ['Not Applicable', 0, 1, 2]
    trn = st.selectbox("TRN (Total credit -2) (Optional)", options=trn_options, index=0, key="trn")

    trumpet_options = ['Not Applicable', 0, 1]
    trumpet = st.selectbox("Trumpet High or Low liquidity taken (Total credit -1) (Optional)", options=trumpet_options, index=0, key="trumpet")

    # Calculate for App 1
    base_total_credit_1 = 15
    optional_credit_1 = 0

    if trn != 'Not Applicable':
        optional_credit_1 += 2
    if trumpet != 'Not Applicable':
        optional_credit_1 += 1

    total_possible_credit_1 = base_total_credit_1 + optional_credit_1

    obtained_credit_1 = wdrr + full_set + partial + ddr + model + zero_line + entry_model
    if trn != 'Not Applicable':
        obtained_credit_1 += trn
    if trumpet != 'Not Applicable':
        obtained_credit_1 += trumpet

    percentage_1 = (obtained_credit_1 / total_possible_credit_1) * 100 if total_possible_credit_1 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_1} / {total_possible_credit_1}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Trade Confidence:</b> <span style='color:green;'>{percentage_1:.2f}%</span></h3>", unsafe_allow_html=True)

# ------------------- Calculator 2: Trade Entry Calculator -------------------
with col2:
    st.header("Trade Entry Calculators")

    # Inputs for App 2
    mdrc = st.selectbox("MDRC (Total credit -3)", options=[0, 1, 2, 3], key="mdrc")
    structure = st.selectbox("Structure (Total credit -2)", options=[0, 1, 2], key="structure")
    m7_box = st.selectbox("M7 Box(0.5) (Total credit -2)", options=[0, 1, 2], key="m7_box")
    svp = st.selectbox("SVP (Total credit -1)", options=[0, 1], key="svp")
    bml = st.selectbox("BML (Total credit -1)", options=[0, 1], key="bml")
    mb = st.selectbox("MB (Total credit -1)", options=[0, 1], key="mb")
    db = st.selectbox("DB (Total credit -1)", options=[0, 1], key="db")
    wdrc_mid = st.selectbox("WDRC(Mid) (Total credit -1)", options=[0, 1], key="wdrc_mid")
    drc = st.selectbox("DRC (Total credit -1)", options=[0, 1], key="drc")
    limiter = st.selectbox("Limiter (Total credit -1)", options=[0, 1], key="limiter")
    drib = st.selectbox("Drib (Total credit -1)", options=[0, 1], key="drib")  # Moved Drib here
    ddr_zero = st.selectbox("DDR Zero Line (Total credit -1)", options=[0, 1], key="ddr_zero")
    qx_true_conf = st.selectbox("QX True Conf (Total credit -1)", options=[0, 1], key="qx_true_conf")

    # Calculate for App 2
    base_total_credit_2 = 17  # Already correct
    obtained_credit_2 = (mdrc + structure + m7_box + svp + bml + mb +
                         db + wdrc_mid + drc + limiter + drib +
                         ddr_zero + qx_true_conf)

    percentage_2 = (obtained_credit_2 / base_total_credit_2) * 100 if base_total_credit_2 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_2} / {base_total_credit_2}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Entry Quality:</b> <span style='color:green;'>{percentage_2:.2f}%</span></h3>", unsafe_allow_html=True)
