import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    def create_payment(self):
        #criar pagamentto na instituicao financeira
        bank_payment_id = uuid.uuid4() #simulamos criancao hash de uma instituicao financeira
        hash_payment = 'hash_payment_{bank_payment_id}' #copia e cola do qr_code
        img = qrcode.make(hash_payment) #criar img do qr_code
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png") #salva imagem como png na pasta img

        return {
                "bank_payment_id": bank_payment_id,
                "qr_code_path": "qr_code_payment_{bank_payment_id}"
            }