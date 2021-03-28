from pymediainfo_video_test import PyMediaInfoTest
from tiny_tag_video_test import TinyTagTest
from ffmpeg_video_test import FfmpegTest


def print_info():
    file = "file_example.mp4"
    PyMediaInfoTest.print_media_info(file)
    TinyTagTest.print_media_info(file)
    FfmpegTest.print_media_info(file)


print_info()
