import en_core_web_sm

def check_verb(token):
    """Check verb type given spacy token"""
    if token.pos_ == 'VERB':
        indirect_object = False
        direct_object = False
        for item in token.children:
            if(item.dep_ == "iobj" or item.dep_ == "pobj"):
                indirect_object = True
            if (item.dep_ == "dobj" or item.dep_ == "dative"):
                direct_object = True
        if indirect_object and direct_object:
            return 'VERB_DITRANVERB'
        elif direct_object and not indirect_object:
            return 'VERB_TRANVERB'
        elif not direct_object and not indirect_object:
            return 'VERB_INTRANVERB'
        else:
            return 'VERB'
    else:
        return token.pos_

#spacy.cli.download("en_core_web_sm")
nlp = en_core_web_sm.load()
docs = ["A little boy named Andy loves to be in his room, playing with his toys, especially his doll named Woody. but, what do the toys do when Andy is not with them, they come to life. Woody believes that he has life (as a toy) good. however, he must worry about Andy's family moving, and what Woody does not know is about Andys birthday party. Woody does not realize that Andy's mother gave him an action figure known as Buzz Lightyear, who does not believe that he is a toy, and quickly becomes Andy's new favorite toy. Woody, who is now consumed with jealousy, tries to get rid of Buzz. then, both Woody and Buzz are now lost. they must find a way to get back to Andy before he moves without them, but they will have to pass through a ruthless toy killer, Sid Phillips.",
        "After being trapped in a jungle board game for 26 years, a man-child wins his release from the game. but, no sooner has he arrived that he is forced to play again, and this time sets the creatures of the jungle loose on the city. now it is up to him to stop them.",
        "A family wedding reignites the ancient feud between next-door neighbors and fishing buddies John and Max. Meanwhile, a sultry Italian divorcée opens a restaurant at the local bait shop, alarming the locals who worry she'll scare the fish away. But she's less interested in seafood than she is in cooking up a hot time with Max.",
        "Cheated on, mistreated and stepped on, the women are holding their breath, waiting for the elusive \"good man\" to break a string of less-than-stellar lovers. Friends and confidants Vannah, Bernie, Glo and Robin talk it all out, determined to find a better way to breathe."]
'a little boy named andy loves to be in his room, playing with his toys, especially his doll named \"woody\". but, what do the toys do when andy is not with them, they come to life. woody believes that he has life (as a toy) good. however, he must worry about andys family moving, and what woody does not know is about andys birthday party. woody does not realize that andys mother gave him an action figure known as buzz lightyear, who does not believe that he is a toy, and quickly becomes andys new favorite toy. woody, who is now consumed with jealousy, tries to get rid of buzz. then, both woody and buzz are now lost. they must find a way to get back to andy before he moves without them, but they will have to pass through a ruthless toy killer, sid phillips.'
'after being trapped in a jungle board game for 26 years, a man-child wins his release from the game. but, no sooner has he arrived that he is forced to play again, and this time sets the creatures of the jungle loose on the city. now it is up to him to stop them.'
'things dont seem to change much in wabasha county: max and john are still fighting after 35 years, grandpa still drinks, smokes, and chases women , and nobodys been able to catch the fabled \"catfish hunter\", a gigantic catfish that actually smiles at fishermen who try to snare it. six months ago john married the new girl in town (ariel), and people begin to suspect that max might be missing something similar in his life. the only joy max claims is left in his life is fishing, but that might change with the new owner of the bait shop.'
'this story based on the best selling novel by terry mcmillan follows the lives of four african-american women as they try to deal with their very lives. friendship becomes the strongest bond between these women as men, careers, and families take them in different directions. often light-hearted this movie speaks about some of the problems and struggles the modern women face in todays world.'
'george banks must deal not only with the pregnancy of his daughter, but also with the unexpected pregnancy of his wife.'
'hunters and their prey--neil and his professional criminal crew hunt to score big money targets (banks, vaults, armored cars) and are, in turn, hunted by lt. vincent hanna and his team of cops in the robbery/homicide police division. a botched job puts hanna onto their trail while they regroup and try to put together one last big retirement score. neil and vincent are similar in many ways, including their troubled personal lives. at a crucial moment in his life, neil disobeys the dictum taught to him long ago by his criminal mentor--never have anything in your life that you cant walk out on in thirty seconds flat, if you spot the heat coming around the corner--as he falls in love. thus the stage is set for the suspenseful ending....'
'while she was growing up, sabrina fairchild spent more time perched in a tree watching the larrabee family than she ever did on solid ground. as the chauffeurs daughter on their lavish long island estate, sabrina was invisible behind the branches, but she knew them all below... there is maude larrabee, the modern matriarch of the larrabee corporation; linus larrabee, the serious older son who expanded a successful family business into the worlds largest communications company; and david, the handsome, fun-loving larrabee, who was the center of sabrinas world until she was shipped off to paris. after two years on the staff of vogue magazine, sabrina has returned to the larrabee estate but now she has blossomed into a beautiful and sophisticated woman. and shes standing in the way of a billion dollar deal.'
'a mischievous young boy, tom sawyer (jonathan taylor thomas, witnesses a murder by the deadly injun joe. tom becomes friends with huckleberry finn (brad renfro, a boy with no future and no family. tom has to choose between honoring a friendship or honoring an oath because the town alcoholic is accused of the murder. tom and huck go through several adventures trying to retrieve evidence.'
'some terrorists kidnap the vice president of the united states and threaten to blow up the entire stadium during the final game of the nhl stanley cup. there is only one way and one man to stop them...'
'when a deadly satellite weapon system falls into the wrong hands, only agent 007 can save the world from certain disaster. armed with his license to kill, bond races to russia in search of the stolen access codes for \"goldeneye,\" an awesome space weapon that can fire a devastating electromagnetic pulse toward earth. but 007 is up against an enemy who anticipates his every move: a mastermind motivated by years of simmering hatred. bond also squares off against xenia onatopp, an assassin who uses pleasure as her ultimate weapon.'
'comedy-drama about a widowed u.s. president and a lobbyist who fall in love. its all above-board, but \"politics is perception\" and sparks fly anyway.'
'another spoof from the mind of mel brooks. this time hes out to poke fun at the dracula myth. basically, he took \"bram stokers dracula,\" gave it a new cast and a new script and made a big joke out of it. the usual, rich english are attacked by dracula and dr. van helsing is brought in to save the day.'

for doc in docs:
    s = ""
    for token in nlp(doc):
        if token.dep_ == "ROOT":
            s += token.text + " => "
        # print((token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop))
    print(s)