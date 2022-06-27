"""
Copyright 2022 Ali Azam. All rights reserved.
Use of this source code is governed under the MIT
license that can be found in the LICENSE file.
"""

import random

from PIL import Image, ImageDraw
from hashlib import md5, sha1, blake2b
from string import hexdigits

_MD5   = lambda x: md5(x.encode()).hexdigest()
_SHA   = lambda x: sha1(x.encode()).hexdigest()
_BLAKE = lambda x: blake2b(x.encode()).hexdigest()

def _square(image, x, y, block, pad, colour):
    x = x * block + pad
    y = y * block + pad
	
    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x + block, y + block), fill=colour)

def identicon(seed, width=420, pad=0.12, invert=False, hasher='md5'):
    """
    generate(seed, width=420, pad=0.12, invert=False, hasher='md5')

    Args:
        seed (str): Seed used to generate the identicon.
        width (int, optional): The width of the image in pixels.
        pad (float, optional): Percentage border (of block) around the sprite.
        invert (bool, optional): Invert the colour of the identicon.
        hasher (str/func(str) -> str, optional): Hashing algorithm. 
            Acceptable values of `hasher` are 'md5', 'blake', 'sha' or a custom function which accepts a string and returns a compatible hash.

    Returns:
        image: PIL.Image

    ```
    # Example
    generate("seed").show()
    generate("agzg").save("agzg.png")
    ```
    """

    if pad <= 0.0 or pad > 0.4:
        raise ValueError("0.0 < pad < 0.4 only")

    if type(hasher) == str:
        hasher = hasher.lower().strip()

        if hasher == 'sha':
            hasher = _SHA
        elif hasher == 'blake':
            hasher = _BLAKE
        elif hasher == 'md5':
            hasher = _MD5
        else:
            raise ValueError("hasher = 'md5', 'blake' or 'sha'")
    else:
        # Ensure custom hashers are compatible with algorithm.
        # Otherwise, warn and switch to MD5.
        test = hasher("test")
        if type(test) != str or len(test) < 15 or not all(c in hexdigits for c in test):
            raise ValueError("Provided hasher is incompatible")
    
    seed = hasher(seed)[-15:]
 
    # Calculate image width, pixel size and padding.
    p = int(width * pad)
    b = (width - 2 * p) // 5
    w = b * 5 + 2 * p

    # Use the seed to create HSL.
    hue = int(seed[-6:], 16) / 0xffffff * 360
    sat = 65 + int(seed[-2], 16) / 0xff * 25
    lum = 45 + int(seed[0], 16) / 0xff * 40
    hsl = f"hsl({hue}, {sat}%, {lum}%)"

    image  = Image.new("RGB", (w, w), "#F0F0F0")
    colour = hsl
    
    if invert:
        image  = Image.new("RGB", (w, w), hsl)
        colour = "#F0F0F0"
     
    filled = []

    for i, v in enumerate(seed):
        yes = int(v, 16) <= 10
        filled.append(yes)

        if yes and i < 10:
            _square(image, i // 5, i % 5, b, p, colour)
            _square(image, 4 - i // 5, i % 5, b, p, colour)
        elif yes:
            _square(image, i // 5, i - 10, b, p, colour)

    # Ignore (arguably) boring sprites.
    if all(filled) or not any(filled) or sum(filled) < 3:
        return identicon(seed, width, pad, invert, hasher)
        
    return image

if __name__ == "__main__":
    VALID = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    try:
        import argparse
    except:
        exit("pip install argparse")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("seed", nargs="?", help="Seed used to generate the identicon.")
    parser.add_argument("-i", "--invert", help="Invert identicon colours.", action="store_true")
    parser.add_argument("-s", "--save", help="Confirm save identicon.", action="store_true")
    parser.add_argument("-v", "--view", help="View identicon.", action="store_true")
    
    args = parser.parse_args()

    if args.seed == None:
        args.seed = input("Enter seed: ").strip()

    image = identicon(args.seed, invert=args.invert)

    if args.view: image.show()
    
    if args.save or input("save (y/N): ").lower() in ("y", "yes"):
        name = "".join([c if c in VALID else '-' for c in args.seed]) + ".png"
        image.save(name)
        print(f"Saved as {name}")

