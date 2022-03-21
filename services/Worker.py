import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from services.StarkBank import StarkManager
from random import randint
import starkbank
import atexit
import time

starkManager = StarkManager()

def worker():
    invoices_amount = randint(8, 12)
    invoices = []
    for i in range(invoices_amount):        
        # Generate random amount
        amount = randint(1, 1000)

        invoices.append(starkbank.Invoice(
            amount,
            tax_id = "20.018.183/0001-80",
            name = "Stark Bank S.A."            
        ));    
      
    status, created_invoices, erros, message = starkManager.create_invoice(invoices);
    
    if status:
        #logger.info(`${invoices_amount} invoices created;`);
        pass
    else:
        #logger.error(`${invoices_amount} invoices not created;`);
        pass
    
    return created_invoices;


def start_worker():
    starkManager.auth() 
    worker()   
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=worker, trigger="interval", seconds=10800)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())