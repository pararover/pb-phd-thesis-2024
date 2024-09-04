ls01 = LombScargle(t01, rate01, rateError01)
frequency01, power01 = ls01.autopower()

ls02 = LombScargle(t02, rate02, rateError02)
frequency02, power02 = ls02.autopower()

print(ls01.false_alarm_probability(max(power01)))
print(ls02.false_alarm_probability(max(power01)))