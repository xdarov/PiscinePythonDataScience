from config import NUM_OF_STEPS, FILE_NAME, TEMP, REPORT_NAME, REPORT_FORMAT
from analytics import Research

def main():
    research = Research(FILE_NAME)
    data = research.file_reader()
    analyt = research.Analytics(data)
    if data != None:
        counts = analyt.counts()
        fractions = analyt.fractions(*counts)
        predict_random = analyt.predict_random(NUM_OF_STEPS)
        report = TEMP.format(sum(counts), counts[0], counts[1],
                          fractions[0], fractions[1], NUM_OF_STEPS,
                          predict_random.count([1, 0]),
                          predict_random.count([0, 1]))
        print(report)
        analyt.save_file(report, REPORT_NAME, REPORT_FORMAT)

if __name__ == '__main__':
    main()