class PrePro:
    @staticmethod
    def filter(file_name):

        try:
            with open(file=file_name, mode="r") as f:
                source = f.readlines()[0]
            idx = source.find("--")
            if idx == -1:
                return source
            return source[:idx]

        except Exception as error:
            raise TypeError(error)
