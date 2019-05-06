class StatisticsCalculator:

    def process(self, line: str) -> str:
        data = line.split(':')
        #print(data)
        return (data[3]+':'+data[0]+':CHI')
        pass

    print(process('','C0FFEE1C:CHI:NYC:714'))