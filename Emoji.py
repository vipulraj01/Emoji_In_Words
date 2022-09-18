message = input("> ")
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
}
outcome = " "
for word in words:
   outcome += emojis.get(word, word) + " "
print(outcome)