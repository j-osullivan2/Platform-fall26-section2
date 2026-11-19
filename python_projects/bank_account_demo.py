from git_projects.my_repo.python_projects.bank_account import BankAccount

account=BankAccount("1234", 100) # do not need to give objects types
print(account)
account.deposit(35)
print(account)
account.withdraw(70)
print(account)
balance=account.get_balance()
print(balance) 
# lebronto