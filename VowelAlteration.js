function findSolutions(words) {
    //console.log(words);
    var vowels = "aeiou";
    var group = [];           //for five possible candidates at a time
    var solutions = [];       //It will contain the solutions
    var countSame = 0;        //Using for check the if @group contains 5 candidates
    for (var i=0; i<words.length; i++) {
      for(var j=0; j<words[i].length; j++) {
        if (vowels.includes(words[i][j])) {
          for(var k=0; k<vowels.length; k++) {
            group.push(words[i].replace(words[i][j], vowels[k]));
          }
          for (var l=0; l<group.length; l++) {
            console.log(words.includes(group[l]), group[l]);
            if (words.includes(group[l])) {
              countSame++;
              console.log("countSame:", countSame);
            }
          }
          console.log(countSame, !solutions.includes(group), "group:", group, "solutions:", solutions);
          if (countSame === 5 && solutions.every(x => !x.includes(group[0]))) {
            solutions.push(group);
          }
          countSame = 0;
          group = [];
        }
      }
    }
  return solutions;
}
  findSolutions(['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'en', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'un', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'in', 'blue', 'bluejays', 'an', 'blunder',
     'last', 'lest', 'list', 'lost', 'lust','beryl', 'jigsawed',
     'oospheres', 'on', 'troweller', 'volcanizes', 'fag', 'feg', 'fig', 'fog', 'fug', 'tag', 'teg', 'tig', 'tog', 'tug']);
