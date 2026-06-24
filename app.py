import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="AI-Assisted Underwriting System",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.metric-card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

.big-font {
    font-size:24px !important;
    font-weight:bold;
}

.stButton>button {
    background-color:#0A4D9C;
    color:white;
    border-radius:8px;
    width:100%;
}

</style>
""", unsafe_allow_html=True)



# ----------------------------
# HEADER
# ----------------------------

st.title("🏦 AI-Assisted Framework for Credit Risk Assessment and Automated Underwriting")

st.markdown("---")

# ----------------------------
# APPLICANT INFORMATION
# ----------------------------

st.header("Applicant Information Entry")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    annual_income = st.number_input(
        "Annual Income (₹)",
        min_value=0,
        value=600000
    )

    employment_status = st.selectbox(
        "Employment Status",
        [
            "Salaried",
            "Self-Employed",
            "Business Owner",
            "Unemployed"
        ]
    )

    years_employment = st.number_input(
        "Years of Employment",
        min_value=0,
        value=5
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=700
    )

with col2:

    existing_loan = st.number_input(
        "Existing Loan Amount (₹)",
        min_value=0,
        value=100000
    )

    dti = st.slider(
        "Debt-to-Income Ratio (%)",
        0,
        100,
        30
    )

    number_loans = st.number_input(
        "Number of Existing Loans",
        min_value=0,
        value=1
    )

    previous_defaults = st.number_input(
        "Previous Loan Defaults",
        min_value=0,
        value=0
    )

    loan_amount = st.number_input(
        "Loan Amount Requested (₹)",
        min_value=0,
        value=500000
    )

loan_purpose = st.selectbox(
    "Loan Purpose",
    [
        "Home Loan",
        "Personal Loan",
        "Education Loan",
        "Vehicle Loan",
        "Business Loan"
    ]
)
# ----------------------------
# BUTTON
# ----------------------------

if st.button("Evaluate Application"):

    # ----------------------------
    # PROCESSING SCREEN
    # ----------------------------

    with st.spinner("Validating applicant information..."):
        pass

    with st.spinner("Running AI credit risk assessment..."):
        pass

    with st.spinner("Generating underwriting recommendation..."):
        pass

    # ----------------------------
    # SIMPLE RULE-BASED LOGIC
    # ----------------------------

    risk_score = 50

    risk_score += (credit_score - 600) / 5

    if dti > 50:
        risk_score -= 20

    elif dti > 35:
        risk_score -= 10

    risk_score -= previous_defaults * 10

    risk_score = max(0, min(100, int(risk_score)))

    # ----------------------------
    # RISK CATEGORY
    # ----------------------------

    if risk_score >= 80:
        risk_category = "Low Risk"
        recommendation = "Approve"

    elif risk_score >= 50:
        risk_category = "Medium Risk"
        recommendation = "Manual Review"

    else:
        risk_category = "High Risk"
        recommendation = "Reject"

    #-----------------------------
    #APPLICATION SUMMARY
    # ----------------------------
    
        st.subheader("Applicant Summary")

    summary = pd.DataFrame({

        "Field":[
            "Age",
            "Annual Income",
            "Credit Score",
            "DTI Ratio",
            "Previous Defaults"
        ],

        "Value":[
            age,
            annual_income,
            credit_score,
            f"{dti}%",
            previous_defaults
        ]

    })

    st.table(summary)

    #------------------------
    #DASHBOARD
    #----------------------

    st.markdown("---")
    st.header("Underwriting Recommendation Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Credit Risk Score", risk_score)
    c2.metric("Risk Category", risk_category)
    c3.metric("AI Recommendation", recommendation)

    st.subheader("Key Contributing Factors")

    factors = []

    if credit_score >= 750:
        factors.append("✓ Strong Credit Score")

    elif credit_score < 600:
        factors.append("✗ Low Credit Score")

    if dti < 30:
        factors.append("✓ Low Debt-to-Income Ratio")

    elif dti > 50:
        factors.append("✗ High Debt-to-Income Ratio")

    if previous_defaults == 0:
        factors.append("✓ No Previous Defaults")

    else:
        factors.append("✗ Previous Defaults Present")

    for factor in factors:
        st.write(factor)

    #---------------------------
    #GAUGE CHART
    # ----------------------------

        fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=risk_score,

        title={
            'text':"Credit Risk Score"
        },

        gauge={

            'axis':{
                'range':[0,100]
            },

            'bar':{
                'color':"#0A4D9C"
            },

            'steps':[

                {
                    'range':[0,50],
                    'color':'#ffcccc'
                },

                {
                    'range':[50,80],
                    'color':'#fff0b3'
                },

                {
                    'range':[80,100],
                    'color':'#ccffcc'
                }
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    #----------------------------
    # AI RECOMMENDATION BANNER
    #----------------------------
    if recommendation == "Approve":

        st.success(
            "AI Recommendation: APPROVE"
        )

    elif recommendation == "Manual Review":

        st.warning(
            "AI Recommendation: MANUAL REVIEW"
        )

    else:

        st.error(
            "AI Recommendation: REJECT"
        )
    
    #---------------------------
    # EXPLAINABILITY SECTION
    #-----------------------------

        st.subheader(
        "Top Contributing Factors"
    )

    explainability = {

        "Credit Score":35,

        "Income Stability":25,

        "Debt-to-Income Ratio":-20,

        "Previous Defaults":-15,

        "Employment History":10
    }

    for factor,value in explainability.items():

        st.progress(
            abs(value)/40
        )

        st.write(
            f"{factor}: {value}% impact"
        )

    #------------------------------
    # HUMAN-IN-THE-LOOP
    # ----------------------------

    st.markdown("---")
    st.header(
        "Human Underwriter Review"
    )

    decision = st.selectbox(

        "Select Final Decision",

        [

            "Accept Recommendation",

            "Request Additional Review",

            "Reject Application"

        ]
    )

    comments = st.text_area(
        "Underwriter Comments"
    )
    

    if st.button(
        "Submit Final Decision"
    ):

        st.success(
            "Decision Submitted Successfully"
        )

        st.write(
            "### Decision Summary"
        )

        st.write(
            "AI Recommendation:",
            recommendation
        )

        st.write(
            "Underwriter Decision:",
            decision
        )

        st.write(
            "Comments:",
            comments
        )

        st.balloons()