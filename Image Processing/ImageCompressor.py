from PIL import Image
import io

def compress_image_accurate(input_path, output_path, max_size=50000, quality=100, step=10):
    img = Image.open(input_path)
    width, height = img.size
    print(width, height)
    img_byte_arr = io.BytesIO()
    img.thumbnail((width, height))
    img.save(img_byte_arr, format='JPEG', quality=quality)
    img_byte_arr = img_byte_arr.getvalue()
    x, y = (width, height)
    while len(img_byte_arr) > max_size:
        print("loading...")
        img = Image.open(io.BytesIO(img_byte_arr))
        img_byte_arr = io.BytesIO()
        img.thumbnail((x, y))
        img.save(img_byte_arr, format='JPEG', quality=quality)
        x -= step
        y -= step
        img_byte_arr = img_byte_arr.getvalue()
        if x <= 0 or y <= 0:
            break
    if len(img_byte_arr) > max_size:
        # The image could not be compressed to the desired size
        # Return the original image instead
        img = Image.open(input_path)
        img.save(output_path)
    else:
        with open(output_path, 'wb') as f:
            f.write(img_byte_arr)

def compress_image_low_size(input_path, output_path, max_size, quality=100, step=10):
    img = Image.open(input_path)
    width = height = 1000
    print(width, height)
    img_byte_arr = io.BytesIO()
    img.thumbnail((width, height))
    img.save(img_byte_arr, format='JPEG', quality=quality)
    img_byte_arr = img_byte_arr.getvalue()
    x, y = (width, height)
    while len(img_byte_arr) > max_size:
        print("loading...")
        img = Image.open(io.BytesIO(img_byte_arr))
        img_byte_arr = io.BytesIO()
        img.thumbnail((x, y))
        img.save(img_byte_arr, format='JPEG', quality=quality)
        x -= step
        y -= step
        img_byte_arr = img_byte_arr.getvalue()
        if x <= 0 or y <= 0:
            break
    if len(img_byte_arr) > max_size:
        # The image could not be compressed to the desired size
        # Return the original image instead
        img = Image.open(input_path)
        img.save(output_path)
    else:
        with open(output_path, 'wb') as f:
            f.write(img_byte_arr)


input_path = 'input.jpg'
output_path = 'output.jpg'
max_size = 3000000
compress_image_accurate(input_path, output_path, max_size)
