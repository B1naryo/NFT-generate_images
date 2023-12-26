from PIL import Image
import os
import random
import time

def generate(size=None, generated_images=None):
    x, y = 24, 24
    size = size or 24

    target_dir = 'generatedPixelart'
    target_path = os.getcwd()

    panda_types = ['face1.png', 'face2.png', 'face3.png']
    face_png = os.path.join(target_path, 'face', random.choice(panda_types))

    glasses_chances = 5
    eyes_png = os.path.join(target_path, 'eye', 'eyes5.png' if random.randint(1, 100) <= glasses_chances else f'eyes{random.randint(1, 4)}.png')

    earrings_chances = 25
    ears_png = os.path.join(target_path, 'ear', f'ear{random.randint(2, 4)}.png' if random.randint(1, 100) <= earrings_chances else 'ear1.png')

    mouth_png = os.path.join(target_path, 'mouth', f'mouth{random.randint(1, 7)}.png')
    nose_png = os.path.join(target_path, 'nose', f'nose{random.randint(1, 4)}.png')

    while True:
        # Base image with colored background
        output_image = Image.new('RGB', (size, size), (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))

        # Importing pixelated pngs
        with Image.open(face_png).resize((size, size)) as face:
            with Image.open(eyes_png).resize((size, size)).convert('RGBA') as eyes:
                with Image.open(ears_png).resize((size, size)).convert('RGBA') as ears:
                    with Image.open(mouth_png).resize((size, size)).convert('RGBA') as mouth:
                        with Image.open(nose_png).resize((size, size)).convert('RGBA') as nose:
                            # Adding elements
                            output_image.paste(face, (0, 0))
                            output_image.paste(eyes, (0, 0), eyes)
                            output_image.paste(ears, (0, 0), ears)
                            output_image.paste(mouth, (0, 0), mouth)
                            output_image.paste(nose, (0, 0), nose)

        # Check if the generated image is unique
        file_name = f'{int(time.time())}.png'
        if file_name not in generated_images:
            generated_images.add(file_name)
            print(f"Imagem única gerada: {file_name}")
            break  # Exit the loop if the image is unique

    # Save final image
    file_path = os.path.join(target_path, target_dir, file_name)
    output_image.save(file_path)

    return file_path

def generate_big_image(size=None, n=10, m=10):
    size = size or 24
    x, y = size, size

    target_dir = 'generatedPixelart'
    target_path = os.getcwd()

    generated_images = set()  # Set to keep track of generated image filenames

    # Base image with colored background
    output_image = Image.new('RGB', (x * n, y * m), (255, 255, 255))

    total_images = n * m
    images_generated = 0

    for i in range(n):
        for j in range(m):
            images_generated += 1
            print(f"Gerando imagem {images_generated}/{total_images}...")
            panda_png = generate(size, generated_images)
            panda = Image.open(panda_png)
            output_image.paste(panda, (i * x, j * y))
            panda.close()  # Close the image after use

    file_name = os.path.join(target_path, target_dir, f'family_{int(time.time())}.png')
    output_image.save(file_name)
    print(f"Todas as {total_images} imagens foram geradas com sucesso!")

if __name__ == "__main__":
    generate_big_image(48, 20, 15)
    input("Pressione Enter para continuar...")

