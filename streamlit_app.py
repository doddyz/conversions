import streamlit as st

INGREDIENTS_GRAMS_WEIGHT = {'Flour': 120, 'Flour (sieved)': 110, 'Sugar (granulated)': 200, 'Icing Sugar': 100, 'Brown Sugar': 180, 'Cornflour (corn starch)': 120, 'Rice (uncooked)': 190, 'Couscous (uncooked)': 180, 'Oats (uncooked)': 90, 'Table Salt': 300, 'Butter': 240, 'Vegetable Shortening': 190, 'Nuts (chopped)': 150, 'Nuts (ground)': 120, 'Breadcrumbs (fresh)': 60, 'Breadcrumbs (dry)': 150, 'Sultanas / Raisins': 200}

INGREDIENTS = INGREDIENTS_GRAMS_WEIGHT.keys()

CUPS_RANGE = [1/4, 1/3, 1/2, 2/3, 3/4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_of_cups = st.sidebar.select_slider("# of Cup(s)", CUPS_RANGE)

ingredient = st.sidebar.selectbox("Pick ingredient", INGREDIENTS)

ingredient_weight_in_grams = number_of_cups * INGREDIENTS_GRAMS_WEIGHT[ingredient]

st.metric(label="Weight in Grams", value=int(ingredient_weight_in_grams))
