# Use this method to send a > message.
message = input("> ")
# Splits a string into words.
words = message.split( " ")
emojis = {
   "smiling" : "😀",
   "sad" : "😞",
   "lol" : "😂",
   "sick":"😨",
   "happy": "😀",
   "cry": "😢",
   "confused" : "😕",
   "cold" : "🥶",
   "dissapointed" : "😞",
   "disguised" : "🥸",
   "expressionless" : "😑",
   "flyinng kiss" : "😘",
   "exhaling" : "😮‍💨",
   "screaming" : "😱",
   "vomating" : "🤮"
# Print emojis for each word.
}
outcome = " "
for word in words:
   outcome += emojis.get(word, word) + " "
print(outcome)
