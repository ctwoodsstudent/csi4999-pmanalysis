from Bio import phenotype
import gzip, tarfile

class Parser:

    def __init__(self):

    def readGzip(self, path):
        with gzip.open(path, 'rb') as f:
            file_content = f.read()
        return file_content

    def compressGzip(self, file_content):
        s_out = gzip.compress(file_content)
        return s_out
        
    def openTar(self, path):
        tar = tarfile.open(path)
        tar.extractall()
        tar.close()

    def readTar(self, path):
        tar = tarfile.open(path, "r:gz")
        lst = []
        for tarinfo in tar:
            lst.append( (tarinfo.name, tarinfo.size, tarinfo.isreg(), tarinfo.isdir) )
        tar.close()
        return lst
