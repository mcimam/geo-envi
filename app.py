from flask import Flask, jsonify
from numpy import random

app = Flask(__name__)

# Predict Fossil by pict
# Let's say it will use some algorithm
def predict_fossil_by_pict(pict = ''):
    # Run AI alogoritm
    # Unfortunetly, it's impossible to build rn
    # So we emulate it with using random algoritm between 2 pict
    # fossilId = model(pict)
    fossil_id = random.randint(0,1)

    # If In real situation use something like this
    # model = tf.keras.models.load_model('./model/predict_fossil.h5') #Load Model
    # fossil_id = model.predict(pict) #Predict Pict <Vector>
    
    return fossil_id

# API -> Application Programming Interface
# Nerima Input Gambar Fossil
@app.route("/")
def detect_fossil():
    # pict = Req.image
    # Mockup Database
    fossil = [
        {
        'id':1,
        'Kingdom' : 'Animalia',
        'Phylum' : 'Molusca',
        'Class': 'Bivalvia',
        'Ordo' : 'Ostreida',
        'Family' : 'Malleidae',
        'Genus' : 'Isognomon',
        'Species' : 'Isognomon alatus Gmelin, 1791',
        'Description' : 'Isognomon alatus Gmelin, 1791 disebut juga dengan "flat tree oyster". Bagian luar cangkang berwarna krem kecoklatan dan di bagian dalamnya berwarna coklat. Panjang cangkangnya sekitar 75-95 mm dengan tinggi 40-50 mm. Cangkangnya berbentuk iregular yang dihubungkan dengan hinge. Cangkang bertekstur kasar dan terdapat pola seperti melingkar.',
        'Distribution' : 'Carribbean Sea, Gulf of Mexico, Antilles, dan di sepanjang pantai Amerika Selatan bagian tengah dan utara',
        'Paleoenvironment' : 'Akar mangrove, shallow rocky area dengan kedalaman 15 m, area dengan tingkat sedimentasi tinggi, dan di celah antara terumbu karang',
        'Age' : 'Ditemukan pertama kali pada Pleistosen (2,19-0,78 Ma)',
        },
        {
        'id':2,
        'Kingdom' : 'Animalia',
        'Phylum' : 'Atropoda',
        'Class': 'Trilobita',
        'Ordo' : 'Odontopleurida',
        'Family' : 'Odontopleuridae',
        'Genus' : 'Miraspis',
        'Species' : 'Miraspis mira Baraande, 1846',
        'Description' : 'Terlihat adanya duri yang menonjol dari cepahlon thorax dan pygidium. Ciri khas dari Miraspis adalah "spines on spines"',
        'Distribution' : 'Liten Formation, Motol Member, Lodenice, dan Republik Ceko',
        'Paleoenvironment' : 'Marine',
        'Age' : 'Silurian (433-431 Ma)',
        },
    ]

    # Simulasikan bagaimana AI Bekerja
    # choosen_fossil_id = predict_fossil_by_pict(pict)
    choosen_fossil_id = predict_fossil_by_pict()
    # Simulate query select by id
    choosen_fossil = fossil[choosen_fossil_id]

    return jsonify(choosen_fossil)