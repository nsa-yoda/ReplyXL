from lib.imagize import Imagize
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print "index"
    return 'Hello there!'

@app.route('/imagize')
def imagize():
    print "imagize"
    #print lib.imagize.__init__()

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)

    I = Imagize()
    print I.generate("As they rounded a bend in the path that ran beside the river, Lara recognized the "
                     "silhouette of a fig tree atop a nearby hill. The weather was hot and the days were "
                     "long. The fig tree was in full leaf, but not yet bearing fruit. Soon Lara spotted other "
                     "landmarks - an outcropping of limestone beside the path that had a silhouette like a man's "
                     "face, a marshy spot beside the river where the waterfowl were easily startled, a tall tree "
                     "that looked like a man with his arms upraised. They were drawing near to the place where "
                     "there was an island in the river. The island was a good spot to make camp. They would "
                     "sleep on the island tonight. Lara had been back and forth along the river path many "
                     "times in her short life. Her people had not created the path - it had always been there, "
                     "like the river - but their deerskin-shod feet and the wooden wheels of their handcarts "
                     "kept the path well worn. Lara's people were salt traders, and their livelihood took them "
                     "on a continual journey. At the mouth of the river, the little group of half a dozen "
                     "intermingled families gathered salt from the great salt beds beside the sea. They groomed "
                     "and sifted the salt and loaded it into handcarts. When the carts were full, most of the "
                     "group would stay behind, taking shelter amid rocks and simple lean-tos, while a band of "
                     "fifteen or so of the heartier members set out on the path that ran alongside the river. "
                     "With their precious cargo of salt, the travelers crossed the coastal lowlands and traveled "
                     "toward the mountains. But Lara's people never reached the mountaintops; they traveled only "
                     "as far as the foothills. Many people lived in the forests and grassy meadows of the "
                     "foothills, gathered in small villages. In return for salt, these people would give "
                     "Lara's people dried meat, animal skins, cloth spun from wool, clay pots, needles and "
                     "scraping tools carved from bone, and little toys made of wood. Their bartering done, "
                     "Lara and her people would travel back down the river path to the sea. The cycle would "
                     "begin again. It had always been like this. Lara knew no other life. She traveled back "
                     "and forth, up and down the river path. No single place was home. She liked the "
                     "seaside, where there was always fish to eat, and the gentle lapping of the waves "
                     "lulled her to sleep at night. She was less fond of the foothills, where the path "
                     "grew steep, the nights could be cold, and views of great distances made her dizzy. "
                     "She felt uneasy in the villages, and was often shy around strangers. The path itself "
                     "was where she felt most at home. She loved the smell of the river on a hot day, and "
                     "the croaking of frogs at night. Vines grew amid the lush foliage along the river, with "
                     "berries that were good to eat. Even on the hottest day, sundown brought a cool breeze "
                     "off the water, which sighed and sang amid the reeds and tall grasses. in a surprisingly "
                     "gentle embrace. His body was as warm and naked as her own, but much bigger and much harder. "
                     "She wondered if Fascinus was with them in the darkness, for she seemed to feel the beating "
                     "of wings between their legs as she was entered by the thing that gave origin to life.")