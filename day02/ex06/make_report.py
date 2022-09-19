from config import NUM_OF_STEPS, FILE_NAME, TEMP, REPORT_NAME, REPORT_FORMAT, MESSAGE_SUCCESS, MESSAGE_FAILURE, WEBHOOK
from analytics import Research
import logging

def main():
    try:
        logging.basicConfig(filename='analytics.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s')
        research = Research(FILE_NAME)
        data = research.file_reader()
        analyt = research.Analytics(data)
        if data != None:
            # print(data)
            counts = analyt.counts()
            # print(*counts)
            fractions = analyt.fractions(*counts)
            # print(*fractions)
            predict_random = analyt.predict_random(NUM_OF_STEPS)
            # print(predict_random)
            # print(analyt.predict_last(research))
            report = TEMP.format(sum(counts), counts[0], counts[1],
                            fractions[0], fractions[1], NUM_OF_STEPS,
                            predict_random.count([1, 0]),
                            predict_random.count([0, 1]))
            print(report)
            analyt.save_file(report, REPORT_NAME, REPORT_FORMAT)
            research.send_slack_message(MESSAGE_SUCCESS, WEBHOOK)
    except (ValueError, OSError):
            research.send_slack_message(MESSAGE_FAILURE, WEBHOOK)
            pass


if __name__ == '__main__':
    main()