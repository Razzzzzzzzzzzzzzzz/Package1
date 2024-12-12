class File:
   # Attributes: name, suffix, size
   def __init__(self, name, suffix, size):
       if type(name) != str:
           raise TypeError("Name must be of type str.")
       if type(suffix) != str:
           raise TypeError("Suffix must be of type str.")
       if len(suffix) < 2 or len(suffix) > 5:
           raise ValueError("Suffix length can only be 2-5 characters.")
       if type(size) != int:
           raise TypeError("Size must be of type int.")
       if size < 0:
           size = 0
       self.name = name
       self.suffix = suffix
       self.size = size


   def __str__(self):
       return f"{self.name}.{self.suffix}, size: {self.size}"


   def __repr__(self):
       return f"{self.name}.{self.suffix}"


   # ==   __eq__
   # >    __gt__
   # <    __lt__
   # >=   __ge__
   # <=   __le__
   # !=   __ne__
   def __eq__(self,other):
       return self.name == other.name and self.suffix == other.suffix


   def __gt__(self,other):
       if type(other) != File:
           raise TypeError
       return self.size > other.size


if __name__ == "__main__":
   file1 = File("file1","docx",30)
   file2 = File("file2","txt",60)
   file3 = File("file3","txt",100)
   file4 = File("file1", "docx", 30)


   print(file1)
   print(file2)
   print(file3)


   list_files = [file2, file1, file3]


   print(max(list_files))
   print(min(list_files))


   print(file2 > file3)
   #print(file2.__gt__(file3))


   # print(file1 in list_files)
   # print(file4 in list_files)
   # print(file1==file4)
   # list_files.remove(file4)
   # print(list_files)
   # print(file1 != file2)
   # print(file1 > file2)






   # print(list_files)
   # for i in list_files:
   #     print(i.size)
