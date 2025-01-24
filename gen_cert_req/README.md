# Generate Certificate Signing Request (CSR)
These scripts are used to generate a CSR with appropriate SAN information for a CA to sign and generate a certificate. There are two separate ways to do this via the two separate scripts - only one is needed to generate the csr.

### gencert-using-san
1. Edit san.cnf with appropriate info
    1. Ensure SAN info contains commonName as first entry
1. Run `./gencert-using-san [certificate-name]`
1. Copy CSR and submit to CA
1. Download certificate from CA and use as you will


### gencert
This script does not prompt for input.  Simply adjust the settings  within the script itself for the CN, Org, etc. as needed.  All DNS / SAN settings are fed in as arguments.
1. `./gencert.sh domainname.com san1.com san2.com` where `domainname.com` is the Common Name
1. Copy CSR and submit to CA
1. Profit

### Certificate Authorities
* https://your.server.here
* https://your.other.server

---

### Cheat Sheet for OpenSSL:
* Create p12 for import to IIS
	* `openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt`

* Check a Certificate Signing Request (CSR) 
    * `openssl req -text -noout -verify -in CSR.csr`

* Convert private key to PEM
	* `ssh-keygen -f id_rsa -e -m pem`
* Check a private key 
    * `openssl rsa -in privateKey.key -check`
* Check a certificate 
    * `openssl x509 -in certificate.crt -text -noout`
* Check a PKCS#12 file (.pfx or .p12) 
    * `openssl pkcs12 -info -in keyStore.p12`
* Generate a new private key and Certificate Signing Request 
    * `openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key`
* Generate a self-signed certificate (see How to Create and Install an Apache Self Signed Certificate for more info) 
    * `openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:4096 -keyout privateKey.key -out certificate.crt`
* Generate a certificate signing request (CSR) for an existing private key 
    * `openssl req -out CSR.csr -key privateKey.key -new`
* Generate a certificate signing request based on an existing certificate 
    * `openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key`
* Remove a passphrase from a private key 
    * `openssl rsa -in privateKey.pem -out newPrivateKey.pem`
* Check an MD5 hash of the public key to ensure that it matches with what is in a CSR or private key 
    * `openssl x509 -noout -modulus -in certificate.crt | openssl md5`
    * `openssl rsa -noout -modulus -in privateKey.key | openssl md5`
    * `openssl req -noout -modulus -in CSR.csr | openssl md5`
* Check an SSL connection. All the certificates (including Intermediates) should be displayed 
    * `openssl s_client -connect www.paypal.com:443`
* Convert a DER file (.crt .cer .der) to PEM 
    * `openssl x509 -inform der -in certificate.cer -out certificate.pem`
* Convert a PEM file to DER 
    * `openssl x509 -outform der -in certificate.pem -out certificate.der`
* Convert a PKCS#12 file (.pfx .p12) containing a private key and certificates to PEM 
    * `openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes`
    * You can add -nocerts to only output the private key 
    * or add -nokeys to only output the certificates.
* Convert a PEM certificate file and a private key to PKCS#12 (.pfx .p12) 
    * `openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt`
* Remove key passphrase 
    * `openssl rsa -in oldkey.pem -out newkey.pem`
