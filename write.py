class Write:

    file_name = ""
    with open("file_name.txt", "r") as f:
        file_name = f.read()

    @staticmethod
    def header():
        with open("header.asm", "r") as in_file:
            with open(f"{Write.file_name}.asm", "w") as out_file:
                out_file.write(in_file.read())

    @staticmethod
    def write(code):
        with open(f"{Write.file_name}.asm", "a") as out_file:
            out_file.write(f"   {code}")

    @staticmethod
    def footer():
        with open("footer.asm", "r") as in_file:
            with open(f"{Write.file_name}.asm", "a") as out_file:
                out_file.write(in_file.read())
