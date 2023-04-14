import warnings

from DataParser import DataParser

warnings.simplefilter("ignore")
path_of_data = r'FILE PATH TO EXCEL FILE'
parser = DataParser(path_of_data)


class main():
    parsed_data = parser.parse_data()
    print(f"Length of parsed data: {len(parsed_data)}")


if __name__ == '__main__':
    main()
