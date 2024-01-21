import streamlit as st

# Function to create a clickable link
def make_clickable(link, text):
    return f"[{text}]({link})"

# Construct Amazon search URLs based on the book titles and authors
def create_amazon_search_url(title, author):
    search_query = '+'.join(title.replace(':', '').replace(',', '').split()) + '+' + '+'.join(author.split())
    return f"https://www.amazon.com/s?k={search_query}"

# Manual data entry with constructed Amazon search URLs and key recommendations
books_data = [
    {
        "Title": "Ending Aging",
        "Author": "Aubrey de Grey",
        "Key Recommendations": "Protein intake; omega-3 fatty acids; fisetin & quercetin; vitamins C & E; coQ10; L-carnitine; ALA; low sugar diet; curcumin & resveratrol; sulforaphane (broccoli); NAD+ precursors; spermidine",
        "Amazon Link": create_amazon_search_url("Ending Aging", "Aubrey de Grey")
    },
    {
        "Title": "Lifespan",
        "Author": "David Sinclair",
        "Key Recommendations": "Resveratrol; blueberries; peanuts; NAD+ precursors; IF; exercise; cold exposure",
        "Amazon Link": create_amazon_search_url("Lifespan", "David Sinclair")
    },
    {
        "Title": "The Longevity Code",
        "Author": "Kris Verburgh",
        "Key Recommendations": "Quercetin (apples, grapes, berries); fisetin (strawberries); resveratrol (grapes, berries)",
        "Amazon Link": create_amazon_search_url("The Longevity Code", "Kris Verburgh")
    },
    {
        "Title": "Juvenescence",
        "Author": "Jim Mellon and Al Chalabi",
        "Key Recommendations": "Fisetin and quercetin",
        "Amazon Link": create_amazon_search_url("Juvenescence", "Jim Mellon Al Chalabi")
    },
    {
        "Title": "The Longevity Diet",
        "Author": "Valter Longo",
        "Key Recommendations": "Low-calorie, low-protein, low-carb, high-fat diet; plant-based diet with fish consumption; IF and time-restricted feeding",
        "Amazon Link": create_amazon_search_url("The Longevity Diet", "Valter Longo")
    },
    {
        "Title": "Time of Our Lives",
        "Author": "Tom Kirkwood",
        "Key Recommendations": "Selenium; Vit C; Vit E; Omega-3; Resveratrol; coQ10; curcumin",
        "Amazon Link": create_amazon_search_url("Time of Our Lives", "Tom Kirkwood")
    },
    {
        "Title": "The Youth Pill",
        "Author": "David Stipp",
        "Key Recommendations": "IR; resveratrol; rapamycin; metformin; astragalus",
        "Amazon Link": create_amazon_search_url("The Youth Pill", "David Stipp")
    },
    {
        "Title": "A Means to an End",
        "Author": "William Clark",
        "Key Recommendations": "Berries; dark chocolate; nuts; green tea; Vit C; Vit E; coQ10",
       
        "Amazon Link": create_amazon_search_url("A Means to an End", "William Clark")
    },
    {
        "Title": "Blue Zones",
        "Author": "Dan Buettner",
        "Key Recommendations": "Plant-based diet; moderate caloric intake ('80% full')",
        "Amazon Link": create_amazon_search_url("Blue Zones", "Dan Buettner")
    },
    {
        "Title": "Transcend",
        "Author": "Ray Kurzweil and Terry Grossman",
        "Key Recommendations": "Cruciferous vegetables; fruits high in antioxidants; water",
        "Amazon Link": create_amazon_search_url("Transcend", "Ray Kurzweil Terry Grossman")
    },
    {
        "Title": "Cracking the Aging Code",
        "Author": "Josh Mitteldorf and Dorion Sagan",
        "Key Recommendations": "Moderate and varied exercise instead of intense; caloric restriction",
        "Amazon Link": create_amazon_search_url("Cracking the Aging Code", "Josh Mitteldorf Dorion Sagan")
    },
    {
        "Title": "Age Later",
        "Author": "Nir Barzilai",
        "Key Recommendations": "Moderate alcohol and coffee consumption; caloric restriction; metformin",
        "Amazon Link": create_amazon_search_url("Age Later", "Nir Barzilai")
    }
]

# Streamlit page setup
st.title('Book Recommendations with Amazon Links')

# Displaying the table with clickable links
for book in books_data:
    st.subheader(book["Title"])
    st.write("Author:", book["Author"])
    st.write("Key Recommendations:", book["Key Recommendations"])
    st.markdown(make_clickable(book["Amazon Link"], "View on Amazon"), unsafe_allow_html=True)
