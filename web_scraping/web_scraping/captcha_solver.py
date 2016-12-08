from PIL import Image

def ocr(im, threshold=200, alphabet="0123456789abcdef"):
    img = Image.open(im)
    img = img.convert("RGB")
    box = (8, 8, 58, 18)
    img = img.crop(box)
    pixdata = img.load()

    letters = Image.open('letters.bmp')
    ledata = letters.load()

    # Clean the background noise, if color != white, then set to black.
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if (pixdata[x, y][0] > threshold) \
                    and (pixdata[x, y][1] > threshold) \
                    and (pixdata[x, y][2] > threshold):

                pixdata[x, y] = (255, 255, 255, 255)
            else:
                pixdata[x, y] = (0, 0, 0, 255)

    counter = 0;
    old_x = -1;

    letterlist = []

    for x in range(letters.size[0]):
        black = True
        for y in range(letters.size[1]):
            if ledata[x, y][0] <> 0 :
                black = False
                break
        if black :
            if True :
                box = (old_x + 1, 0, x, 10)
                letter = letters.crop(box)
                t = p(img, letter);
                print counter, x, t
                letterlist.append((t[0], alphabet[counter], t[1]))
            old_x = x
            counter += 1

    box = (old_x + 1, 0, 140, 10)
    letter = letters.crop(box)
    t = p(img, letter)
    letterlist.append((t[0], alphabet[counter], t[1]))

    t = sorted(letterlist)
    t = t[0:5]  # 5-letter captcha

    final = sorted(t, key=lambda e: e[2])
    answer = ""
    for l in final:
        answer = answer + l[1]
    return answer

print(ocr(sys.argv[1]))