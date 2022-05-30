from plants.services.tables import PlantsExcelParser


def import_plants_from_table(filename: str = '/code/evraz/plants/services/zmk.xlsx'):
    """Парсинг ЗМК из xlsx файла"""
    parser = PlantsExcelParser(filename, start_row=6)
    return parser.get_plants_and_plants_objects()
