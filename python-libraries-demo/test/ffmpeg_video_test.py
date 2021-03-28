import json

import ffmpeg


class FfmpegTest:

    @staticmethod
    def print_media_info(file):
        info = ffmpeg.probe(file)
        print("\nFfmpeg")
        print(json.dumps(info, indent=4))
