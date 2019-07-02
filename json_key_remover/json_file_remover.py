class JSON_KEY_REMOVER:
    def __init__(self):
        self.data = []

    def import_json(self, filename):
        import json

        with open(filename) as json_file:
            self.data = json.load(json_file)

        print('import json done')

    def del_daily_zero_coordinates(self):
        import json

        for k in range(len(self.data)):
            for i in range(len(self.data[k]["history"]["dateInformation"][2]["daily"])):
                for j in range(0, 24):
                    if [0, 0] == self.data[k]["history"]["dateInformation"][2]["daily"][i]["dailyTimeline"]['dateT'+str(j)]["coordinates"]:
                        del self.data[k]["history"]["dateInformation"][2]["daily"][i]["dailyTimeline"]['dateT'+str(j)]["coordinates"]

        with open('data.json', 'w', encoding='UTF-8-sig') as data_file:
            self.data = json.dump(self.data, data_file, ensure_ascii=False)

        print("Done!")