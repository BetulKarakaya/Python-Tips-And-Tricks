class Employee:
   def work(self):
      print ("Working :)")
      return

class SoftwareDeveloper(Employee):
   def work(self):
      print ("Working on a coding project.")
      return

class Accountant(Employee):
   def work(self):
      print ("Working on budgeting.")
      return

def main():
   jobs = [SoftwareDeveloper(), Accountant()]
   for job in jobs:
      job.work()

if __name__ == "__main__":
   main()