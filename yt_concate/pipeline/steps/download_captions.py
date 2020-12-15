import os

from pytube import YouTube

from .step import Step
from .step import StepException

import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('downloading caption for', yt)
            if utils.caption_file_exists(yt.url):
                print('found existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError) as e:
                print('Found an Error: ', e, 'while downloading the caption for')
                continue

            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt

            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print ('took', end - start, 'seconds')

        return data
