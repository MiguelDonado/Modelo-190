from intro_func import get_pdf_file, read_pdf
from support_regex import (
    individuo_pattern,
    dni_nombre_provincia_pattern,
    clave_pattern,
    text_holding_base_and_retenciones_pattern,
    base_and_retenciones_pattern,
    gastos_deducibles_pattern,
    to_number,
    check_match_number,
    check_match,
)
from output import write_to_xlsx


def main():
    file = get_pdf_file()
    text_file = read_pdf(file)
    rows = []
    for page in text_file:
        individuos_page = individuo_pattern.findall(page)
        for individuo in individuos_page:
            dni = check_match(dni_nombre_provincia_pattern, individuo, 1)
            if dni:
                text_holding_base_and_retenciones = (
                    text_holding_base_and_retenciones_pattern.search(individuo).group(1)
                )
                try:
                    bases_and_retenciones = base_and_retenciones_pattern.findall(
                        text_holding_base_and_retenciones
                    )
                except AttributeError:
                    bases_and_retenciones = [(0.00, 0.00)]
                bases = sum([to_number(tpl[0]) for tpl in bases_and_retenciones])
                retenciones = sum([to_number(tpl[1]) for tpl in bases_and_retenciones])
                row = [
                    dni,
                    check_match(dni_nombre_provincia_pattern, individuo, 2),
                    check_match(dni_nombre_provincia_pattern, individuo, 3),
                    check_match(clave_pattern, individuo, 1),
                    bases,
                    retenciones,
                    check_match_number(gastos_deducibles_pattern, individuo),
                ]
            else:
                row = [""] * 7
            rows.append(row)
    write_to_xlsx(rows)


main()
