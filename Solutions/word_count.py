import os
import sys

class WordCount:
    def get_info(self, option="", file=""):
        if file == "":
            for line in sys.stdin:
                file_name = line.rstrip()
                if file_name.lower() != "" and os.path.isfile(file_name):
                    file = file_name
                    break
                elif file_name.lower() == "exit":
                    return

        match option:
            case "-c":
                size = self.get_file_byte_size(file)
                # print(size)
                return size
            case "-l":
                lineCount = self.get_file_line_count(file)
                # print(lineCount)
                return lineCount
            case "-w":
                wordCount = self.get_word_count(file)
                # print(wordCount)
                return wordCount
            case "-m":
                characterCount = self.get_character_count(file)
                # print(characterCount)
                return characterCount
            case _:
                size = self.get_file_byte_size(file)
                lineCount = self.get_file_line_count(file)
                wordCount = self.get_word_count(file)
                characterCount = self.get_character_count(file)
                # print(
                #     size, lineCount, wordCount, characterCount
                # )
                return size, lineCount, wordCount, characterCount

    @staticmethod
    def get_file_byte_size(file):
        stats = os.stat(file)
        return stats.st_size

    @staticmethod
    def get_file_line_count(file):
        f = open(file, "r")
        # Original solution but after reading online this is inefficient for larger files
        # print(len(file.readlines()))
        for count, item in enumerate(f):
            pass
        f.close()
        return count + 1

    @staticmethod
    def get_word_count(file):
        f = open(file, "r")
        data = f.read().split(" ")
        f.close()
        return len(data)

    @staticmethod
    def get_character_count(file):
        # Look into with statements so you can avoid closing file at the end.
        f = open(file, "r")
        data = f.read()
        f.close()
        return len(data)


# Useful links:
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/ref_file_read.asp
# https://www.geeksforgeeks.org/enumerate-in-python/
# https://www.geeksforgeeks.org/python-os-stat-method/
