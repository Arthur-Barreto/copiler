import re


class PrePro:
    @staticmethod
    def filter(file_name):

        try:
            with open(file=file_name, mode="r") as f:
                source = f.readlines()[0]

            cleaned_source = re.sub(r"--.*|\n$", "", source)

            with open("output.txt", "w") as f:
                f.write(cleaned_source)

            return cleaned_source

        except Exception as error:
            raise TypeError(error)
