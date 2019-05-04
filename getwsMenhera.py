import requests
import re
import PIL.Image as Image
from os import listdir, mkdir, remove

rep = re.compile(r'https://[A-z]+[0-9].sinaimg.cn/large/')


def main():
    s = set()
    for i in range(300):
        response = requests.get('https://api.ixiaowai.cn/mcapi/mcapi.php', allow_redirects=False)
        s.add(response.headers['Location'])

    with open('img_url.txt', 'a+', encoding='utf-8') as f:
        for i in s:
            f.write(i + '\n')


def get_img():
    global rep
    lst = []
    with open('img_url.txt', 'r') as f:
        for line in f.readlines():
            lst.append(line.strip('\n'))

    for i in lst:
        r = requests.get(i)
        print('get: ' + i)
        with open('img/' + re.sub(rep, '', i), 'wb+') as f:
            f.write(r.content)


def convert_background(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


def files_convert(dir):
    s = listdir(dir)
    num = 0
    try:
        mkdir('convert')
    except FileExistsError:
        pass
    for i in s:
        try:
            img = Image.open(dir + '/' + i)
        except OSError:
            pass
        else:
            img = convert_background(img)
            img.save('convert/' + str(num) + '.png', quality=50)
            print('Convert: ' + i)
            num += 1


if __name__ == '__main__':
    main()
    get_img()
    files_convert('img')
    try:
        remove('img_url.txt')
    except:
        pass
