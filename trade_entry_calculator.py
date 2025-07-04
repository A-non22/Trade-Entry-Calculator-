import streamlit as st

st.set_page_config(page_title="Trade Scenarios", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>Trade Scenarios</h1>",
    unsafe_allow_html=True
)

# Create two columns for Scenario 1 and Scenario 2
col1, col2 = st.columns(2)

# ------------------- SCENARIO 1 -------------------
with col1:
    st.header("Trade Confidence Calculator (Scenario 1 - Long)")

    # Trade Confidence Calculator Inputs (Scenario 1)
    wdrr1 = st.selectbox("WDRR (Total credit -3)", options=[0, 1, 2, 3], key="wdrr1")
    full_set1 = st.selectbox("Full Set (Total credit -3)", options=[0, 1, 2, 3], key="full_set1")
    ddr1 = st.selectbox("DDR (Total credit -2)", options=[0, 1, 2], key="ddr1")
    model1 = st.selectbox("Model (Total credit -2)", options=[0, 1, 2], key="model1")
    zero_line1 = st.selectbox("Zero Line +/- (Total credit -1)", options=[0, 1], key="zero_line1")
    entry_model1 = st.selectbox("Entry Model (Total credit -1)", options=[0, 1], key="entry_model1")

    st.subheader("Optional Input")
    partial_options = ['Not Applicable', 0, 1]
    partial1 = st.selectbox("Partial (Total credit -1) (Optional)", options=partial_options, index=0, key="partial1")

    trn_options = ['Not Applicable', 0, 1, 2]
    trn1 = st.selectbox("TRN (Total credit -2) (Optional)", options=trn_options, index=0, key="trn1")

    trumpet_options = ['Not Applicable', 0, 1]
    trumpet1 = st.selectbox("Trumpet High or Low liquidity taken (Total credit -1) (Optional)", options=trumpet_options, index=0, key="trumpet1")

    base_total_credit_1 = 14  # reduced from 15 to 14 since Partial moved from mandatory to optional
    optional_credit_1 = 0
    if partial1 != 'Not Applicable':
        optional_credit_1 += 1
    if trn1 != 'Not Applicable':
        optional_credit_1 += 2
    if trumpet1 != 'Not Applicable':
        optional_credit_1 += 1
    total_possible_credit_1 = base_total_credit_1 + optional_credit_1

    obtained_credit_1 = wdrr1 + full_set1 + ddr1 + model1 + zero_line1 + entry_model1
    if partial1 != 'Not Applicable':
        obtained_credit_1 += partial1
    if trn1 != 'Not Applicable':
        obtained_credit_1 += trn1
    if trumpet1 != 'Not Applicable':
        obtained_credit_1 += trumpet1

    percentage_1 = (obtained_credit_1 / total_possible_credit_1) * 100 if total_possible_credit_1 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_1} / {total_possible_credit_1}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Trade Confidence:</b> <span style='color:green;'>{percentage_1:.2f}%</span></h3>", unsafe_allow_html=True)

    st.header("Trade Entry Calculator (Scenario 1 - Long)")

    # Trade Entry Calculator Inputs (Scenario 1)
    mdrc1 = st.selectbox("MDRC (Total credit -3)", options=[0, 1, 2, 3], key="mdrc1")
    structure1 = st.selectbox("Structure (Total credit -2)", options=[0, 1, 2], key="structure1")
    m7_box1 = st.selectbox("M7 Box(0.5) (Total credit -2)", options=[0, 1, 2], key="m7_box1")
    svp1 = st.selectbox("SVP (Total credit -1)", options=[0, 1], key="svp1")
    bml1 = st.selectbox("BML (Total credit -1)", options=[0, 1], key="bml1")
    mb1 = st.selectbox("MB (Total credit -1)", options=[0, 1], key="mb1")
    db1 = st.selectbox("DB (Total credit -1)", options=[0, 1], key="db1")
    wdrc_mid1 = st.selectbox("WDRC(Mid) (Total credit -1)", options=[0, 1], key="wdrc_mid1")
    drc1 = st.selectbox("DRC (Total credit -1)", options=[0, 1], key="drc1")
    limiter1 = st.selectbox("Limiter (Total credit -1)", options=[0, 1], key="limiter1")
    drib1 = st.selectbox("Drib (Total credit -1)", options=[0, 1], key="drib1")
    ddr_zero1 = st.selectbox("DDR Zero Line (Total credit -1)", options=[0, 1], key="ddr_zero1")
    qx_true_conf1 = st.selectbox("QX True Conf (Total credit -1)", options=[0, 1], key="qx_true_conf1")

    base_total_credit_2 = 17
    obtained_credit_2 = (mdrc1 + structure1 + m7_box1 + svp1 + bml1 + mb1 +
                         db1 + wdrc_mid1 + drc1 + limiter1 + drib1 +
                         ddr_zero1 + qx_true_conf1)

    percentage_2 = (obtained_credit_2 / base_total_credit_2) * 100 if base_total_credit_2 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_2} / {base_total_credit_2}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Entry Quality:</b> <span style='color:green;'>{percentage_2:.2f}%</span></h3>", unsafe_allow_html=True)

# ------------------- SCENARIO 2 -------------------
with col2:
    st.header("Trade Confidence Calculator (Scenario 2 - Short)")

    # Trade Confidence Calculator Inputs (Scenario 2)
    wdrr2 = st.selectbox("WDRR (Total credit -3)", options=[0, 1, 2, 3], key="wdrr2")
    full_set2 = st.selectbox("Full Set (Total credit -3)", options=[0, 1, 2, 3], key="full_set2")
    ddr2 = st.selectbox("DDR (Total credit -2)", options=[0, 1, 2], key="ddr2")
    model2 = st.selectbox("Model (Total credit -2)", options=[0, 1, 2], key="model2")
    zero_line2 = st.selectbox("Zero Line +/- (Total credit -1)", options=[0, 1], key="zero_line2")
    entry_model2 = st.selectbox("Entry Model (Total credit -1)", options=[0, 1], key="entry_model2")

    st.subheader("Optional Input")
    partial2 = st.selectbox("Partial (Total credit -1) (Optional)", options=partial_options, index=0, key="partial2")
    trn2 = st.selectbox("TRN (Total credit -2) (Optional)", options=trn_options, index=0, key="trn2")
    trumpet2 = st.selectbox("Trumpet High or Low liquidity taken (Total credit -1) (Optional)", options=trumpet_options, index=0, key="trumpet2")

    optional_credit_3 = 0
    if partial2 != 'Not Applicable':
        optional_credit_3 += 1
    if trn2 != 'Not Applicable':
        optional_credit_3 += 2
    if trumpet2 != 'Not Applicable':
        optional_credit_3 += 1
    total_possible_credit_3 = base_total_credit_1 + optional_credit_3

    obtained_credit_3 = wdrr2 + full_set2 + ddr2 + model2 + zero_line2 + entry_model2
    if partial2 != 'Not Applicable':
        obtained_credit_3 += partial2
    if trn2 != 'Not Applicable':
        obtained_credit_3 += trn2
    if trumpet2 != 'Not Applicable':
        obtained_credit_3 += trumpet2

    percentage_3 = (obtained_credit_3 / total_possible_credit_3) * 100 if total_possible_credit_3 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_3} / {total_possible_credit_3}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Trade Confidence:</b> <span style='color:green;'>{percentage_3:.2f}%</span></h3>", unsafe_allow_html=True)

    st.header("Trade Entry Calculator (Scenario 2 - Short)")

    # Trade Entry Calculator Inputs (Scenario 2)
    mdrc2 = st.selectbox("MDRC (Total credit -3)", options=[0, 1, 2, 3], key="mdrc2")
    structure2 = st.selectbox("Structure (Total credit -2)", options=[0, 1, 2], key="structure2")
    m7_box2 = st.selectbox("M7 Box(0.5) (Total credit -2)", options=[0, 1, 2], key="m7_box2")
    svp2 = st.selectbox("SVP (Total credit -1)", options=[0, 1], key="svp2")
    bml2 = st.selectbox("BML (Total credit -1)", options=[0, 1], key="bml2")
    mb2 = st.selectbox("MB (Total credit -1)", options=[0, 1], key="mb2")
    db2 = st.selectbox("DB (Total credit -1)", options=[0, 1], key="db2")
    wdrc_mid2 = st.selectbox("WDRC(Mid) (Total credit -1)", options=[0, 1], key="wdrc_mid2")
    drc2 = st.selectbox("DRC (Total credit -1)", options=[0, 1], key="drc2")
    limiter2 = st.selectbox("Limiter (Total credit -1)", options=[0, 1], key="limiter2")
    drib2 = st.selectbox("Drib (Total credit -1)", options=[0, 1], key="drib2")
    ddr_zero2 = st.selectbox("DDR Zero Line (Total credit -1)", options=[0, 1], key="ddr_zero2")
    qx_true_conf2 = st.selectbox("QX True Conf (Total credit -1)", options=[0, 1], key="qx_true_conf2")

    obtained_credit_4 = (mdrc2 + structure2 + m7_box2 + svp2 + bml2 + mb2 +
                         db2 + wdrc_mid2 + drc2 + limiter2 + drib2 +
                         ddr_zero2 + qx_true_conf2)

    percentage_4 = (obtained_credit_4 / base_total_credit_2) * 100 if base_total_credit_2 > 0 else 0

    st.header("Results")
    st.markdown(f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_4} / {base_total_credit_2}</span></h3>", unsafe_allow_html=True)
    st.markdown(f"<h3><b>Entry Quality:</b> <span style='color:green;'>{percentage_4:.2f}%</span></h3>", unsafe_allow_html=True)
