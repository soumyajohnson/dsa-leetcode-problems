class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log=[],[]
        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key=lambda x: (x.split(" ")[1:],x.split()[0]))
        return letter_log+digit_log