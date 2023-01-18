# contents = ["The man was looking for something.",
#             "A quick brown fox jumps over the lazy dogs.",
#             "Padma is a rever.",
#             "Hardinz is a bridge."]
#
# filenames = ["needs.txt",
#              "longstring.txt",
#              "river.txt",
#              "bridge.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"Test/{filename}", "w")
#     file.write(content)


filenames = ["1.doc", "2.report", "3.presentation"]

filenames = [filename.replace(".", "-") + ".pdf" for filename in filenames]
print(filenames)