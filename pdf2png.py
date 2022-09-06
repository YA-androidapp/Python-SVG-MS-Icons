#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# python -m pip install pdf2image
# https://github.com/oschwartz10612/poppler-windows/releases/download/v22.04.0-0/Release-22.04.0-0.zip


from pathlib import Path
from pdf2image import convert_from_path
import glob
import os
import sys


dirs = [
    '2022-officecontent-symbols-june2022/AI_Symbols/Symbols_AI'
]

poppler_path = 'C:/poppler-22.04.0/Library/bin'


def main():
    for d in dirs:
        for file in glob.glob(os.path.join(d, os.path.join('**', '*.pdf')), recursive=True):
            name = file.split('.pdf')[0]
            print(name)
            url = name + '.pdf'

            input_pdf_path = Path(url)
            out_format = 'png'

            images = convert_from_path(pdf_path = input_pdf_path, dpi = 300, fmt = out_format,poppler_path = poppler_path)

            for i, image in enumerate(images):
                out_image_path = Path("{}_{}.{}".format(input_pdf_path.stem, i + 1, out_format))
                image.save(out_image_path, out_format)

if __name__ == "__main__":
    main()