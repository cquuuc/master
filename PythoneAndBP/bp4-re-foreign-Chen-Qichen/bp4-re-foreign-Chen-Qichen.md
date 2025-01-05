# Task1

### Communication with Web Service Support

```
title 与网络服务支持的沟通 Communication with Web Service Support

loop 直到获得满意的答案 Until a Satisfactory Answer is Obtained
    用户User -> 网络服务系统WebServer: 发送请求 Submit Request
    网络服务系统WebServer -> 知识库系统knowledgeSys: 查询解决方案 Query Solution
    alt 请求可以解决 Solution Found
        知识库系统knowledgeSys -> 网络服务系统WebServer: 返回答案 Return Answer
        网络服务系统WebServer -> 用户User: 返回答案 Provide Answer
    else 请求不能解决 Solution Not Found
        网络服务系统WebServer -> 支持操作员operator: 转发请求 Forward Request
        支持操作员operator -> 网络服务系统WebServer: 返回处理结果 Return Result
        网络服务系统WebServer -> 用户User: 返回处理结果 Provide Result
    end
end
```

![image-20241226000241790](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241226000241790.png)

### International Remittance Registration

```
title 国际汇款登记 International Remittance Registration

loop 直到请求有效 Until the Request is Valid
    汇款人sender -> 汇款银行sending bank: 提交汇款请求 Submit Remittance Request
    汇款银行sending bank -> 汇款银行sending bank: 检查请求有效性 Check Request Validity
    alt 请求有效 Request Valid
        汇款银行sending bank -> 国际汇款系统RemittanceSys: 发送汇款请求 Send Remittance Request
        国际汇款系统RemittanceSys -> 收款银行receiving bank: 转发请求 Forward Request
        alt 2小时内提款 Withdrawal within 2 Hours
            汇款人sender -> 汇款银行sending bank: 撤回汇款请求 Withdraw Remittance Request
            汇款银行sending bank -> 国际汇款系统RemittanceSys: 处理撤回 Process Withdrawal
            国际汇款系统RemittanceSys -> 收款银行receiving bank: 处理撤回 Process Withdrawal
            汇款银行sending bank -> 汇款人sender: 汇款撤回确认 Remittance Withdrawal Confirmation
        else 2小时后确认 Confirmation after 2 Hours
            收款银行receiving bank -> 国际汇款系统RemittanceSys: 确认收款 Confirm Receipt
            国际汇款系统RemittanceSys -> 汇款银行sending bank: 确认汇款 Confirm Remittance
            汇款银行sending bank -> 汇款人sender: 汇款确认 Remittance Confirmation
        end
    else 请求无效 Request Invalid
        汇款银行sending bank -> 汇款人sender: 返回错误信息 Return Error Message
    end
end

国际汇款系统RemittanceSys -> 欧洲交易所CME European Exchange: 查询汇率 (CNY/USD) Query Exchange Rate (CNY/USD)
欧洲交易所CME European Exchange -> 国际汇款系统RemittanceSys: 返回汇率 Return Exchange Rate
国际汇款系统RemittanceSys -> 汇款银行sending bank: 结算汇率 Settle Exchange Rate

```

![image-20241226001018283](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241226001018283.png)

# Task2

![image-20250105233936386](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250105233936386.png)

![image-20250105233924564](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250105233924564.png)

![image-20241227014051153](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241227014051153.png)



![image-20241227014059740](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241227014059740.png)



![image-20241227014120161](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241227014120161.png)

# Task3

- Process 1 (Obtaining a Loan)： 

![image-20241231031816524](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241231031816524.png)

![image-20241231031841437](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241231031841437.png)

![image-20241231031856731](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20241231031856731.png)

- Process 2 (Company employee expense reimbursement)： 

![image-20250103184549993](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250103184549993.png)

![image-20250103184606320](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250103184606320.png)

- Process 3 (Handling Customer Complaints)：

![image-20250105172435875](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250105172435875.png)

![image-20250105172500986](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250105172500986.png)

![image-20250105172523178](C:\Users\ROG\AppData\Roaming\Typora\typora-user-images\image-20250105172523178.png)
