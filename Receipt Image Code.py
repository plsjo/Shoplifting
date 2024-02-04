import cv2
import pytesseract
import openai
import pandas as pd

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\lin23\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract'

# Read image from which text needs to be extracted
img = cv2.imread("Sweet_Mama.jpeg")

# Preprocessing the image starts
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Sort contours from top to bottom and left to right
contours = sorted(contours, key=lambda x: (cv2.boundingRect(x)[1], cv2.boundingRect(x)[0]))

# Create a dictionary to store item and price pairs
item_price_dict = {}

# Loop through the identified contours
for idx, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    cropped = img[y:y + h, x:x + w]

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped).strip()

    # Determine if the text is an item or a price
    if idx % 2 == 0:  # Even index corresponds to item
        item_price_dict[f'Item {idx // 2 + 1}'] = {'item': text}
    else:  # Odd index corresponds to price
        item_price_dict[f'Item {idx // 2 + 1}']['price'] = text

# Get the number of people to split the cost
num_people = int(input("Enter the number of people to split the cost among: "))

# Calculate the evenly split cost per person
for key, value in item_price_dict.items():
    price = float(value.get('price', 0))
    value['even_split'] = price / num_people if num_people > 0 else 0

# Construct a message for the OpenAI API
message = f"Create a table with items, prices, and evenly split amounts for {num_people} people:\n\n"
for key, value in item_price_dict.items():
    item = value['item']
    price = value.get('price', 'N/A')  # Use 'N/A' if price is not available
    even_split = value.get('even_split', 'N/A')  # Use 'N/A' if even_split is not available
    message += f"| {item} | {price} | {even_split} |\n"

# Set your OpenAI API key
openai.api_key = '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'

# Use the chat/completions endpoint for ChatGPT Turbo
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
)

# Extract and print the generated completion
completion = response['choices'][0]['message']['content'].strip()
hdr_seen = False
data = []
for row in completion.split('\n'):
    if '|' in row and '-' not in row:
        if not hdr_seen:
            hdr_seen = True
        else:
            data.append([k.strip() for k in row.split('|') if k!=''])

df = pd.DataFrame(data=data, columns=['item', 'cost', 'even_split'])
print(df)
