import streamlit as st

st.set_page_config(page_title="Hypotheses & Validation", layout="wide")
st.title("Hypotheses & Validation")

hypotheses = {
    1: ("Weather & Historical Climate Effects", "Each climate component independently influences disease incidence."),
    2: ("System-Type Sensitivity", "Wild systems have stronger climate-disease links than agricultural."),
    3: ("Thermal & Precipitation Mismatch", "Disease peaks when weather deviates from norms in wild systems."),
    4: ("Agricultural Resilience", "Crops show reduced mismatch effects due to management."),
    5: ("Geographic & Pathogen Modulation", "Pathogen identity modulates climate-disease relationships.")
}
for num, (title, desc) in hypotheses.items():
    with st.expander(f"Hypothesis {num}: {title}"):
        st.write(desc)
        st.image(f"https://via.placeholder.com/600x300.png?text=Validation+Plot+{num}", use_column_width=True)