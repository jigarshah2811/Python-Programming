
"""
using namespace std;

/*
Input: char_limit = 20, message = "Hey Steven, your Uber is arriving now!"
Output: ["Hey Steven, (1/3)", "your Uber is (2/3)", "arriving now! (3/3)"]

Input: char_limit = 20, message = "Hey StevenShah, your Uber is arriving now!"
Output: ["Hey (1/3)", "StevenShah, (2/3)", "your Uber is arriving now! (3/3)"]


 (/) 4 Chars & 6 nums for 1000*20 len of message

Requirements:
1) Do not split a word across messages -- unless the word will not
fit in a single message, then you can split it across two messages or truncate the word.
2) Metadata (ie. ` (1/3)`) counts against the character limit. For example "Hey Steven, (1/3)" contains 17 characters.
*/



"""

"""
correct_output = ["Hey Steven, (9/10)", "your Uber is (2/3)", "arriving now! (3/3)"]

"Your car is a yellow toyota carolla and your driver is Steven Smith. We hope you have a very safe and pleasant journey. Please make sure to tell your friends all about Uber! We look forward to you riding with us again soon."





"Your car ... (1/xx)"
"Your car ... (2/xx)"
.
.
.
"Your car ... (10/xx)"


output: List(List(Char))
Input: FinalFun
Ouput: List(String)

"""
def SMSSplit(message, limit):
    current = 0
    countSms = 0
    currentRange = 1
    mul = 10
    inc = 2

    result = ""

    """
    # Remainting count TotalSMS

    for i in xrange(len(message)):

        temp = message[current::remChar]

        if temp.nextChar != " ":
            while (temp != " ")
                temp = tem p --

        countSms += 1

    totalSms += countSms


    # totalSms

    """


    while current < len(message):
        # Fix number of metadata chars to be reserved
        remChar = limit - inc
        temp = message[current::remChar]
        current += remChar

        sms = temp + metaString
        result.append(sms)

    yield result



message = "Hey Steven, your Uber is arriving now!"
expected_output = ["Hey Steven, (1)", "your Uber is (2)", "arriving now! (3)"]

result = []
countSms = 1
for sms in SMSSplit(message, 20):
    metaData = '(' + countSms + ')'
    result.append(sms + metaData)
    countSms += 1