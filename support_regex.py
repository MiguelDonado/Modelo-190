import re


def to_number(number):
    if number:
        return float(number.replace(".", "").replace(",", ".").replace("\n", ""))
    else:
        return 0.00


def check_match_number(input, string):
    try:
        result = input.search(string).group(1)
        if result:
            return to_number(result)
        else:
            return 0.00
    except AttributeError:
        return 0.00


def check_match(input, string, i):
    try:
        result = input.search(string).group(i)
        if result:
            return result
        else:
            return ""
    except AttributeError:
        return ""


# ----------------------------------------REGULAR EXPRESSIONS----------------------------------------
individuo_pattern = re.compile(
    r"^NIF\sdel\sperceptor.*?Ascendientes", flags=re.DOTALL | re.MULTILINE
)
dni_nombre_provincia_pattern = re.compile(
    r"Provincia\n(\w+)\s(.*)\s(\d\d)$", flags=re.MULTILINE
)
clave_pattern = re.compile(r"^Clave:\s([A-Z])", flags=re.MULTILINE)

text_holding_base_and_retenciones_pattern = re.compile(
    r"Subclave.*ingresados en el Estado", flags=re.DOTALL
)
base_and_retenciones_pattern = re.compile(
    r"\s([0-9\.]+,\d\d)\s([0-9\.]+,\d\d)?", flags=re.MULTILINE
)

gastos_deducibles_pattern = re.compile(
    r"^Reducciones\s.*(\n[0-9\.]+,\d\d).*\nHijos", flags=re.MULTILINE
)
# ---------------------------------------------------------------------------------------------------
