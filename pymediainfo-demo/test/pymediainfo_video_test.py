from pymediainfo import MediaInfo
import json


class PyMediaInfoTest:

    @staticmethod
    def print_media_info(file):
        media_info = MediaInfo.parse(file)
        print("\nPyMediaInfo")
        for i in media_info.tracks:
            print(json.dumps(i.to_data(), indent=4))
