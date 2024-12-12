class Hard_Disk:
   def __init__(self,size):
       self.size = size
       self.files = {}




   def __str__(self):
       """Prints the files, its size and the storage."""
       return f"Size: {self.size}, Files: {self.files}, files storage: {self.used_space()}"




   def used_space(self):
       """Returns the used space of all the files together"""
       return sum(self.files.values())




   def free_space(self):
       """Returns the remaining space"""
       return self.size - sum(self.files.values())




   def add_file(self,name,size):
       if name not in self.files:
           if self.used_space() + size <= self.size:
               self.files[name] = size
               return True
           else:
               print("No space in disk.")
               return False
       else:
           print("File already exists.")
           return False


   def del_file(self, name):
       if name in self.files:
           del self.files[name]
           return True
       else:
           print("File does not exist.")
           return False


   def update_file(self, name, size):
       if self.used_space() + size - self.files[name] <= self.size:
           if name in self.files:
               self.files[name] = size
               return True
           else:
               print("File does not exist.")
               return False
       else:
           print("File is too large, changes has been disregarded.")
           return False


print("-----Add A File-----")
myfiles = HardDisk(50)
stop = 1
while stop == 1:
   name1 = input("name: ")
   size1 = int(input("size: "))
   if myfiles.add_file(name1,size1):
       print(f"File {name1} has been added.")
   stop = int(input("Write 1 to continue: "))
print(myfiles)
print("----- Delete A File -----")
name2 = input("File to delete: ")
if myfiles.del_file(name2):
   print(f"Flie {name2} has been deleted.")
print(myfiles)
print("----- Update A File -----")
name3 = input("File name to update: ")
size3 = int(input("New file size: "))
if myfiles.update_file(name3,size3):
   print(f"File {name3} has been updated to size {size3}")
print(myfiles)
