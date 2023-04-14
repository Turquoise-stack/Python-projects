import pandas as pd
import re
from constants import dictionaries

class DataParser:
    def __init__(self, path_of_data):
        # self.items = None
        self.path_of_data = path_of_data
        self.title = ''
        self.territory = ''
        self.assets = ''
        self.tmp_assets = ''
        self.status = ''
        self.audio = ''
        self.subtitle = ''

    def parse_data(self):
        data = pd.read_excel(self.path_of_data, sheet_name='Giant TVOD Orders', usecols=[1, 3, 4, 6])
        my_list = data.values.tolist()

        parsed_data = []

        for group in my_list:
            if str(group[3]) != 'Available':
                continue

            if str(group[2]) == 'Metadata Only':
                continue

            parsed_row = {}
#
            for i in range(len(group)):
                if i == 0:
                    # Title will be capitalized and cleaned from special characters and numbers.
                    parsed_row['title'] = str(group[i]).upper()
                    parsed_row['title'] = re.sub(r'[^\w\s,]|[\d]', '', parsed_row['title'])

                    if parsed_row['title'].startswith('The,'):
                        parsed_row['title'] = parsed_row['title'][4:]
                elif i == 1:
                    parsed_row['territory'] = dictionaries.territory_codes.get(str(group[i]), 'N/A')
                elif i == 2:
                    parsed_row['assets'] = str(group[i])
                    tmp_assets = parsed_row['assets']

                    for key, value in dictionaries.language_assets.items():
                        tmp_assets = tmp_assets.replace(key, value)

                        words = tmp_assets.split()

                        if 'and' in words:
                            parsed_row['audio'] = ''.join(words[0])
                            parsed_row['subtitle'] = ''.join(words[0])
                        else:
                            parsed_row['audio'], parsed_row['subtitle'] = words[0], words[1]

                elif i == 3:
                    parsed_row['status'] = str(group[i])

            parsed_data.append(parsed_row)

        return parsed_data



