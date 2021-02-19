#Take a sample of ten phishing e-mails (or any text file) and find most commonly occurring word(s)

PhishingEMails = [
"claimyourprize@mymoney.com",
"luckywinner@freemoney.com",
"claimtheprize@mymoney.com",
"youarelucky@freemoney.com",
"youarewinner@prizeforyou.com",
"spinthewheel@freemoney.com",
"claimprize@mymoney.com",
"luckyjackpot@lottery.com",
"claimmoney@mymoney.com",
"luckyprize@mymoney.com",
"takeyourprize@lottery.com"
]

d = {}

for x in PhishingEMails:
    a = x.split("@")
    for z in a:
        if z not in d:
            d[z] = 1
        else:
            d[z]+=1

max_Occuring = max(d,key=d.get)
print("Most Commonly Occuring Word is:", max_Occuring)

print("Thanks for Using the Program!")