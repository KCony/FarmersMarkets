

import model

testcases_input = []
testcases_result = []

count = 0
passed = 0
failed = 0

for test in testcases_input:
    res = model.find(test)
    if res == testcases_result[count]:
        passed +=1 # счетчик выполненных тестов
    else:
        failed +=1  # счетчик проваленных тестов
    count += 1  #общий счетчик тестов
