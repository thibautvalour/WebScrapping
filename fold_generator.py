import os


#Permet de générer un fichier s'il n'existe pas
def _folder_generator(dir: str):
    x = dir.split("/")
    cur: str
    for index, cur in enumerate(x):
        z = ""
        type(type(index))
        for i in range(len(x[:index]) + 1):
            z += x[i] + "/"
        if not os.path.exists(z):
            # crée le fichier
            print("crée " + z)
            os.mkdir(z)

# gen_dir("cours/ce1/anglais")