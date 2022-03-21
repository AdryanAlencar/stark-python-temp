import starkbank
import os


class StarkManager():
    def __init__(self):        
        pass    

    def auth(self):
        """
        Authenticate to Stark Bank API
        """        
        starkbank.user = starkbank.Project(
            environment = "sandbox",
            id = 4534912526843904,
            private_key = "-----BEGIN EC PARAMETERS-----\nBgUrgQQACg==\n-----END EC PARAMETERS-----\n-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIKfUrlOPgWfIZ40HOilT7zPvgE6ofh+vzh2JAGsutpPToAcGBSuBBAAK\noUQDQgAEQVJSXFkE26cwb46dyZAEKoBaLiCFVAdG04NlQieSAiLYnD15UsG89rkl\ndR7iL5fFPpv9hF8JWgPNghZnvPnlOg==\n-----END EC PRIVATE KEY-----"
        )
            

    def create_invoice(self, order = [ ]):
        """#Create an invoice
        Send to Stark Bank a list of Invoice objects and receive a list of Invoice objects in return.
        ## Attributes:
            - order: list of Invoice objects
        ## Returns:
            - Invoice object list
        """
        try:
            invoices = starkbank.invoice.create(order)
            return True, invoices, [], "Invoice created"
        except starkbank.error.InputErrors as exception:
            return False, order,[exception.errors], "Invalid input"
        
    def create_transfer(self, order = [ ]):
        """
        #Create a transfer
        Send to Stark Bank a list of Transfer objects and receive a list of Transfer objects in return.
        ## Attributes:
            - order: list of Transfer objects
        ## Returns:
            - Transfer object list
        """
        try:
            transfers = starkbank.transfer.create(order)
            return True, transfers, [], "Transfer created"
        except starkbank.error.InputErrors as exception:
            return False, order,[exception.errors], "Invalid input"
    

    def validate_signature(self, data, key):
        """#Validate signature
        Validate the signature of a request.
        ## Attributes:
            - data: request body
            - key: public key

        ## Returns:
            - Event object
        """
        try:
            event = starkbank.event.parse(content=data, key=key);

            return True, event, "Signature validated"
        except starkbank.error.SignatureError as exception:
            return False, exception.errors, "Invalid signature"
