
import img2pdf
import os


def main():
    files = [file for file in os.listdir()]
    images = []
    for file in files:
        head, tail = os.path.splitext(file)
        if tail.lower() not in {'.jpeg', '.jpg'}:
            continue
        images.append(file)
    with open('gradbeno_dovoljenje.pdf', 'wb') as file:
        file.write(img2pdf.convert(images))


if __name__ == '__main__':
    main()
