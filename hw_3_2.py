## start
test_score: int = int (input("Enter your test score: "));
if test_score < 0 or test_score > 100:
    print ("grade illegal");
elif test_score <= 40:
    print ("try harder next time...");
elif test_score <= 60:
    print ("you're getting there, need some more work");
elif test_score <= 80:
    print ("good pretty")
elif test_score <= 95:
    print ("awesome!")
else:
    print ("excellent!!! You're a Star!");
## end