# Task1

![WebServic](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task1\WebServic.png)

```
title Communication with Web Service Support

User -> Web Service System: Submit Support Request
Web Service System -> Knowledge Base System: Query Solution
Knowledge Base System -> Web Service System: Return Solution
alt Solution Found
    Web Service System -> User: Provide Solution
else Solution Not Found
    Web Service System -> Support Operator: Notify New Request
    Support Operator -> Web Service System: View Request
    Web Service System -> Support Operator: Provide Solution
    Support Operator -> User: Respond to Support Request
end






```

![ExchangeRegistration](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task1\ExchangeRegistration.png)

```
title International Remittance Registration

Remitter -> Remittance Bank: Submit 2-Hour Delayed Remittance Request
Remittance Bank -> International Remittance System: Process Request
International Remittance System -> Receiving Bank: Forward Request
alt Withdrawal within 2 Hours
    Remitter -> Remittance Bank: Withdraw Remittance Request
    Remittance Bank -> International Remittance System: Process Withdrawal
    International Remittance System -> Receiving Bank: Process Withdrawal
    Remittance Bank -> Remitter: Remittance Withdrawal Confirmation
else Confirmation after 2 Hours
    Receiving Bank -> International Remittance System: Confirm Receipt
    International Remittance System -> Remittance Bank: Confirm Remittance
    Remittance Bank -> Remitter: Remittance Confirmation
end

International Remittance System -> Exchange Rate System: Query Exchange Rate (CNY/USD)
Exchange Rate System -> International Remittance System: Return Exchange Rate
International Remittance System -> Remittance Bank: Settle Exchange Rate

```

# Task2

## flowchat

![flowchat](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task2\flowchat.png)

## EPC

![EPC](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task2\EPC.png)

## BPMN

![Bpmn](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task2\Bpmn.png)

# Task3

![1](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task3\1.png)

![2](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task3\2.png)

![3](C:\Users\ROG\Desktop\master_1\PythoneAndBP\bp4-foreign-Chen-Qichen\Task3\3.png)