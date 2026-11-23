import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Rural Solutions Platform",
    page_icon="🌍",
    layout="wide"
)

# Sample Data
if "equipment" not in st.session_state:
    st.session_state.equipment = [
        {
            "Equipment": "Tractor",
            "Owner": "Ramesh",
            "Contact": "9876543210",
            "Rent": 1500
        },
        {
            "Equipment": "Rotavator",
            "Owner": "Suresh",
            "Contact": "9123456780",
            "Rent": 1000
        },
        {
            "Equipment": "Seed Drill",
            "Owner": "Mahesh",
            "Contact": "9988776655",
            "Rent": 800
        }
    ]

if "food" not in st.session_state:
    st.session_state.food = [
        {
            "Donor": "ABC Function Hall",
            "Food": "Veg Biryani",
            "Quantity": 150,
            "Location": "Guntur"
        },
        {
            "Donor": "Sai Hotel",
            "Food": "Meals",
            "Quantity": 80,
            "Location": "Vijayawada"
        }
    ]

database = {
    "Paracetamol": "Used for fever and pain relief.",
    "Amoxicillin": "Antibiotic used for bacterial infections.",
    "Cetirizine": "Used to treat allergies.",
    "Pantoprazole": "Used for acidity and gastric issues.",
    "Ibuprofen": "Used for pain and inflammation.",
    "Azithromycin": "Used to treat respiratory infections."
}

st.title("🌍 Smart Rural Solutions Platform")
st.subheader("Agriculture • Food Management • Healthcare")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "🏠 Home",
        "🚜 AgriRent",
        "🍛 Food Rescue",
        "💊 MediTranslate"
    ]
)

# HOME
if module == "🏠 Home":

    st.header("Welcome")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🚜 AgriRent\n\nEquipment Sharing Platform")

    with col2:
        st.success("🍛 Food Rescue\n\nFood Donation Platform")

    with col3:
        st.warning("💊 MediTranslate\n\nMedicine Information Assistant")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Registered Equipment", len(st.session_state.equipment))

    with c2:
        total_food = sum(
            item["Quantity"]
            for item in st.session_state.food
        )
        st.metric("Food Portions Available", total_food)

    with c3:
        st.metric("Medicines Supported", len(database))

# AGRIRENT
elif module == "🚜 AgriRent":

    st.header("🚜 AgriRent")

    option = st.radio(
        "Choose",
        ["Add Equipment", "Browse Equipment"]
    )

    if option == "Add Equipment":

        equipment_name = st.text_input("Equipment Name")
        owner_name = st.text_input("Owner Name")
        contact = st.text_input("Contact Number")
        rent = st.number_input(
            "Rent Per Day",
            min_value=0
        )

        if st.button("Add Equipment"):

            st.session_state.equipment.append(
                {
                    "Equipment": equipment_name,
                    "Owner": owner_name,
                    "Contact": contact,
                    "Rent": rent
                }
            )

            st.success("Equipment Added Successfully")

    else:

        df = pd.DataFrame(
            st.session_state.equipment
        )

        st.dataframe(df)

        st.subheader("Equipment Details")

        for item in st.session_state.equipment:
            with st.expander(item["Equipment"]):
                st.write("Owner:", item["Owner"])
                st.write("Contact:", item["Contact"])
                st.write("Rent Per Day: ₹", item["Rent"])

# FOOD RESCUE
elif module == "🍛 Food Rescue":

    st.header("🍛 Food Rescue")

    option = st.radio(
        "Choose",
        ["Donate Food", "Available Donations"]
    )

    if option == "Donate Food":

        donor = st.text_input(
            "Hotel / Function Name"
        )

        food_item = st.text_input(
            "Food Item"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1
        )

        location = st.text_input(
            "Location"
        )

        if st.button("Donate Food"):

            st.session_state.food.append(
                {
                    "Donor": donor,
                    "Food": food_item,
                    "Quantity": quantity,
                    "Location": location
                }
            )

            st.success("Donation Added Successfully")

    else:

        df = pd.DataFrame(
            st.session_state.food
        )

        st.dataframe(df)

        total = sum(
            item["Quantity"]
            for item in st.session_state.food
        )

        st.success(
            f"Potential Meals Saved: {total}"
        )

# MEDITRANSLATE
elif module == "💊 MediTranslate":

    st.header("💊 MediTranslate")

    medicine = st.text_input(
        "Enter Medicine Name"
    )

    if st.button("Explain Medicine"):

        if medicine in database:

            st.success(
                database[medicine]
            )

        else:

            st.warning(
                "Medicine not found."
            )

    st.markdown("---")

    st.subheader(
        "Medicine Database"
    )

    for med, desc in database.items():
        st.write(
            f"✅ {med} - {desc}"
        )

    st.info(
        "For educational purposes only."
    ) 
