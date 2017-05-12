def find_solutions(words):
  print(words)
  vowels = "aeiou"
  group = []
  solutions = []
  count_same = 0
  for word in words:
    for letter in range(len(word)):
      if word[letter] in vowels:
        for vowel in vowels:
          group.append(word.replace(word[letter], vowel))
        for variation in group:
          if variation in words:
            count_same += 1
        if count_same == 5 and group not in solutions:
          solutions.append(group)
        count_same = 0
        group = []
  print(solutions)
  return solutions
  
find_solutions(['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'en', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'un', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'in', 'blue', 'bluejays', 'an', 'blunder',
     'last', 'lest', 'list', 'lost', 'lust','beryl', 'jigsawed',
     'oospheres', 'on', 'troweller', 'volcanizes'])
