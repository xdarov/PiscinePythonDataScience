from config import NUM_OF_STEPS, FILE_NAME, TEMP, REPORT_NAME, REPORT_FORMAT
from analytics import Research
import logging

def main():
    logging.basicConfig(filename='analytics.log', level=logging.DEBUG,
                format='%(asctime)s %(message)s')
    Research = Research(FILE_NAME)
    data = Research.file_reader()
    analyt = Research.Analytics(data)
    if data != None:
        # print(data)
        counts = analyt.counts()
        # print(*counts)
        fractions = analyt.fractions(*counts)
        # print(*fractions)
        predict_random = analyt.predict_random(NUM_OF_STEPS)
        # print(predict_random)
        # print(analyt.predict_last(Research))
        report = TEMP.format(sum(counts), counts[0], counts[1],
                          fractions[0], fractions[1], NUM_OF_STEPS,
                          predict_random.count([1, 0]),
                          predict_random.count([0, 1]))
        print(report)
        analyt.save_file(report, REPORT_NAME, REPORT_FORMAT)

if __name__ == '__main__':
    main()