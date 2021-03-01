import os
for root, dirs, files in os.walk("\\\msk02daascl02\\Profile"):
    for file in files:
        if file.endswith(".pst"):
             print(os.path.join(root, file))