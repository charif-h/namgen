import re
from nltk.corpus import wordnet

def yearOld(txt):
    if(re.match("\d*-year-old", txt.lower())):
        d = int(txt[:txt.find("-")])
        if(d < 14):
            return "child"
        elif(d < 19):
            return "teenager"
        elif (d < 40):
            return "young"
        elif(d < 60):
            return "adult"
        else:
            return "old"

def unit(txt):
    if (re.match("\d*,?\d*-[a-z]*", txt.lower())):
        u = txt[txt.find("-") + 1:]
        if(u == "year-old"):
            return yearOld(txt)
        else:
            return u
def th(txt):
    if(re.match("^(\d*1st|\d*2nd|\d*3rd|\d+th)", txt)):
        l = re.compile("^(\d*1st|\d*2nd|\d*3rd|\d+th)").split(txt)
        u = l[-1]
        if(u != ""):
            return u[u.find("-") + 1:]
        else:
            return "number"

def getLemma(w):
    d = wordnet.synsets(w)
    if (len(d) > 0):
        return d[0].lemmas()[0].name()

def concepter(word):
    w = str(word)
    reps = {"ment": [""],
            "ed": ["e", ""],
            "ility": ["le"],
            "tion": ["t", ""],
            "ity": [""],
            "ic": ["y", ""],
            "ism": [""],
            "ician": ["y"],
            "ian": [""],
            "al": [""],
            "ive": ["e", ""],
            "ant": [""],
            "ing": ["e", "y", ""],
            "s": [""],
            "er": ["e", ""],
            "-in-law": [""],
            "alize": [""],
            "ally": [""],
            "ly": [""],
            "like": [""],
            "": [""]}
    lemma = None

    for ed in reps.keys():
        if(w.endswith(ed)):
            for v in reps[ed]:
                lemma = getLemma(w.replace(ed, v))
                if(lemma is not None):
                    return lemma
    '''if(w.endswith("ment")):
        lemma = getLemma(w[:-4])
    if(w.endswith("ed")):
        lemma = getLemma(w[:-1])
        if(lemma is None):
            lemma = getLemma(w[:-2])
    if(w.endswith("ility")):
        lemma = getLemma(w.replace("ility", "le"))
    if (w.endswith("tion")):
        lemma = getLemma(w[:-3])
    return lemma'''


lex = ["abandon", "abandoned", "abandonment", "abbess", "ability", "able", "aboard", "abort", "abortion", "abound", "about", "above", "abroad", "abruptly", "absence", "absurd", "absurdity", "abuse", "abused", "abusive", "academic", "academy", "accent", "accept", "acceptance", "access", "accident", "accidental", "accidentally", "accidentaly", "acclaimed", "acclimates", "accompany", "accomplice", "accomplish", "accomplished", "accomplishment", "accordian", "accountant", "accounting", "accuse", "accused", "accustom", "ace", "achieve", "acne", "acolyte", "acquaintance", "acquit", "acrobat", "acrophobia", "across", "act", "action", "action-packed", "action/adventure", "active", "actively", "activist", "activity", "actor", "actress", "actual", "actually", "ad", "adapt", "adaptation", "add", "addiction", "addition", "additional", "address", "adherence", "adjust", "administrator", "admire", "admirer", "adolescent", "adopt", "adoption", "adoptive", "adorable", "adorably", "adore", "adult", "adultery", "adulthood", "advance", "advanced", "advantage", "advent", "adventure", "adventurer", "adversary", "advertise", "advertisement", "advertising", "advice", "affair", "affect", "affection", "affectionately", "affectless", "affirm", "affliction", "affluent", "afloat", "african", "african-american", "after", "afterlife", "aftermath", "afternoon", "again", "against", "age", "agency", "agent", "ago", "agoraphobic", "agree", "agreeable", "agreed", "agreement", "ahead", "aid", "aide", "ail", "aimlessly", "air", "airborne", "airline", "airstrip", "airwave", "aka", "alarm", "albanian", "album", "alchemist", "alcohol", "alcoholic", "alcoholism", "alert", "algerian-born", "alias", "alien", "alienated", "alive", "all", "all-around", "all-girl", "all-out", "all-star", "all-too-easy", "all-white-male", "allegation", "allegedly", "allegiance", "allegory", "allergist", "alley", "allow", "allure", "ally", "almanac", "almost", "alone", "along", "alongside", "already", "also", "altar", "alter", "alternate", "alternately", "alternative", "alters", "although", "always", "amateur", "amazingly", "amazonian", "ambassador", "ambition", "ambitious", "ambivalent", "amends", "american", "amiable", "amish", "amnesia", "amnesiac", "among", "amongst", "amoral", "amorous", "amount", "amour", "amp", "amuse", "amusement", "amusing", "an", "an-exact", "analyze", "anarchist", "ancestor", "ancient", "and", "andrew", "android", "anew", "angel", "anger", "angry", "animal", "animate", "animated", "animation", "animator", "announce", "announces", "annoy", "annoyance", "anonymous", "anorexic", "another", "answer", "anti-fascist", "anti-heroine", "anti-war", "antic", "antique", "anxious", "any", "anymore", "anyone", "anything", "anywhere", "apalled", "apart", "apartheid", "apartment", "apathy", "ape", "apocalypse", "apparent", "apparently", "appeal", "appear", "appearance", "appetite", "appoint", "apprehend", "apprentice", "approach", "approval", "approve", "approves", "aptly", "arab", "arch", "archbishop", "archenemies", "archer", "archetype", "architect", "archival", "archive", "ardor", "area", "arise", "aristocracy", "aristocrat", "aristocratic", "arm", "armed", "armored", "armour-plated", "army", "around", "arouse", "arrange", "arranged", "arrangement", "array", "arrest", "arrival", "arrive", "arrogant", "arson", "arsonist", "art", "artifact", "artist", "artistic", "artistry", "as", "as-yet-unspecified", "ascetic", "ashram", "asian", "aside", "ask", "asleep", "aspect", "aspiration", "aspire", "aspiring", "assassin", "assassinate", "assassination", "assault", "assemble", "assign", "assignment", "assist", "assistance", "assistant", "associate", "assort", "assume", "astonish", "astronaut", "astronomy", "astrophysicist", "asylum", "at", "athlete", "athletic", "atmosphere", "atmospheric", "atoll", "atom", "atop", "atrocity", "attack", "attain", "attempt", "attend", "attendees", "attention", "attic", "attitude", "attorney", "attract", "attracted", "attraction", "attractive", "audacity", "audience", "audio", "audition", "auditor", "aunt", "australian", "austrian", "authentic", "author", "authority", "authorize", "autistic", "auto", "auto-mechanic", "autobiographical", "automobile", "available", "avalanche", "avant-garde", "avenge", "avenger", "average", "avert", "aviator", "avoid", "await", "awaken", "award", "award-winning", "awarded", "aware", "away", "awesome", "awful", "awhile", "awkward", "awry", "b-movies", "baby", "baby-sit", "baby..", "bachelor", "back", "back-drop", "backdrop", "background", "backward", "backwater", "bad", "bad-boy", "bad-guy", "badder", "badge", "badger", "badly", "bag", "baggage", "bagpipe-playing", "bail", "bait", "bakery", "balance", "balcony", "ball", "ball-player", "ballistic", "ballplayer", "bamboo", "ban", "band", "bandleader", "bandmate", "banish", "bank", "banker", "banquet", "bar", "bar-band", "bar/restaurant", "barbed", "bardic", "bare-ass", "barely", "bargain", "barmaid", "barren", "barrier", "bartender", "base", "baseball", "basement", "basic", "basis", "basketball", "bath", "battery", "batting", "battle", "battle-scarred", "battlefield", "bayou", "be", "beach", "bean", "bear", "beast", "beat", "beating", "beau", "beautiful", "beautifully", "beauty", "beauty-", "because", "beckons", "become", "becomes", "bed", "bedroom", "beer", "befall", "befitting", "before", "befriend", "beg", "begin", "beginning", "behalf", "behavior", "behaviour", "behind", "behind-the-scenes", "belief", "believe", "belle", "belong", "belonging", "beloved", "below", "below-ground", "bench", "beneath", "benefit", "bent", "beret", "berserk", "besotted", "best", "best-ever", "bestow", "bet", "betcha", "betray", "betrayal", "better", "between", "beyond", "bickering", "bicycle", "bid", "bidder", "big", "big-time", "bigoted", "bigotry", "bike", "bildungsroman", "bilko", "bill", "billiards", "billionaire", "bimbo", "bind", "bio-dome", "bio-pic", "biography", "biological", "biologist", "biopic", "bird", "birth", "birthday", "birthday-night", "birthright", "bisexual", "bisexuality", "bishop", "bit", "bite", "bitter", "bitterly", "bittersweet", "bizarre", "black", "blackmail", "blade", "blade-wielding", "blame", "blasphemous", "blast", "blathering", "blaze", "bleak", "bleed", "blend", "bless", "blind", "blink", "block", "blockage", "blond", "blonde", "blood", "bloodthirsty", "bloody", "bloom", "blossom", "blow", "blowhard", "blue", "blue-blood", "blunder", "board", "boarding", "boat", "body", "bodyguard", "bohemian", "boiling", "boisterous", "boldly", "bolster", "bolt", "bomb", "bombastic", "bombing", "bombshell", "bonanza", "bond", "bone", "booby", "book", "bookie", "boom", "boost", "booster", "booth", "booze", "border", "bore", "boring", "born", "born-again", "borough", "borrow", "bos", "boss", "botch", "both", "bottom", "bounce", "bound", "boundary", "bourgeoisie", "bowler", "bowling-alley", "box", "boxer", "boxing", "boy", "boyfriend", "boyhood", "boys", "braggart", "brain", "brain-hacking", "brash", "brat", "bratty", "bravery", "bravura", "brazilian", "break", "break-up", "breakdown", "breakfast-cereal", "breaking", "breakup", "breath", "breathe", "breathing", "bribe", "bribery", "brick", "bride", "bridge", "brief", "briefest", "brigade", "brigand", "bright", "brilliant", "brimstone", "bring", "brink", "bristling", "british", "broadcast", "broadly", "broken", "broker", "brothel", "brother", "brother-in-law", "brotherliness", "brotherly", "browbeat", "brownstone", "brutal", "brutalize", "brutally", "bubble", "buck"]
dict = {}
for l in lex:
    lv = []
    v = concepter(l)
    if(dict.get(v) is not None):
        lv = dict[v]
    lv.append(l)
    dict[v] = lv

    #print(l, "\t=>\t", concepter(l))
    #print(l, "\t=>\t", wordnet.synsets(l))
for d in dict.keys():
    print(d, "\t=>\t", dict[d])
print(len(dict))