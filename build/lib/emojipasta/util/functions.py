class Functions():

    def is_image(url):
        extensions = ['jpg', 'png', 'jpeg']
        length = len(url)
        index = 1
        for x in range(2, length):
            if url[-x] == ".":
                break
            else:
                index+=1
        ext = url[-index:].lower()
        if ext not in extensions:
            return False
        else:
            return True
