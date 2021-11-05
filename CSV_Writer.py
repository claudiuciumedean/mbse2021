import csv  

class CSV_Writer:
  def __init__(self, simulation_id):
    self.filename = f"simulation_{simulation_id}.csv"
    self.headers = ['HealtyPersons', 'InfectedPersons', 'RecoveredPersons', 'Time']
    self.write_header()

  def write_header(self):
    with open(self.filename, 'w') as csvfile: 
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(self.headers) 
      csvfile.close()
  
  def write_row(self, row):
    with open(self.filename, 'a') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(row)
      csvfile.close()