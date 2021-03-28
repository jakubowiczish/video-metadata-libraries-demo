from tinytag import TinyTag


class TinyTagTest:

    @staticmethod
    def print_media_info(file):
        info = TinyTag.get(file)
        print("\nTinyTag")
        print(info)
