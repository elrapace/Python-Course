import PIL, sys, datetime
from PIL import Image

if len(sys.argv) > 1:
    print(f'IMAGE: {sys.argv[1]}')
else:
    print('NO IMAGE! INSERT IMAGE TO COMPRESS')
    sys.exit(1)

g_originale_image = sys.argv[1]
g_extension = g_originale_image.split('.')[1]

with Image.open(g_originale_image) as image:
    image_height = image.height
    image_width = image.width

    print(f'THE ORIGINAL SIZE OF IMAGE IS: {round(len(image.fp.read())/1024,2)} KB')

    l_image = image.resize((image_width,image_height), PIL.Image.NEAREST)

    l_compressed_image = 'compressed_image_' + str(datetime.date.today()) + '.' + g_extension
    l_image.save(l_compressed_image, optimize=True, compress_level=9)

    with Image.open(l_compressed_image) as compressed_image:
        print(f'THE SIZE OF COMPRESSED IMAGE IS: {round(len(compressed_image.fp.read())/1024,2)} KB')