'''
python C:/wamp64/www/apps/lilpostloo/DailyProgrammer/Challenge375Hard.py

https://old.reddit.com/r/dailyprogrammer/comments/aqwvxo/20190215_challenge_375_hard_graph_of_thrones/

Rules:
(1) If all triangular relationships (3 nodes) are stable, then whole network is stable
(2) Balanced triangles have 1 or 3 positive links 
(3) Unbalanced triangles have 0 or 2 positive links 

Algorithm:
  Generate score table of relationships between all 2 nodes which have a relationship (Values: 1 = positive, 0 = negative).
  Generate all triangular relationships and score them using score table
    if score == 1 or 3 then it is balanced
    if score == 0 or 2 then it is unbalanced
  If all triangles are balanced then network is balanced, otherwise its not.


'''

def getUniqueNodes(lines):
  merged = []
  for line in lines[1:]:
    s = line.split(' ++ ')
    s = ' -- '.join(s).split(' -- ')
    merged += s
  return list(set(merged))
 

def generateRelationships(lines):
  relationships = {}
  for line in lines:
    if ' ++ ' in line:
      s = line.split(' ++ ')
      s.sort()
      relationships[','.join(s)] = 1
      #relationships.append([','.join(s),1])
    if ' -- ' in line:
      s = line.split(' -- ')
      s.sort()
      relationships[','.join(s)] = 0
      #relationships.append([','.join(s),0])

  return relationships

def checkStability(nodes,relationships):
  triNodes = sorted(list(set([','.join(sorted([x,y,z])) for x in nodes for y in nodes for z in nodes if (x!=y and y!=z and x!=z)])))
  #print(triNodes)
  #print('\n')

  triArr = [x.split(',') for x in triNodes]

  balanced = True
  for node in triArr:
    score1 = relationships[node[0]+','+node[1]]
    score2 = relationships[node[1]+','+node[2]]
    score3 = relationships[node[0]+','+node[2]]
    total = score1+score2+score3;
    print(total,node,score1,score2,score3)
    balanced = False if total==0 or total==2 else balanced

  return 'Balanced' if balanced else 'Unbalanced'

def run(input):
  lines = input.splitlines()
  N = lines[:1][0].split(' ')[0]
  M = lines[:1][0].split(' ')[1]
  relationships = generateRelationships(lines[1:])
  nodes = getUniqueNodes(lines[1:])
  nodes.sort()
  stability = checkStability(nodes,relationships)
  print(stability)


input = '''6 15
Superman ++ Green Lantern
Superman ++ Wonder Woman
Superman -- Sinestro
Superman -- Cheetah
Superman -- Lex Luthor
Green Lantern ++ Wonder Woman
Green Lantern -- Sinestro
Green Lantern -- Cheetah
Green Lantern -- Lex Luthor
Wonder Woman -- Sinestro
Wonder Woman -- Cheetah
Wonder Woman -- Lex Luthor
Sinestro ++ Cheetah
Sinestro ++ Lex Luthor
Cheetah ++ Lex Luthor'''
run(input)


input = '''120 16
Daenerys Targaryen ++ Jon Snow
Daenerys Targaryen ++ Tyrion Lannister
Daenerys Targaryen ++ Varys
Daenerys Targaryen ++ Jorah Mormont
Daenerys Targaryen ++ Beric Dondarrion
Daenerys Targaryen ++ Sandor “the Hound” Clegane
Daenerys Targaryen ++ Theon and Yara Greyjoy
Daenerys Targaryen -- Sansa Stark
Daenerys Targaryen -- Arya Stark
Daenerys Targaryen -- Bran Stark
Daenerys Targaryen -- The Lords of the North and the Vale
Daenerys Targaryen -- Littlefinger
Daenerys Targaryen -- Cersei Lannister
Daenerys Targaryen -- Jaime Lannister
Daenerys Targaryen -- Euron Greyjoy
Jon Snow ++ Tyrion Lannister
Jon Snow ++ Varys
Jon Snow ++ Jorah Mormont
Jon Snow ++ Beric Dondarrion
Jon Snow ++ Sandor “the Hound” Clegane
Jon Snow -- Theon and Yara Greyjoy
Jon Snow -- Sansa Stark
Jon Snow -- Arya Stark
Jon Snow -- Bran Stark
Jon Snow -- The Lords of the North and the Vale
Jon Snow -- Littlefinger
Jon Snow -- Cersei Lannister
Jon Snow -- Jaime Lannister
Jon Snow -- Euron Greyjoy
Tyrion Lannister ++ Varys
Tyrion Lannister ++ Jorah Mormont
Tyrion Lannister ++ Beric Dondarrion
Tyrion Lannister ++ Sandor “the Hound” Clegane
Tyrion Lannister ++ Theon and Yara Greyjoy
Tyrion Lannister -- Sansa Stark
Tyrion Lannister -- Arya Stark
Tyrion Lannister -- Bran Stark
Tyrion Lannister -- The Lords of the North and the Vale
Tyrion Lannister -- Littlefinger
Tyrion Lannister -- Cersei Lannister
Tyrion Lannister -- Jaime Lannister
Tyrion Lannister -- Euron Greyjoy
Varys ++ Jorah Mormont
Varys ++ Beric Dondarrion
Varys ++ Sandor “the Hound” Clegane
Varys ++ Theon and Yara Greyjoy
Varys -- Sansa Stark
Varys -- Arya Stark
Varys -- Bran Stark
Varys -- The Lords of the North and the Vale
Varys -- Littlefinger
Varys -- Cersei Lannister
Varys -- Jaime Lannister
Varys -- Euron Greyjoy
Jorah Mormont ++ Beric Dondarrion
Jorah Mormont ++ Sandor “the Hound” Clegane
Jorah Mormont ++ Theon and Yara Greyjoy
Jorah Mormont -- Sansa Stark
Jorah Mormont -- Arya Stark
Jorah Mormont -- Bran Stark
Jorah Mormont -- The Lords of the North and the Vale
Jorah Mormont -- Littlefinger
Jorah Mormont -- Cersei Lannister
Jorah Mormont -- Jaime Lannister
Jorah Mormont -- Euron Greyjoy
Beric Dondarrion ++ Sandor “the Hound” Clegane
Beric Dondarrion ++ Theon and Yara Greyjoy
Beric Dondarrion -- Sansa Stark
Beric Dondarrion -- Arya Stark
Beric Dondarrion -- Bran Stark
Beric Dondarrion -- The Lords of the North and the Vale
Beric Dondarrion -- Littlefinger
Beric Dondarrion -- Cersei Lannister
Beric Dondarrion -- Jaime Lannister
Beric Dondarrion -- Euron Greyjoy
Sandor “the Hound” Clegane ++ Theon and Yara Greyjoy
Sandor “the Hound” Clegane -- Sansa Stark
Sandor “the Hound” Clegane -- Arya Stark
Sandor “the Hound” Clegane -- Bran Stark
Sandor “the Hound” Clegane -- The Lords of the North and the Vale
Sandor “the Hound” Clegane -- Littlefinger
Sandor “the Hound” Clegane -- Cersei Lannister
Sandor “the Hound” Clegane -- Jaime Lannister
Sandor “the Hound” Clegane -- Euron Greyjoy
Theon and Yara Greyjoy -- Sansa Stark
Theon and Yara Greyjoy -- Arya Stark
Theon and Yara Greyjoy -- Bran Stark
Theon and Yara Greyjoy -- The Lords of the North and the Vale
Theon and Yara Greyjoy -- Littlefinger
Theon and Yara Greyjoy -- Cersei Lannister
Theon and Yara Greyjoy -- Jaime Lannister
Theon and Yara Greyjoy -- Euron Greyjoy
Sansa Stark ++ Arya Stark
Sansa Stark ++ Bran Stark
Sansa Stark ++ The Lords of the North and the Vale
Sansa Stark ++ Littlefinger
Sansa Stark -- Cersei Lannister
Sansa Stark -- Jaime Lannister
Sansa Stark -- Euron Greyjoy
Arya Stark ++ Bran Stark
Arya Stark ++ The Lords of the North and the Vale
Arya Stark ++ Littlefinger
Arya Stark -- Cersei Lannister
Arya Stark -- Jaime Lannister
Arya Stark -- Euron Greyjoy
Bran Stark ++ The Lords of the North and the Vale
Bran Stark -- Littlefinger
Bran Stark -- Cersei Lannister
Bran Stark -- Jaime Lannister
Bran Stark -- Euron Greyjoy
The Lords of the North and the Vale ++ Littlefinger
The Lords of the North and the Vale -- Cersei Lannister
The Lords of the North and the Vale -- Jaime Lannister
The Lords of the North and the Vale -- Euron Greyjoy
Littlefinger -- Cersei Lannister
Littlefinger -- Jaime Lannister
Littlefinger -- Euron Greyjoy
Cersei Lannister ++ Jaime Lannister
Cersei Lannister ++ Euron Greyjoy
Jaime Lannister ++ Euron Greyjoy'''
run(input)


'''
a network is balanced if all of its triangles are balanced

balanced triangles are:
  1 or 3 ++
unbalanced are:
  0 or 2 ++ 


if odd node
  odd pluses = balanced
  even pluses = unbalanced
if even node:



Superman ++ Green Lantern
Superman ++ Wonder Woman
Superman -- Sinestro
Superman -- Cheetah
Superman -- Lex Luthor

Green Lantern ++ Superman
Green Lantern ++ Wonder Woman
Green Lantern -- Sinestro
Green Lantern -- Cheetah
Green Lantern -- Lex Luthor

Wonder Woman ++ Superman
Wonder Woman ++ Green Lantern
Wonder Woman -- Sinestro
Wonder Woman -- Cheetah
Wonder Woman -- Lex Luthor


Sinestro ++ Cheetah
Sinestro ++ Lex Luthor
Sinestro -- Superman
Sinestro -- Wonder Woman
Sinestro -- Green Lantern


Cheetah ++ Lex Luthor
Cheetah ++ Sinestro
Cheetah -- Superman
Cheetah -- Wonder Woman
Cheetah -- Green Lantern


Lex Luther ++ Sinestro
Lex Luther ++ Cheetah
Lex Luther -- Superman
Lex Luther -- Wonder Woman
Lex Luther -- Green Lantern




Superman ++ Green Lantern ++ Wonder Woman ++ Superman
Superman ++ Green Lantern -- Sinestro -- Superman
Superman ++ Green Lantern -- Cheetah -- Superman
Superman ++ Green Lantern -- Lex Luthor -- Superman
Superman ++ Wonder Woman -- Sinestro -- Superman
Superman ++ Wonder Woman -- Cheetah -- Superman
Superman ++ Wonder Woman -- Lex Luthor -- Superman
Superman -- Sinestro ++ Cheetah -- Superman
Superman -- Sinestro ++ Lex Luthor -- Superman
Superman -- Cheetah ++ Lex Luthor -- Superman

'''