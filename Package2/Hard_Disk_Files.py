from File import File
# This class is used to create Hard Disk objects.
# Hard Disk attributes are: size, files (list of files)
# Methods: add_file, del_file, update_file, used_space, free_space




class HardDiskFiles:
   def __init__(self, size):
       """__init__ create an empty hard disk:
       Initializes the attribute: size.
       The attribute files is a list that will be empty when the HD is created."""
       if type(size) != int:
           raise TypeError("Disk size must be int.")
       if size < 0:
           size = 0
       self.size = size
       self.files = []


   def used_space(self):
       """Returns the sum of all the file sizes.
       Go through the list of files and sum the size of each file object"""
       sum_sizes = 0
       for file in self.files:
           sum_sizes += file.size
       return sum_sizes


   def free_space(self):
       """Returns the free space"""
       return self.size - self.used_space()


   def add_file(self, file):
       """Add file will add a file to the list if it doesn't exist and
       if there is enough space. Return a boolean value if it succeeded or not"""
       if type(file) != File:
           raise TypeError("Type is supposed to be File.")
       # Check if the file already exists
       if file in self.files:
           print(f"{file.name}.{file.suffix} already exists!")
           return False


       # Check if there is no space for the file
       if self.free_space() < file.size:
           print(f"No space for file: {file.name}.{file.suffix}")
           return False


       # All valid - add the file to the files list
       self.files.append(file)
       return True


   def del_file(self, file: File):
       """Delete a file from the list if the file exists.
       Return a boolean value if it succeeded or not."""
       if file in self.files:
           self.files.remove(file)
           return True


       print(f"{file.name}.{file.suffix} doesn't exist.")
       return False


   def update_file(self, file: File):
       """Update a file in the list:
       If the file exists and there is enough space - update to the new size, otherwise
       print a message. Return a boolean value if it succeeded or not."""
       # Check if the file doesn't exist in the dictionary
       if file not in self.files:
           print(f"file {file.name}.{file.suffix} doesn't exist.")
           return False


       # Find the file in the list
       file_index = self.files.index(file)


       # Check if there is not enough space for the new size
       if self.free_space() + self.files[file_index].size < file.size:
           print(f"No space for updating file: {file.name}.{file.suffix}")
           return False


       # All valid - update the file size
       self.files[file_index] = file
       return True


   def biggest_file(self):
       """Returns the file with the highest size"""
       return max(self.files)


   def __str__(self):
       return (f"HD: size {self.size} used space:{self.used_space()} free space:{self.free_space()}"
               f"\n{self.files}")




if __name__ == "__main__":
   hd1 = HardDiskFiles(200)
   file1 = File("file1","docx",30)
   file2 = File("file2","txt",60)
   file3 = File("file3","txt",20)




   file4 = File("file2","txt",10)




   hd1.add_file(file1)
   hd1.add_file(file2)
   hd1.add_file(file3)
   print(hd1)
   file1 = File("file1","docx",110)
   hd1.update_file(file1)
   print(hd1)


   print(hd1.biggest_file())


# hd1.add_file(file2)
# hd1.add_file(file4)
# print(hd1)
# hd1.del_file(file1)
# print(hd1)
