
from PIL import Image, ImageDraw, ImageFont
import random
from googletrans import Translator
translator = Translator()
xz = 0
yz =0
import math

#output: 'The sky is blue and I like bananas'

# Define the background image path
bg_path = "background.jpeg" #image that is in background, this case its the cat

# Define the messages and fonts
messages = ["I love you", "Marry Me", "Love you honey"]  #what text you want to be in your picture

fonts = [ImageFont.truetype("arial.ttf", 24), ImageFont.truetype("arial.ttf", 18)]

# Define the languages

language_fonts = {
    'Afrikaans': 'Arial',
    'Albanian': 'Arial',
    'Amharic': 'Nyala',
    'Arabic': 'Times New Roman',
    'Armenian': 'Arial',
    'Azerbaijani': 'Arial',
    'Basque': 'Arial',
    'Belarusian': 'Arial',
    'Bengali': 'Vrinda',
    'Bosnian': 'Arial',
    'Bulgarian': 'Arial',
    'Catalan': 'Arial',
    'Corsican': 'Arial',
    'Croatian': 'Arial',
    'Czech': 'Arial',
    'Dutch': 'Arial',
    'English': 'Arial',
    'Esperanto': 'Arial',
    'Estonian': 'Arial',
    'Filipino': 'Arial',
    'Finnish': 'Arial',
    'French': 'Arial',
    'Frisian': 'Arial',
    'Galician': 'Arial',
    'Georgian': 'Sylfaen',
    'German': 'Arial',
    'Greek': 'Arial',
    'Gujarati': 'Shruti',
    'Haitian Creole': 'Arial',
    'Hausa': 'Arial',
    'Hawaiian': 'Arial',
    'Hindi': 'Mangal',
    'Hmong': 'Arial',
    'Hungarian': 'Arial',
    'Icelandic': 'Arial',
    'Igbo': 'Arial',
    'Indonesian': 'Arial',
    'Irish': 'Arial',
    'Italian': 'Arial',
    'Japanese': 'MS Gothic',
    'Javanese': 'Arial',
    'Kannada': 'Tunga',
    'Kazakh': 'Arial',
    'Korean': 'Batang',
    'Kyrgyz': 'Arial',
    'Lao': 'DokChampa',
    'Latin': 'Times New Roman',
    'Latvian': 'Arial',
    'Lithuanian': 'Arial',
    'Luxembourgish': 'Arial',
    'Macedonian': 'Arial',
    'Malagasy': 'Arial',
    'Malay': 'Arial',
    'Malayalam': 'Kartika',
    'Maltese': 'Arial',
    'Maori': 'Arial',
    'Marathi': 'Mangal',
    'Mongolian': 'Arial',
    'Myanmar (Burmese)': 'Myanmar Text',
    'Norwegian': 'Arial',
    'Odia': 'Kalinga',
    'Pashto': 'Arial',
    'Persian': 'Times New Roman',
    'Polish': 'Arial',
    'Portuguese': 'Arial',
    'Punjabi': 'Raavi',
    'Romanian': 'Arial',
    'Russian': 'Arial',
    'Samoan': 'Arial',
    'Scots Gaelic': 'Arial',
    'Serbian': 'Arial',
    'Sesotho': 'Arial',
    'Shona': 'Arial',
    'Sindhi': 'Arial',
    'Slovak': 'Arial',
    'Slovenian': 'Arial',
    'Somali': 'Arial',
    'Spanish': 'Arial',
    'Sundanese': 'Arial',
    'Swahili': 'Arial',
    'Swedish': 'Arial',
    'Tajik': 'Arial',
}


amount_pics = int(input("Amount Of Pictures: "))
amount_per_circle = int(input("Amount of text per 360 circle: "))

for total_count in range(amount_pics):
    filename = "output1.png"


    # Load the background image
    bg_image = Image.open(bg_path)
    # Get the image size
    width, height = bg_image.size

    # Create a draw object
    draw = ImageDraw.Draw(bg_image)

    # Iterate over 30 times to display messages
    change = 100

    center_x = width/2.3 #x of your center of the circle
    center_y = height/2 #y of your center of circle
    radius = 500  #radius of circle
    angle_degrees = 0

    for i in range(amount_per_circle):
        # Select a random message, language, font, and position

        check = False
        while(check==False):
            try:
                message = random.choice(messages)
                language = random.choice(list(language_fonts.keys()))
                size_text= 24 #text size
                font = ImageFont.truetype(f"{(language_fonts[language]).lower()}.ttf", size_text)
                translated = translator.translate(message, dest=language)

            except:
                check=False
                continue
            check =True


        if(check==True):

            angle_degrees += int(360/amount_per_circle)
            angle_radians = math.radians(angle_degrees)  #you can change the formula for different patterns, here i use circle
            x = center_x + radius * math.cos(angle_radians)
            y = center_y + radius * math.sin(angle_radians)


            draw.text((x, y), f"{translated.text}", font=font, fill=(0, 0, 0))

        # Draw the message on the image

    # Display the image
    bg_image.show()
    filename = f"{filename[0:6]+str(total_count+1)}.png"
    print(filename)
    bg_image.save(fp=filename)
