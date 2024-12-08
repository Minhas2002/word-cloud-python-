from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

mask_image = np.array(Image.open('CSE_64_K.png'))

with open('CSE_64_K.txt', 'r', encoding='utf-8') as file:
    text = file.read()

wordcloud = WordCloud(
    mask=mask_image,
    contour_color='#2A3439',
    contour_width=2,
    background_color='black',
    width=800, height=800,
    max_words=500,
    colormap='coolwarm'
).generate(text)


plt.figure(figsize=(50, 50))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
