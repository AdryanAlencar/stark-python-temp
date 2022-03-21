from services.StarkBank import StarkManager
from flask import Blueprint, request
import starkbank
import json

WebhookController = Blueprint(
    'webhook_controller', __name__, template_folder='controllers')
starkManager = StarkManager()


@WebhookController.route('/dispatch', methods=['POST'])
def dispatch():
    data = request.data
    signature_key = request.headers.get("Digital-Signature")
    print(signature_key)
    
    try:
        event = starkManager.validate_signature(data=data, key=signature_key)
        if event.subscription == "invoice" and event.log.type == "credited":
            amount = event.log.invoice.amount
            total = amount - 50 #0.50 pix fee.            

            transfer = starkManager.create_transfer([
                starkbank.Transfer(
                    amount = total,
                    name = "Stark Bank S.A.",
                    taxId = "20.018.183/0001-80",
                    bankCode = "20018183", # if tree digits= > TED, if more = > Pix.
                    branchCode = "0001",
                    accountNumber = "6341320293482496",
                    accountType = "payment"
                )
            ])
            
            return 200

    except starkbank.error.InputErrors as exception:
        return json.dumps({
            "status": "error",
            "message": "Invalid signature"
        }), 400
