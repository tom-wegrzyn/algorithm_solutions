import os
import sys


class WordCount:
    def get_info(self, option: str = "", file: str = "") -> None | int | tuple[int, int, int, int]:
        """
        Takes in two strings, an option and a file, and returns information on the file based on the option specified.

        Parameters
        ----------
        option : str
            The option string for determining what information to return about the file.
        file : str
            The file string to locate the file.

        Returns
        ----------
        None | int | tuple[int, int, int, int]
            Returns none if exit is input by the user when prompted.
            Returns an int if an option parameter is specified.
            Returns a tuple of ints if a file is specified without any options.
        """
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
    def get_file_byte_size(file: str) -> int:
        """
        Takes in a string containing the file path and returns byte size of the file.

        Parameters
        ----------
        file : str
            A string denoting the file path.

        Returns
        ----------
        int
            Returns the byte size of the file.
        """
        stats = os.stat(file)
        return stats.st_size

    @staticmethod
    def get_file_line_count(file: str) -> int:
        """
        Takes in a string containing the file path and returns the line count of the file.

        Parameters
        ----------
        file : str
            A string denoting the file path.

        Returns
        ----------
        int
            Returns the line count of the file.
        """
        f = open(file, "r")
        # Original solution but after reading online this is inefficient for larger files
        # print(len(file.readlines()))
        for count, item in enumerate(f):
            pass
        f.close()
        return count + 1

    @staticmethod
    def get_word_count(file: str) -> int:
        """
        Takes in a string containing the file path and returns the word count of the file.

        Parameters
        ----------
        file : str
            A string denoting the file path.

        Returns
        ----------
        int
            Returns the word count of the file.
        """
        f = open(file, "r")
        data = f.read().split(" ")
        f.close()
        return len(data)

    @staticmethod
    def get_character_count(file: str) -> int:
        """
        Takes in a string containing the file path and returns the character count of the file.

        Parameters
        ----------
        file : str
            A string denoting the file path.

        Returns
        ----------
        int
            Returns the character count of the file.
        """
        # TODO Look into with statements so you can avoid closing file at the end.
        f = open(file, "r")
        data = f.read()
        f.close()
        return len(data)
