text = "X-DSPAM-Confidence:    0.8475";
n = text.find('.')

d = text[n-1:]
print(float(d))
