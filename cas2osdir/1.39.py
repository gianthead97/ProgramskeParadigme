import os



for (trenutni_dir, _, fajlovi) in os.walk("//"):
    if "index.html" in fajlovi:
        print (os.path.join(trenutni_dir, "index.html"))
    elif "index.php" in fajlovi:
        print (os.path.join(trenutni_dir, "index.php"))


        