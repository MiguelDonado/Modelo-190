from openpyxl import Workbook


def write_to_xlsx(employees):

    wb = Workbook()
    ws = wb.active

    fieldnames = (
        "DNI",
        "Nombre y apellidos",
        "Codigo provincia",
        "Clave",
        "Percepcion Total",
        "Retencion Total",
        "Gastos deducibles",
    )
    ws.append(fieldnames)

    for employee in employees:
        ws.append(employee)

    wb.save("Modelo 190.xlsx")
