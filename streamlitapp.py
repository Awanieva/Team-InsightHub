import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('ridge_model.pkl', 'rb'))

def main():
    st.title("Cereal Ratings")

    activities = ["About the Project", "Predictions"]
    # Set the default choice to "Predictions"
    choice = st.sidebar.selectbox("Select Activity", activities, index=1)
    
    st.sidebar.markdown(
            """ Developed by Team InsightHub
                """)

    if choice == "About the Project":
        html_temp_home1 = """<div style="background-color:#00CCFF;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Cereal Rating Prediction Using Machine Learning Model
                                            </h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
    
        st.write("""
                 To simplify cereal selection by analyzing nutritional content, categorize cereals as ‘Healthy’ or ‘Unhealthy’ and predict consumer ratings.

            """)
        st.write("""
        # Team members
            - Confidence Chinelo Ojiako (Project Lead)
            - Godwin Valentine (Assistant project lead)
            - Feranmi Olufunminiyi(Query Analyst)
            - Anubha Jarwal 
            - Horeb Nesimone
            - Isaac Ndirangu Muturi
            - Mobki Markus
            - Enemuo Echezonachukwu 
            - Morufdeen Atilola
            - Owolabi Israel
            - Monjok Joseph Terem
            - Anne Pet-Ameh
                 
                 """)
            
    elif choice == "Predictions":
        st.subheader("Prediction")
    
        # Input Variable (... your input fields ...)
        calories = st.number_input('Calories')
        protein = st.number_input('protein')
        fat =  st.number_input('fat')
        sodium = st.number_input('sodium')
        fiber  = st.number_input  ('fiber')
        carbo  = st.number_input  ('carbo')
        sugars  = st.number_input  ('sugars')
        vitamins  = st.number_input  ('vitamins')
        weight  = st.number_input  ('weight')
        cups  = st.number_input  ('cups')
        Cereal_Type_Cold = st.number_input('Cereal Type (Cold)', min_value=0, max_value=0, step=1, format="%d", help='Select 0 if cereal type is eaten Cold')
        Cereal_Type_Hot = st.number_input('Cereal Type (Hot)', min_value=0, max_value=1, step=1, format="%d", help='Select 1 if cereal type is eaten Hot, Select 0 if cereal type is not eaten Hot')

        #prediction code
        if st.button('Predict'):
            makeprediction = model.predict([[calories, protein, fat, sodium, fiber,carbo, sugars, vitamins,
                                             weight, cups, Cereal_Type_Cold, Cereal_Type_Hot]])
            output = round(makeprediction[0],2)
            st.success('The Rating for this Cereal is {}'.format(output))

if __name__ == '__main__':
        main()