import logging
import azure.functions as func
import subprocess
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    subscription_id = req.params.get('subscription_id')
    tenant = req.params.get('tenant')
    secret = req.params.get('secret')
    client = req.params.get('client_id')

    body = req.get_body()

    f = open("./playbook.yml", "wb")
    f.write(body) 
    f.close()

    cmd = "export AZURE_CLIENT_ID=" + client + "; "
    cmd += "export AZURE_SECRET=" + secret + "; "
    cmd += "export AZURE_SUBSCRIPTION_ID=" + subscription_id + "; "
    cmd += "export AZURE_TENANT=" + tenant + "; "
    cmd += "ansible-playbook ./playbook.yml"

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    # output = cmd
    # error = "no error"
    try:
        x = json.dumps({ 'output': str(output), 'error': str(error) })
        #if len(str(output) + str(error)) > 0:
        #    return func.HttpResponse("XXXXXX", headers={"Access-Control-Allow-Origin": "*"})
        #else:
        #    return func.HttpResponse("YYYYYY", headers={"Access-Control-Allow-Origin": "*"})
        return func.HttpResponse(x, headers={"Access-Control-Allow-Origin": "*"})

    except Exception as e:
        return func.HttpResponse("EXCEPTION", headers={"Access-Control-Allow-Origin": "*"})
