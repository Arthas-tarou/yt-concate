from .step import Step
from yt_concate.model.yt import YT

class InitalizeYT(Step):
    def process(self, data, inputs, utils):

        """
        for url in data:
            YT(url)
        """

        return [YT(url for url in data)]