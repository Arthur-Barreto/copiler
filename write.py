class Write:

    code = ""

    @staticmethod
    def header(file_name: str):
        file_name = file_name.split(".")[0] + ".asm"
        with open("header.asm", "r") as in_file:
            with open(file_name, "w") as out_file:
                out_file.write(in_file.read())

    @staticmethod
    def body(file_name: str):
        file_name = file_name.split(".")[0] + ".asm"
        with open(file_name, "a") as out_file:
            out_file.write(Write.code)

    @staticmethod
    def footer(file_name: str):
        file_name = file_name.split(".")[0] + ".asm"
        with open("footer.asm", "r") as in_file:
            with open(file_name, "a") as out_file:
                out_file.write(in_file.read())
