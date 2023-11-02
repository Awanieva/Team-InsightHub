import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('ridge_model.pkl', 'rb'))

def main():
    st.title("Cereal Ratings")

    activities = ["Introduction", "Predictions"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    st.sidebar.markdown(
            """ Developed by Team InsightHub
                """)

    if choice == "Introduction":
        html_temp_home1 = """<div style="background-color:#00CCFF;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Cereal Rating Prediction Using Machine Learning Model
                                            </h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
    
        st.write("""
                 - This project delves into the intricate relationship between different cereals bla bla
            """)
        st.write("""
                 # Team members
                - Confidence Chinelo Ojiako (Project Lead)
                - (Assistant project lead)
                - (Query Analyst)
                - Isaac Ndirangu Muturi
                - Mobki Markus 
                - Anubha Jarwal 
                 
                 """)
            
    elif choice == "Predictions":
        st.subheader("Prediction")
    
#Input Variable
    calories = st.number_input('Calories')
    protein = st.number_input('protein')
    fat =  st.number_input('fat')
    sodium = st.number_input('sodium')
    fiber  = st.number_input  ('fiber')
    carbo  = st.number_input  ('carbo')
    sugars  = st.number_input  ('sugars')
    vitamins  = st.number_input  ('vitamins')
    shelf  = st.number_input  ('shelf')
    weight  = st.number_input  ('weight')
    cups  = st.number_input  ('cups')
    type_C  = st.number_input  ('type_C')
    type_H  = st.number_input  ('type_H')
    
    
    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[calories, protein, fat, sodium, fiber,carbo, sugars, vitamins, shelf,
                                         weight, cups, type_C, type_H]])
        output = round(makeprediction[0],2)
        st.success('The Rating for this Cereal is {}'.format(output))
if __name__ == '__main__':
        main()