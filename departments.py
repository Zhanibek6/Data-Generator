import random
import writer
import general


def generate_output():
    names = ["Sales", "Maintenance", "Support", "Anti-Cancellation"]
    name = random.choice(names)
    numeric_id = general.generate_id()
    departments = [numeric_id, name]
    writer.export_data(departments, "output/departments.csv")
